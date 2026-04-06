---
title: XUnity.AutoTranslator
type: source-summary
sources:
  - "raw/articles/bbepisXUnity.AutoTranslator.md"
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

Unity製ゲームを自動翻訳するための高機能プラグイン。bbepis氏が開発。リアルタイムでゲーム内テキストをインターセプトし、外部翻訳サービスに送信して翻訳結果を表示する。

## 要点

- 対応プラグインフレームワーク: BepInEx（推奨）、MelonLoader、IPA、UnityInjector、ReiPatcher（スタンドアロン）
- IL2CPPにも対応（BepInEx 6 / MelonLoader経由）
- 対応テキストフレームワーク: UGUI、NGUI、IMGUI、TextMeshPro、TextMesh、FairyGUI、Utage
- 組み込み翻訳エンドポイント
  - Google Translate（複数バリアント）、DeepL、Bing、Papago、Baidu、Yandex、Watson、LingoCloud
  - 認証不要のものと、APIキーが必要な正規版の両方を用意
- サードパーティ翻訳エンドポイント
  - SugoiOfflineTranslatorEndpoint: ローカルのSugoi Translator利用
  - LlmTranslators: OpenAI / Ollama対応
  - AutoLLMTranslator: 汎用LLMエンドポイント
  - AutoPollinationTranslator: Pollinations.ai API利用
- スパム防止機構: テキスト変化の1秒待機、セッション毎8000リクエスト上限、同時実行1リクエスト、フレーム毎翻訳検知でシャットダウン等
- 翻訳結果はディスクにキャッシュされ、同じ翻訳の再リクエストを防止
- 手動翻訳ファイルの管理機能あり（テキストファイルベース）
- テクスチャ翻訳にも対応
- CustomTranslateエンドポイントで任意のHTTP翻訳サービスに接続可能
