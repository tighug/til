---
title: ゲーム翻訳ツール
type: concept
sources:
  - "raw/articles/AI Game Translation How to Mod & Translate Game Files.md"
  - "raw/articles/bbepisXUnity.AutoTranslator.md"
  - "raw/articles/davide97lrpgmaker-mv-translator Automatic game data translator for RPGMaker-MV.md"
  - "raw/articles/djethinoUnityGameTranslator Universal Unity games automatic local AI translation and communtity sharing and improvments.md"
  - "raw/articles/RPG-Maker-Translation-Toolsrvpacker-txt-rs A CLI tool to parse RPG Maker games' text to .txt and back.md"
  - "raw/articles/Translator++ Ver. 6.12.26 - A blazingly fast Ruby based RPG Maker parser!.md"
  - "raw/articles/XNA game patcher and plugin framework.md"
related:
  - "[[rpgmaker-translation]]"
  - "[[unity-auto-translator]]"
  - "[[game-localization]]"
  - "[[ai-game-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - game-translation-tools
---

## 概要

ゲーム翻訳ツールとは、ゲーム内テキストの抽出・翻訳・再統合を支援するソフトウェア群のこと。公式ローカライズが提供されないゲームのファンメイド翻訳や、インディー開発者の多言語対応に利用される。

## 翻訳フロー

ゲーム翻訳の基本的な流れは3段階:

1. **テキスト抽出**: ゲームファイルからテキストデータを取り出す
2. **翻訳**: AI翻訳サービスや手動翻訳でテキストを変換
3. **再統合/パッチ**: 翻訳済みテキストをゲームに適用する

## ツールカテゴリ

### RPG Maker系

[[rpgmaker-translation]] を参照。RPG Makerのバージョンごとにデータ形式が異なるため、専用ツールが多数存在する。

- [[translator-plus-plus|Translator++]]: 統合的な翻訳環境。Ruby系RPG Maker向けの高速パーサー搭載
- [[rvpacker-txt-rs]]: テキスト抽出/書き戻しのRust製CLIツール
- [[rpgmaker-mv-translator]]: RPG Maker MV専用のPython自動翻訳ツール

### Unity系

[[unity-auto-translator]] を参照。Modローダー（[[bepinex|BepInEx]]等）を前提とするプラグイン型が主流。

- [[xunity-auto-translator|XUnity.AutoTranslator]]: 最も成熟したUnity翻訳プラグイン。多数の翻訳エンドポイント対応
- [[unity-game-translator|UnityGameTranslator]]: ローカルAI翻訳+コミュニティ翻訳共有に特化した新しいツール

### リアルタイムスクリーン翻訳

ゲームファイルを直接触らず、画面上のテキストをOCRで読み取って翻訳するアプローチ。

- RSTGameTranslation: 複数OCRエンジン対応、Gemini/ChatGPT/Ollama接続可能
- Textractor: ビジュアルノベル向けテキスト抽出ツール

### 基盤ツール

- [[bepinex|BepInEx]]: Unity/XNAゲーム向けModフレームワーク。翻訳プラグインの土台
- MelonLoader: 汎用Unityモッドローダー
- UABE (Unity Assets Bundle Extractor): Unityアセットの抽出・編集

## AI翻訳の活用

近年のゲーム翻訳ツールはAI翻訳との統合が進んでいる:

- **クラウドAPI**: DeepL、Google Translate、OpenAI等の翻訳APIとの直接連携
- **ローカルLLM**: Ollama、LM Studioを使ったオフライン翻訳（コスト・プライバシー面で有利）
- **品質管理**: AI翻訳の後に人手レビュー（human-in-the-loop）を行うワークフローが推奨される
