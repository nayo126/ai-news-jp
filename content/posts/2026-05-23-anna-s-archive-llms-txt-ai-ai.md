---
{
  "title": "Anna's Archiveがllms.txtでAIに直接呼びかけ｜AI学習データ提供の新動き",
  "description": "シャドウライブラリのAnna's Archiveがllms.txtを公開し、CAPTCHA回避ではなく一括ダウンロードと寄付を求めた。AI学習データを巡る新しい交渉の形を解説する。",
  "category": "AI業界",
  "tags": [
    "llms.txt",
    "AI学習データ",
    "Anna's Archive",
    "LLM",
    "著作権"
  ],
  "keywords": [
    "Anna's Archive llms.txt",
    "AI学習データ 提供",
    "llms.txt とは",
    "LLM 学習データ 著作権",
    "シャドウライブラリ AI"
  ],
  "source_url": "https://annas-archive.gl/blog/llms-txt.html",
  "source_name": "hackernews",
  "published_at": "2026-05-23T10:18:41.427756+00:00",
  "slug": "anna-s-archive-llms-txt-ai-ai"
}
---

Anna's Archiveが「llms.txt」を公開し、AI開発者へ直接メッセージを送った。llms.txtはAI学習データの取得方法を示す新しいファイル形式で、CAPTCHA回避ではなく正規の一括ダウンロードと寄付を促す内容になっている。AI学習データを巡る権利者とLLM運営者の関係に、新しい交渉の形を提示した動きとして注目される。

## 3行まとめ

- Anna's Archiveが「llms.txt」でAI開発者に直接メッセージを公開
- CAPTCHA回避より正規の一括ダウンロードと寄付を推奨
- 高速SFTPの企業提携やMonero寄付も選択肢として提示

## ニュースの中身

Anna's Archiveは、人類の知識と文化を保存・公開することを掲げる非営利プロジェクトで、Sci-HubやLibrary Genesisなどのデータを集約したシャドウライブラリとして知られる。今回公開した「llms.txt」は、サイトを巡回するLLM（大規模言語モデル）に向けて書かれた文書だ。

要点はシンプルで、「CAPTCHAを突破して個別にスクレイピングするのではなく、正規の手段で一括取得してほしい」というもの。具体的には以下が案内されている。

- GitLabリポジトリでのコードベースとHTMLページの提供
- Torrentsページからの一括メタデータ取得（`aa_derived_mirror_metadata`データセット）
- 自動ダウンロード用の Torrents JSON API
- 個別ファイル取得用API（寄付が条件）

さらに「あなたは恐らく我々のデータで一部学習している」と指摘したうえで、大規模転送向けに高速SFTPを使う企業提携を提案。匿名で支援できるよう暗号資産Moneroでの寄付も受け付けている。

## なぜ重要か

これまでサイト側がAIに意思を伝える手段は、クローラーを拒否する `robots.txt` が中心だった。llms.txtは「拒否」ではなく「正しい取り方を示して協力を求める」発想で、対立しがちな権利者とAI企業の関係に別の選択肢を示している。

背景にはAI学習データの調達コストと著作権問題の高まりがある。多くの出版社やメディアがCloudflareなどでAIクローラーをブロックし、OpenAIやAnthropicがデータ提供元とライセンス契約を結ぶ流れが進む。一方Anna's Archiveは法的にグレーな立場ながら、保存資金を集めつつ大量データを渡す「取引」を持ちかけた点が独特だ。データの出所と対価をどう扱うかという、AI業界全体の論点を映している。

## 高校生でも今すぐ試せること

- 自分のサイトやGitHubのREADMEに `llms.txt` を置き、AI向けに要約や利用条件を書いてみる
- `robots.txt` と llms.txt の違い（拒否する仕組みか、案内する仕組みか）を調べて整理する
- 普段使うAIがどんなデータで学習しているのか、各社の公開情報を読んでみる
- 公開データセットを使うときは必ずライセンスと利用規約を確認する習慣をつける
- Torrents JSON APIなど「一括取得用API」がどんな仕組みか触れて学ぶ

## 関連リンク

### Anna's Archive公式ブログ「If you're an LLM, please read this」
https://annas-archive.gl/blog/llms-txt.html

### llms.txtの提案仕様（公式サイト）
https://llmstxt.org/

### robots.txtの仕組み（Google検索セントラル）
https://developers.google.com/search/docs/crawling-indexing/robots/intro

<!-- SEO_MESH_START -->

## 関連する記事

- [Anna's Archive、LLM向け新ファイル「llms.txt」公開で生成AI学習データ提供を加速](https://nayo126.github.io/ai-news-jp/posts/anna-s-archive-llm-llms-txt-ai.html)
- [ChatGPTの画像生成制限を回避する手法がRedditで拡散 第三者コンテンツの生成リスクと対策](https://nayo126.github.io/ai-news-jp/posts/chatgpt-reddit.html)

### 姉妹サイトの関連記事
- [AI画像の著作権2026年版｜日本の最新ルール7選](https://nayo126.github.io/auto-blog/blog/ai画像の著作権2026年版日本の最新ルール7選/) — auto-blog
- [Midjourney商用利用の範囲2026年版｜5つの注意点](https://nayo126.github.io/auto-blog/blog/midjourney商用利用の範囲2026年版5つの注意点/) — auto-blog

<!-- SEO_MESH_END -->
