---
title: UnityGameTranslator
type: source-summary
sources:
  - "raw/articles/djethinoUnityGameTranslator Universal Unity games automatic local AI translation and communtity sharing and improvments.md"
related:
  - "[[unity-auto-translator]]"
  - "[[game-translation-tools]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - game-translation-tools
---

## 概要

djethino氏が開発するUnityゲーム向け汎用翻訳Mod。ローカルAI翻訳とコミュニティ翻訳共有を特徴とする。ベータ版。

## 要点

- OpenAI互換APIを使ったAI翻訳（ローカルまたはクラウド）
  - ローカル: Ollama、LM Studio（無料、オフライン動作可能）
  - クラウド: Groq、OpenRouter、OpenAI
  - 推奨ローカルモデル: `qwen3:8b`（6-8GB VRAM必要）
- 対応Modローダー: BepInEx 5/6、MelonLoader（Mono / IL2CPP両対応）
- ランタイム翻訳: ゲームプレイ中にテキストを検知して翻訳
- 数値正規化: "Kill 5 enemies" と "Kill 10 enemies" で翻訳キャッシュを共有
- **コミュニティ翻訳機能**
  - 翻訳のダウンロード・アップロード・共有
  - Steam IDやプロダクト名による自動ゲーム検出
  - Main/Branch/Forkモデルによる協調翻訳
  - 3-wayマージによるインテリジェントな翻訳統合
- 翻訳品質タグシステム: H（Human）= 3点、V（Validated）= 2点、A（AI）= 1点
- Capture Keys Onlyモード: AIなしでテキストキャプチャのみ行い、Webサイトで人手翻訳→100%人間翻訳を実現
- ゲーム内オーバーレイUI（F10で設定画面表示）
- Windows / macOS / Linux対応
- AGPL準拠でセルフホスト可能
