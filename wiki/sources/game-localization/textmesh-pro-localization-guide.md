---
title: "TextMesh Proローカライズガイド"
type: source-summary
sources:
  - "raw/articles/Make TextMesh Pro Font Assets Responsive to Language Localization Switching.md"
  - "raw/articles/TextMesh Pro Localization.md"
related:
  - "[[textmesh-pro-localization]]"
  - "[[unity-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - unity
  - localization
  - textmesh-pro
---

## 要約

TextMesh Pro（TMP）でのローカライズ対応に関する2つの記事の統合サマリー。言語切り替え時のフォントアセット切り替えの実装パターンと、国際文字セットの管理方法を解説。

## フォントアセットの言語対応（Crazy Minnow Studio）

### アーキテクチャ
- **LanguageManager**: 言語変更を管理する集中管理クラス。C#イベントで言語変更を通知
- **LocalizationResponder**: TMPオブジェクトに付与するヘルパースクリプト。言語変更イベントを購読してフォントアセットを切り替え

### 主な機能
- 言語セット（ラテン、キリル、韓国語等）ごとに集中管理されたフォントアセットスロット
- 個別オブジェクトでのフォントアセットオーバーライド機能
- TMPフォントマテリアルプリセットの再マッピング（異なるフォントアセット間でマテリアルを共有可能）
- M2H Localizationパッケージとの連携（他パッケージへの変更も容易）

## 文字セットの管理とフォールバック（Unity公式チュートリアル）

### ベストプラクティス
- 文字セットごとにフォントアセットをグループ化して作成:
  - Latin (ASCII): 英語、スペイン語、ドイツ語、フランス語等
  - Cyrillic: ロシア語、ギリシャ語等
  - East Asian: 中国語、日本語等
  - Middle Eastern: アラビア語、ペルシア語等

### Font Asset Creator
- Font Asset Creatorで国際文字セットをインポート
- Character SetをUnicode Range (Hex)に設定してUnicode範囲を指定

### Dynamic Fallback
- 日本語の漢字など大量の文字セットに対応する手法
- **Static Font Asset**（カタカナ等の固定文字セット）+ **Dynamic Font Asset**（必要な漢字のみ動的に追加）
- フォールバックチェーン: Regional Font → International Font → Dynamic Fallback

### Global Fallback Font
- 複数言語の文字を同時に表示する場合（言語選択画面等）に使用
- Staticフォールバックで各言語の文字セットを含むフォントを設定
- ビルドサイズとメモリ使用量を最小化

### ローカライズパッケージとの統合
- I2 Localization（Unity Asset Store）がTMPと互換性のある包括的なローカライズパッケージとして紹介されている
