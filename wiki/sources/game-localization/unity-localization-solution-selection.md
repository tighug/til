---
title: "Unityローカライズソリューション選定の考慮事項"
type: source-summary
sources:
  - "raw/articles/Factors to Consider When Choosing a Localization Solution for Unity.md"
related:
  - "[[unity-localization]]"
  - "[[textmesh-pro-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - unity
  - localization
---

## 要約

Pocket Gems社が「Adventure Chef: Merge Explorer」を9言語でリリースした経験から、Unityローカライズソリューション選定時に検討すべきポイントを整理した記事。

## ローカライズ対象の洗い出し

- **文字列**: ルックアップテーブル（キー→翻訳値）が基本。動的文字列置換や文脈メタデータ（性別・数量等）のサポートが必要
- **数値・通貨・日付**: C#の`CultureInfo`を使うが、UnityのMono実装では`CultureInfo.CurrentCulture`が正しく返らないためネイティブプラグインが必要
- **外部API**: アプリ内ストア等の外部サービスからの文字列もローカライズ対象
- **画像・テクスチャ・VFX**: テキストを含むアセットも別途対応が必要
- **ストアページ・マーケティング素材**: ゲーム内だけでなくストアページの翻訳も重要

## フォントの考慮事項

- Unicodeフォントでも全言語の全文字を含むことは不可能
- 言語ファミリー（ラテン、アラビア、キリル等）ごとにフォントを用意するか、フォールバックフォントを設定
- TextMeshProはフォールバックフォントとグリフテーブルのカスタマイズに対応
- 大規模な文字セットはメモリ消費に注意

## パフォーマンスへの影響

- **アプリサイズ**: フォントバンドルによるサイズ増加。必要時ダウンロードやシステムフォント利用も選択肢
- **データ構成**: 単一テーブル vs 複数テーブル（言語別・機能別）の設計判断
- **開発パイプライン**: 翻訳追加→翻訳者への送付→インポートのワークフロー設計が重要

## Pocket Gemsの選定結果

- I2 Localization、Lean Localization、Unity Localization Package、オンラインサービスを評価
- **Unity Localization Packageを採用**: Addressablesベースで既存のアセットロードと統合しやすく、CSV/Google Sheetsのインポート・エクスポート対応、pseudo localeによるUIテスト機能あり
- ラッパーレイヤーを構築し、プロジェクト全体のローカライズキーを自動スキャンするユーティリティを開発
