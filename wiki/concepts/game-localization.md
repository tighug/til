---
title: "ゲームローカライズ"
type: concept
sources:
  - "raw/articles/10 Best Game Localization Tips to Level Up Any Title.md"
  - "raw/articles/10 Best Practices for Game Localization.md"
  - "raw/articles/Best Practices for Game Localization Your Video Game Localization Guide.md"
  - "raw/articles/Game localization process 8 essential steps for successful global launch.md"
  - "raw/articles/Game Localization The 2025 Guide.md"
  - "raw/articles/Game Translation and Localization – A Definitive Guide.md"
  - "raw/articles/Gaming Localization A Comprehensive 2025 Guide.md"
  - "raw/articles/The 2025 Gaming Localization Guide.md"
  - "raw/articles/The Complete Guide to Game Localization.md"
  - "raw/articles/8 video game localization examples you won't forget.md"
  - "raw/articles/ゲームローカライズを成功に導く翻訳の依頼方法 - ブログ - SunFlare Style.md"
  - "raw/articles/ゲーム翻訳の現場に迫る！日本語ローカライズの作業とは？（前編）.md"
related:
  - "[[game-localization-qa]]"
  - "[[localization-vs-translation]]"
  - "[[ai-game-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - game-localization
---

## 定義

ゲームローカライズとは、ビデオゲームを別の地域・言語・文化圏のプレイヤー向けに適応させるプロセス。単なるテキスト翻訳（[[localization-vs-translation]]参照）ではなく、文化的適応（カルチャライゼーション）・音声・ビジュアル・法的対応を包含する。

> "The secret to great localization is to make it seem as if the game was made in the language that the player is playing." -- Patrick Gortjes, Ubisoft

## ローカライズ対象要素

| カテゴリ | 対象 |
|---------|------|
| テキスト | UI、ダイアログ、字幕、クエストテキスト、アイテム名、チュートリアル |
| 音声 | ボイスオーバー、効果音、楽曲（著作権考慮） |
| ビジュアル | テクスチャ、看板、アイコン、キャラクターデザイン、ボックスアート |
| マーケティング | ストア説明文、トレイラー、広告、SNS |
| 法的 | 年齢レーティング、免責事項、プライバシーポリシー、マイクロトランザクション表示 |

## プロセス

1. **国際化（i18n）**: コードレベルでの多言語対応準備。テキスト外部化、Unicode対応、テキスト拡張余地確保、RTL対応
2. **市場分析**: ターゲット市場の選定。EFIGS → CJK → アラビア語が一般的な優先順位。ジャンル人気・規制・競合も調査
3. **ローカライズキット作成**: スタイルガイド、用語集、キャラクター設定、ゲーム概要をまとめた資料パッケージ
4. **翻訳・文化適応**: ネイティブかつゲームに精通した翻訳者による作業。CATツール・翻訳メモリ・TMSを活用
5. **音声ローカライズ**: 地域方言・アクセントの選択、声優キャスティング、リップシンク調整
6. **テスト・LQA**: 言語・機能・文化の3層テスト（[[game-localization-qa]]参照）
7. **リリース・継続更新**: ライブサービスゲームでは継続的ローカライズが必要

## リリースモデル

- **シムシップ（同時出荷）**: 全言語版を同時リリース。売上の37%が発売3週間以内に集中するため理想的だが複雑
- **ポストゴールド**: オリジナル版リリース後にローカライズ版。簡単だが収益機会損失
- **混合モデル**: 主要言語は同時、残りは後日。From Softwareの『Elden Ring』DLCが好例

## ローカライズの範囲

- **部分的**: 字幕・UI翻訳のみ。音声は原語。任天堂の西洋向けリリースで一般的
- **完全**: テキスト・音声・ビジュアル全てを適応。AAA作品で標準
- **カルチャライゼーション**: 言語を超えた深い文化適応。ストーリー・キャラクターデザイン・ゲームメカニクスの変更を含む

## ベストプラクティス

- **開発初期からローカライズを計画する**: 後付けは技術的負債とコスト増大の原因
- **テキストをコードから分離**: ハードコーディングは厳禁。JSON/XML/CSVの外部リソースファイルを使用
- **テキスト拡張に備えたUI設計**: ドイツ語は英語比20-30%長い。中国語は逆に短くなる
- **言語コードを使う（国旗ではなく）**: `en-US`、`fr-FR`など。一つの国旗が一つの言語を表さない
- **コンテキストを十分に提供**: スクリーンショット・動画・コメントで翻訳者に文脈を共有
- **一貫性を保つ**: 用語集とスタイルガイドで訳語統一。翻訳メモリで再利用

## 文化適応の注意点

- **色の象徴**: 赤は中国で幸運、南アフリカで喪。緑は中国で不倫を連想させうる
- **暴力・ゴア**: 中国では赤い血禁止、ドイツでは人間への暴力が検閲対象
- **宗教的シンボル**: 『LittleBigPlanet』はコーラン引用で回収
- **骸骨表現**: 中国では禁止。『Fortnite』『World of Warcraft』中国版で骨を別オブジェに置換
- **キャラクターデザイン**: 任天堂のカービィは日本版=可愛い、米国版=好戦的な表情

## 法規制

- **年齢レーティング**: PEGI（欧州）、ESRB（北米）、CERO（日本）、GRAC（韓国）で基準が異なる
- **ナチス表現**: ドイツでは2018年まで禁止
- **マイクロトランザクション**: EU（2025年3月）で仮想通貨の実額表示ガイドライン
- **著作権**: 任天堂『Mother 3』は楽曲著作権問題で西洋リリース困難

## 翻訳依頼先の選択

- フリーランス翻訳者: コスト安だが品質管理・スケーラビリティに課題
- 翻訳会社: 品質チェック工程付き。ゲーム特化翻訳会社もあり
- オンライン翻訳サービス: Gengo等。スピード重視の場合に有効

## 市場データ

- 2025年のゲーム市場規模: 約2,300億ドル
- 上位市場: 中国（487億ドル）、米国（476億ドル）、日本（166億ドル）、韓国（71億ドル）、ドイツ（64億ドル）
- Steamの言語シェア: 英語34%、簡体字中国語29%、ロシア語10%
- 58%のゲーマーが母国語のゲームを購入する可能性が高い

## 著名な事例

- **Ubisoft**: 社内ローカライズ部門。Snowdropエンジン + Oasis + ローカライズ管理プラットフォーム
- **The Witcher 3**: 15言語以上。地域の民話・なぞなぞを文化適応、地域ごとの声優起用
- **Ghost of Tsushima**: 米国開発の日本時代劇。ローカライズが「逆方向」で時代・文化考証に協力。「Yuriko」→「百合」の歴史考証
- **Dragon Quest XI**: 英語版で地域方言声優・韻文・俳句を追加。RPGローカライズの最高峰と評価
- **Genshin Impact**: 中日韓英の完全音声対応。文化イベントも各地域に適応
