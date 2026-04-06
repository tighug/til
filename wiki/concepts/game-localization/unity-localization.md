---
title: "Unityゲームのローカライズ手法"
type: concept
sources:
  - "raw/articles/Factors to Consider When Choosing a Localization Solution for Unity.md"
  - "raw/articles/How to Use the Unity Localization Package A Complete Guide.md"
  - "raw/articles/Localizing Unity Games As An Indie Dev.md"
  - "raw/articles/Localizing Unity Games Step by Step.md"
related:
  - "[[textmesh-pro-localization]]"
  - "[[game-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - unity
  - localization
---

## 概要

Unityでゲームをローカライズするための手法とツールの選択肢。公式パッケージからサードパーティ、独自実装まで、プロジェクト規模や要件に応じた選択が重要になる。

## 主要なローカライズソリューション

### Unity Localization Package（公式）
- Addressablesベースの公式ローカライズパッケージ
- **String Table**で翻訳テキストを管理し、**Asset Table**で画像・音声等を言語別に管理
- **Smart Strings**で動的文字列（複数形、通貨、日付フォーマット等）に対応
- **Localize String Event**コンポーネントでTextMesh Proと連携し、ロケール変更時に自動更新
- CSV / Google Sheetsのインポート・エクスポートに対応
- pseudo localeによるUIオーバーフローのテスト機能
- 無料で利用可能

### I2 Localization
- Unity Asset Storeで入手可能なサードパーティパッケージ
- TextMesh Proと互換性あり
- 長い実績と広いユーザーベースを持つ

### Lean Localization
- 軽量なローカライズパッケージ

### 独自実装
- Google Sheets + カスタムスクリプトによる軽量アプローチ
- `SystemLanguage` enumでUnity内の言語管理を統一
- Google Sheets Scriptでweb APIエンドポイントを公開し、JSONで翻訳データを取得

## ローカライズ設計の考慮事項

### 対象の範囲
- UI文字列（最低限）
- 数値・通貨・日付（`CultureInfo`の扱いに注意）
- 画像・テクスチャ内のテキスト
- 音声・アニメーション
- ストアページ・スクリーンショット

### フォント
- 言語ファミリーごとにフォントアセットを用意（ラテン、キリル、東アジア、中東）
- TextMesh Proのフォールバックフォント機能を活用
- 使用文字のみをスキャンしてフォントアセットを生成するとサイズを大幅削減可能
- 日本語と中国語で同じフォントを使うべきでない（[[textmesh-pro-localization]]参照）

### 翻訳ワークフロー
- 翻訳キーの追加→翻訳者への送付→翻訳のインポートの流れを自動化することが重要
- Global Variablesでリアクティブな動的文字列を実現（値変更時に自動再描画）
- リモートコンテンツ配信で、アプリ更新を待たずに翻訳を更新可能

### RTL（右から左）言語
- TextMesh Proは公式RTLサポートなし
- **RTLTMPro**パッケージで対応（アラビア語、ヘブライ語、ペルシア語等）
- 混在テキスト（LTR + RTL）ではForce Fixオプションが必要

### ビルドと配信
- Addressablesは手動ビルドが必要（自動ビルドされない）
- エディタ上で動作してもビルドで失敗するケースに注意
- Addressables v1.16.16に既知バグあり

## 関連ソース

- [[unity-localization-solution-selection]]
- [[unity-localization-package-guide]]
- [[unity-localization-indie-dev]]
- [[textmesh-pro-localization-guide]]
