---
title: BepInEx
type: source-summary
sources:
  - "raw/articles/XNA game patcher and plugin framework.md"
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

Unity Mono、IL2CPP、.NETフレームワークゲーム（XNA, FNA, MonoGame等）向けのプラグイン/Modフレームワーク。ゲーム翻訳ツールの前提となるModローダーとして重要。

## 要点

- 正式名称: Bepis Injector Extensible
- 対応プラットフォーム
  - Unity Mono: Windows / macOS / Linux（安定版リリースあり）
  - Unity IL2CPP: Windows / Linux（macOS未対応）
  - .NET / XNA: Windows / Mono（macOS, Linux）
- XUnity.AutoTranslatorやUnityGameTranslator等の翻訳プラグインの基盤として利用
- 多数のプラグインローダーに対応: BSIPA、IPA、MelonLoader、MonoMod、Unity Mod Manager等
- ライセンス: LGPL-2.1
- Bleeding Edgeビルド（BepInEx 6）はIL2CPP対応を含むが開発中
