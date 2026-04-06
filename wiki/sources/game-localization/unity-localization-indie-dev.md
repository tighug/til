---
title: "インディー開発者によるUnityローカライズ実践"
type: source-summary
sources:
  - "raw/articles/Localizing Unity Games As An Indie Dev.md"
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

「Pine Tar Poker」のインディー開発者が、Google Sheets + カスタムスクリプトによるUnityローカライズのワークフローを解説した記事。Unity公式パッケージを使わず、独自の軽量ローカライズシステムを構築した事例。

## 翻訳管理（Google Sheets）

- **メインシート**: 全言語のString ID・説明・翻訳を集約。言語ごとの「エクスポート」タブ（key/valueのみ）を生成
- **翻訳者用シート**: 言語ごとに別ファイルを作成し、翻訳者にスコープ付き書き込み権限を付与
- `=GOOGLETRANSLATE($B2, "en", "fr")` でプレースホルダー翻訳を生成（テスト用、出荷はしない）
- バージョン履歴による変更追跡

## Unity側の実装

### String Downloader
- Google Sheets ScriptでWeb APIエンドポイントを公開
- `?sheet=FrenchExport`等でJSON形式の翻訳データを取得
- `SystemLanguage` enumを使って言語名とシート名を統一
- ダウンロードしたJSONをCSVに変換し`Resources`ディレクトリに保存

### Font Asset Generation
- TextMesh ProのSDF font assetを使用
- 中国語・日本語等の大規模文字セットでは全Unicodeレンジの生成は非現実的（8Kテクスチャで23分以上かかる）
- **実際に使用する文字だけをスキャン**して1024x1024テクスチャを高速生成（半秒で完了）

### Localization Manager
- 現在の言語の取得・設定を担当し、言語変更時にC#イベントを発火
- 言語ごとにフォントアセットを割り当て（日本語・中国語用フォントとラテン文字用フォント等）
- 日本語と中国語で同じフォントを使うべきでない（グリフの見た目が異なる）
- UI空間と3D空間のTMPで別々のフォントアセット（またはマテリアル）が必要

### Localized Text Mesh
- **静的文字列**: String IDを指定して自動翻訳
- **書式付き文字列**: `{0}`パラメータで動的値を挿入（言語により位置が変わる）
- **動的文字列**: `SetText`メソッドで実行時に文字列を設定

## 翻訳者の調達

- fiverr.comで個別に翻訳者を探す手法
- ローカライズガイド（スライドショー）を作成して翻訳品質を向上
- 翻訳者にiOS/Androidコードを送付してゲームを体験してもらう
