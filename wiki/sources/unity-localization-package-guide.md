---
title: "Unity Localization Packageの使い方ガイド"
type: source-summary
sources:
  - "raw/articles/How to Use the Unity Localization Package A Complete Guide.md"
  - "raw/articles/Localizing Unity Games Step by Step.md"
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

Unity公式Localization Packageのインストールから本番ビルドまでをカバーする2つのガイド記事の統合サマリー。

## セットアップ手順

1. **パッケージインストール**: Package Managerから`com.unity.localization`を追加（Addressablesも自動インストール）
2. **Localization Settings作成**: Edit > Project Settings > Localizationで設定アセットを生成
3. **ロケール生成**: Locale Generatorで対象言語のロケールアセットを作成
4. **ロケールセレクター設定**: コマンドライン引数 → システムロケール → 固定ロケールの優先順で解決

## String Table

- Window > Asset Management > Localization Tablesで**String Table Collection**を作成
- キー（snake_case）と各ロケールの翻訳テキストを登録
- 用途別にテーブルを分割（UI、Dialogue、Tutorial等）

## TextMesh Proとの連携

- **Localize String Eventコンポーネント**をTMPオブジェクトに追加
- String ReferenceでテーブルとキーをP指定
- Update Stringイベントで`TMP_Text.text`に自動反映
- ロケール切り替え時に自動更新される

## Smart Strings（動的文字列）

- `{VariableName}`でプレースホルダーを定義
- **複数形**: `{Count:plural:{} item|{} items}`（言語ごとの複数形ルールに自動対応、アラビア語は6形式）
- **数値フォーマット**: `{Amount:C}`で通貨、`{Count:N2}`で小数点以下2桁
- **日付フォーマット**: `{Date:d MMM}`等の.NETフォーマット指定子を利用
- MonoBehaviourのpublicフィールドをFormat Argumentsに登録して値を提供

## Global Variables

- `Create > Localization > Global Variables Group`でリアクティブな変数を作成
- Localization SettingsのString Database > Sourcesに登録
- 翻訳文字列内で`{group-name.variable-name}`構文で参照
- 値の変更時にUIが自動で再描画される

## Asset Table（画像・音声等のローカライズ）

- **Asset Table Collection**でスプライト、AudioClip、テクスチャ等を言語別に管理
- Localize Sprite Event、Localize Audio Clip Event等の専用コンポーネントで自動切り替え

## RTL（右から左）言語対応

- TextMesh Proは公式RTLサポートなし → **RTLTMPro**パッケージで対応
- `UI > Text - RTLTMP`コンポーネントを使用
- 英語テキストで始まる混在文字列では**Force Fix**オプションを有効化

## ランタイムでの言語切り替え

- `LocalizationSettings.SelectedLocale`で現在のロケール取得・設定
- `LocalizationSettings.AvailableLocales.GetLocale("en")`で特定ロケールを取得
- 設定は自動で永続化される

## ビルド時の注意

- Addressablesは自動ビルドされない → **Build > New Build > Default Build Script**で手動ビルドが必要
- Addressables v1.16.16に翻訳が読み込まれない既知バグあり（v1.16.15にダウングレードで解決）
- エディタ上では動くがビルドで失敗するパターンに注意
