#!/usr/bin/env python3
"""ai-news-jp用 アフィリエイトカード自動注入

各記事末尾に「関連商品」セクションを追加。
MIDS (~/MONETIZATION_IDS.json) の楽天/もしも/忍者AdMaxがTODO以外なら本番リンク。
そうでなければ検索URL（後で遡及更新される）。

べき等更新: <!-- AFF_CARD_START/END --> で囲む。
"""
from __future__ import annotations
import json
import re
import os
import sys
import urllib.parse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "inject_affiliate.log"
POSTS_DIR = ROOT / "content" / "posts"
LOG.parent.mkdir(exist_ok=True)
MIDS_PATH = Path.home() / "MONETIZATION_IDS.json"

CARD_START = "<!-- AFF_CARD_START -->"
CARD_END = "<!-- AFF_CARD_END -->"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_ids() -> dict:
    if not MIDS_PATH.exists():
        return {}
    try:
        return json.loads(MIDS_PATH.read_text())
    except Exception:
        return {}


IDS = load_ids()
def _resolve_rakuten_id(platform: str = "ai-news-jp") -> str:
    r = (IDS.get("rakuten_affiliate") or {})
    ids_map = r.get("ids") or {}
    routing = r.get("routing") or {}
    if platform in routing and routing[platform] in ids_map:
        v = ids_map[routing[platform]]
        if v and v != "TODO":
            return v
    v = ids_map.get("main")
    if v and v != "TODO":
        return v
    v = r.get("affiliate_id")
    return v if v and v != "TODO" else ""


RAKUTEN_ID = _resolve_rakuten_id("ai-news-jp")
RAKUTEN_OK = bool(RAKUTEN_ID)
NINJA_TAG = (IDS.get("ninja_admax") or {}).get("ad_tag_html")
NINJA_OK = bool(NINJA_TAG) and NINJA_TAG != "TODO"


def rakuten_link(keyword: str) -> str:
    q = urllib.parse.quote(keyword)
    search = f"https://search.rakuten.co.jp/search/mall/{q}/"
    if RAKUTEN_OK:
        return (
            f"https://hb.afl.rakuten.co.jp/hgc/{RAKUTEN_ID}/?pc="
            + urllib.parse.quote(search, safe="")
            + "&link_type=text"
        )
    return search


def amazon_link(keyword: str) -> str:
    q = urllib.parse.quote(keyword)
    return f"https://www.amazon.co.jp/s?k={q}"


def parse_jsonfm(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(\{.*?\n\})\s*\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        return json.loads(m.group(1)), m.group(2)
    except json.JSONDecodeError:
        return {}, text


def card_block(keywords: list[str]) -> str:
    # 各記事 1〜2 個のキーワードでカード表示
    if not keywords:
        return ""
    bits = [
        CARD_START,
        "",
        "## 関連書籍・ツール",
        "",
    ]
    for kw in keywords[:2]:
        bits.extend([
            f'<aside class="affiliate-card">',
            f'<div class="label">{kw} に関連する書籍・ツール</div>',
            f'<p>「{kw}」について実践的に学ぶための参考リソース</p>',
            f'<p><a href="{rakuten_link(kw)}" target="_blank" rel="sponsored noopener">▶ 楽天市場で見る</a></p>',
            f'<p><a href="{amazon_link(kw)}" target="_blank" rel="sponsored noopener">▶ Amazonで見る</a></p>',
            f'</aside>',
            "",
        ])
    if NINJA_OK:
        bits.append(NINJA_TAG)
        bits.append("")
    bits.append(CARD_END)
    return "\n".join(bits)


def upsert(text: str, block: str) -> str:
    if not block:
        return text
    pattern = re.compile(re.escape(CARD_START) + r".*?" + re.escape(CARD_END), re.DOTALL)
    if pattern.search(text):
        return pattern.sub(block, text)
    return text.rstrip() + "\n\n" + block + "\n"


def main() -> int:
    log(f"=== inject (rakuten={RAKUTEN_OK} ninja={NINJA_OK}) ===")
    if not POSTS_DIR.exists():
        log("posts dir missing")
        return 1

    force_all = "--all" in sys.argv or os.environ.get("ALL") == "1"
    touched = 0
    for md in POSTS_DIR.glob("*.md"):
        try:
            text = md.read_text()
        except Exception:
            continue
        fm, body = parse_jsonfm(text)
        if not fm:
            continue
        # Skip if card already exists and not forcing
        if CARD_START in text and not force_all:
            continue
        kws = fm.get("keywords", []) or fm.get("tags", []) or []
        if not kws:
            continue
        block = card_block(kws)
        new = upsert(text, block)
        if new != text:
            md.write_text(new)
            touched += 1
    log(f"=== done: {touched} posts updated ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
