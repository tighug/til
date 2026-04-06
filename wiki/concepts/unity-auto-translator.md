---
title: Unity向け自動翻訳ツール
type: concept
sources:
  - "raw/articles/bbepisXUnity.AutoTranslator.md"
  - "raw/articles/djethinoUnityGameTranslator Universal Unity games automatic local AI translation and communtity sharing and improvments.md"
  - "raw/articles/XNA game patcher and plugin framework.md"
  - "raw/articles/AI Game Translation How to Mod & Translate Game Files.md"
related:
  - "[[game-translation-tools]]"
  - "[[rpgmaker-translation]]"
  - "[[game-localization]]"
  - "[[ai-game-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - game-translation-tools
---

## 概要

Unity製ゲームの翻訳は、Modローダーを通じてランタイムでテキストをフックし翻訳する「プラグイン方式」が主流。ゲームファイルの直接編集が不要で、プレイしながらリアルタイムに翻訳が適用される。

## アーキテクチャ

```
[Unityゲーム] → [Modローダー (BepInEx等)] → [翻訳プラグイン] → [翻訳エンドポイント]
                                                    ↓
                                            [翻訳キャッシュ]
```

1. [[bepinex|BepInEx]] や MelonLoader 等のModローダーがゲームプロセスに注入
2. 翻訳プラグインがHarmonyパッチでテキスト表示処理をフック
3. 表示されるテキストをインターセプトし、翻訳エンドポイント（API / ローカルLLM）に送信
4. 翻訳結果をキャッシュし、UIに反映

## 主要ツール比較

| 項目 | XUnity.AutoTranslator | UnityGameTranslator |
|---|---|---|
| 開発者 | bbepis | djethino |
| 成熟度 | 高（長期メンテナンス） | ベータ |
| 翻訳エンドポイント | Google, DeepL, Bing, Papago等 + サードパーティLLM | OpenAI互換API（ローカル/クラウド） |
| コミュニティ翻訳共有 | 手動（ファイル共有） | 組み込み（Main/Branch/Forkモデル） |
| ローカルLLM対応 | サードパーティプラグイン経由 | ネイティブ対応（Ollama, LM Studio） |
| テキストフレームワーク | UGUI, NGUI, IMGUI, TextMeshPro, FairyGUI, Utage | Harmonyパッチ経由 |
| 品質管理 | 手動翻訳ファイル編集 | H/V/Aタグシステム + Webエディタ |
| Modローダー | BepInEx, MelonLoader, IPA, UnityInjector, ReiPatcher | BepInEx 5/6, MelonLoader |
| IL2CPP対応 | あり（BepInEx 6） | あり（BepInEx 6, MelonLoader） |

### XUnity.AutoTranslator

[[xunity-auto-translator]] を参照。

- 最も広く使われているUnity翻訳プラグイン
- 多数の組み込み翻訳エンドポイント（Google, DeepL, Bing, Papago等）
- スパム防止機構が充実（1秒待機、セッション上限、異常検知によるシャットダウン）
- テクスチャ翻訳にも対応
- LLM連携はサードパーティプラグイン（LlmTranslators, AutoLLMTranslator等）で実現

### UnityGameTranslator

[[unity-game-translator]] を参照。

- ローカルAI翻訳を第一級機能として設計（Ollama, LM Studioでオフライン翻訳可能）
- コミュニティ翻訳プラットフォームを内蔵
  - Main/Branch/Forkモデルでの協調翻訳
  - 3-wayマージによる翻訳統合
  - 品質タグ（H: Human, V: Validated, A: AI）によるスコアリング
- Capture Keys Onlyモードで100%人間翻訳ワークフローも可能
- セルフホスト対応（AGPL）

## 前提: Modローダー

Unity翻訳プラグインは単体では動作せず、Modローダーが必要:

- **[[bepinex|BepInEx]]**: 最も広く推奨される。Mono / IL2CPP両対応（6系）
- **MelonLoader**: 汎用Unityモッドローダー。Mono / IL2CPP対応
- **IPA / UnityInjector**: 一部の古いゲーム向け

ゲームがMono（`Assembly-CSharp.dll` が存在）かIL2CPP（`GameAssembly.dll` が存在）かでModローダーの選択が変わる。

## ローカルLLM翻訳

クラウドAPI依存を減らすため、ローカルLLMによるオフライン翻訳が注目されている:

- Ollama / LM Studio で OpenAI互換APIを提供
- 推奨モデル: `qwen3:8b`（多言語対応、6-8GB VRAM）
- メリット: コストゼロ、プライバシー保護、オフライン動作
- デメリット: ハードウェア要件（GPU/VRAM）、翻訳品質はモデルサイズに依存
