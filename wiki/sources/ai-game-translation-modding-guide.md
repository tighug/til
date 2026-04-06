---
title: "AI Game Translation: How to Mod & Translate Game Files"
type: source-summary
sources:
  - "raw/articles/AI Game Translation How to Mod & Translate Game Files.md"
related:
  - "[[game-translation-tools]]"
  - "[[unity-auto-translator]]"
  - "[[rpgmaker-translation]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - game-translation-tools
---

## 概要

AIを使ったゲーム翻訳Modの作成手順を解説するガイド記事。

## 要点

- ゲーム翻訳の基本フロー: **テキスト抽出** → **AI翻訳** → **再統合/パッチ適用**
- リアルタイムスクリーン翻訳ツール（OCRベース）
  - RSTGameTranslation: 複数OCRエンジン対応、Gemini/ChatGPT/Ollamaに接続可能
  - Tap to Translate Screen: モバイル向けオーバーレイ翻訳
- Modder向けツールキット
  - [[unity-auto-translator|XUnity.AutoTranslator]]: Unityゲーム向けリアルタイム翻訳プラグイン
  - DeepL API: 高品質なニューラル機械翻訳、月50万文字まで無料
  - Textractor: ビジュアルノベル等のテキスト抽出ツール
- Unityゲームの場合はUABE (Unity Assets Bundle Extractor) でアセット抽出
- Unreal Engineの場合は UnrealPak / FModel で .pak ファイルを抽出
- AI翻訳後の人手レビュー（human-in-the-loop）が品質向上に不可欠
- DeepLのグロッサリー機能でキャラ名や固有名詞の訳語統一が可能
