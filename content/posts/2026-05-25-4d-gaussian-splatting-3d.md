---
{
  "title": "4D Gaussian Splattingとは？通常動画から自由視点3Dを再構成する技術を解説",
  "description": "4D Gaussian Splattingは平面の動画を立体データ化し、撮影していない角度の映像も再構成できる3D技術。NeRFとの違いや活用例、無料で試す方法を初心者向けに解説する。",
  "category": "AIツール",
  "tags": [
    "Gaussian Splatting",
    "3D再構成",
    "NeRF",
    "AI技術",
    "動画編集"
  ],
  "keywords": [
    "4D Gaussian Splatting とは",
    "ガウシアンスプラッティング",
    "動画から3D 再構成",
    "NeRF 違い",
    "自由視点 映像 AI"
  ],
  "source_url": "https://reddit.com/r/singularity/comments/1tmxpbj/reconstructing_different_angles_from_live_footage/",
  "source_name": "reddit/r/singularity",
  "published_at": "2026-05-25T10:17:19.224747+00:00",
  "slug": "4d-gaussian-splatting-3d"
}
---

## 3行まとめ
- 4D Gaussian Splattingが通常動画から3D空間を再構成
- 平面の映像を立体化し、撮影していない角度も再生できる
- スマホ撮影にも応用が進む注目の3D表現技術

## ニュースの中身
Redditのr/singularityで、4D Gaussian Splattingという技術が話題になった。投稿者は「ライブ映像から異なるカメラアングルを再構成できる」点を取り上げ、平面の画像を三次元の空間データに変換する仕組みに驚いたと述べている。

Gaussian Splattingは、2023年にInria（フランス国立情報学自動制御研究所）のチームがSIGGRAPH 2023で発表した3D表現手法だ。シーンを無数の「ガウシアン」と呼ばれる半透明の点の集まりとして表現する。従来注目されていたNeRF（Neural Radiance Fields）よりレンダリングが高速で、リアルタイム表示に向くのが大きな特徴とされる。

「4D」は、この3D表現に時間軸を加えたもの。静止した風景だけでなく、動く人物や変化する場面も立体的に記録できる。結果として、1台のカメラで撮った平面の動画から、撮影していない角度の映像を生成したり、視点を自由に動かして再生したりすることが可能になる。

## なぜ重要か
これまで自由視点の映像を作るには、多数のカメラを並べた専用スタジオが必要だった。Gaussian Splatting系の手法は、少ない枚数の画像や1本の動画からでも空間を再構成できるため、制作コストを大きく下げる可能性がある。

NeRFと比べた利点は処理速度だ。NeRFは高品質だが学習と描画に時間がかかる場面が多い。Gaussian Splattingは描画が軽く、Webブラウザ上での表示も実用域に入りつつある。

活用が見込まれる分野は幅広い。映画やMVの特殊効果、スポーツのリプレイ、VR/ARコンテンツ、不動産や商品の3D展示などだ。動画という身近な素材から立体データを作れる点は、個人クリエイターにとっても参入しやすい流れといえる。

## 高校生でも今すぐ試せること
- 「Gaussian Splatting」「Luma AI」などのキーワードで、ブラウザで動く公開デモを検索して動かしてみる
- Luma AIなどの無料アプリで、自分の机の上の小物をスマホで一周撮影し、3Dデータ化を体験する
- NeRFとGaussian Splattingの違いを、速度・画質の観点で1枚のメモにまとめてみる
- 撮影時は被写体の周りをゆっくり一定速度で回り、明るさを保つと再構成の精度が上がる
- 作った3Dモデルや比較メモを学んだ記録としてSNSやブログに残す

## 関連リンク
### [reconstructing different angles from live footage (r/singularity)](https://reddit.com/r/singularity/comments/1tmxpbj/reconstructing_different_angles_from_live_footage/)
### [3D Gaussian Splatting for Real-Time Radiance Field Rendering（Inria公式プロジェクト）](https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/)
### [Luma AI（スマホで3D再構成を試せるツール）](https://lumalabs.ai/)