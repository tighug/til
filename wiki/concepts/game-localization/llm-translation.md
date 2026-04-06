---
title: LLM翻訳
type: concept
sources:
  - "raw/articles/10 Translation Prompts for ChatGPT and Claude That Actually Work.md"
  - "raw/articles/35 ChatGPT Prompts for High-Quality Translation 2026.md"
  - "raw/articles/ChatGPT & LLMs – Separating Fact from Fiction for Localization.md"
  - "raw/articles/List of the Best Large Language Models for Translation.md"
  - "raw/articles/LLM Localization Guide  How AI Is Transforming Translation.md"
  - "raw/articles/The 3 Best LLMs for Translation in 2025 ChatGPT vs. Claude vs. Gemini - Localize Articles.md"
  - "raw/articles/Use AI and large language models for translation - Globalization.md"
  - "raw/articles/What's the best LLM for translation in 2026.md"
related:
  - "[[translation-prompt-engineering]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - llm
  - translation
---

## LLM翻訳とは

大規模言語モデル（LLM）を翻訳タスクに活用するアプローチ。LLMは翻訳専用に設計されていないが、大量の多言語データで訓練されているため、文脈・トーン・文化的ニュアンスを捉えた翻訳が可能。従来のニューラル機械翻訳（NMT）と比較して、より自然で人間に近い翻訳出力を生成する。

## NMT vs LLM

従来のNMT（DeepL、Google翻訳等）とLLMには明確な違いがある。

- **NMT** — セグメント単位処理、正確性に強い、ドメイン特化のファインチューニングが容易・安価、用語集統合が容易
- **LLM** — ドキュメント全体を処理可能、自然さに強い、文脈理解が深い、多用途（翻訳以外にもレビュー・生成が可能）

両者は排他的ではなく、相乗効果を活かしたハイブリッドアプローチが最適解。WMT25でもトップシステムはLLMベースまたはハイブリッドアプローチに移行している。

## 主要モデルの翻訳特性

### Claude（Anthropic）
- スタイル的流暢さ、トーン保持、イディオム・文化的ニュアンスの処理に最も優秀
- マーケティングコピー、ブランドセンシティブなコンテンツに最適
- イディオムの直訳率8%（ChatGPTは34%）
- 大きなコンテキストウィンドウ（200K+トークン）で用語一貫性に強い

### ChatGPT / GPT（OpenAI）
- 技術文書、コードローカライゼーションに強い
- 変数・プレースホルダー・フォーマットの厳密な保持
- より多くの言語ペアをサポート（低リソース言語含む）
- GPT-5は400Kトークンウィンドウ、ハルシネーション率がGPT-4oより45%低減

### Gemini（Google）
- 最大100万トークンのコンテキストウィンドウ
- ネイティブマルチモーダル（テキスト+画像+動画+音声）
- 長文ドキュメントセット、リポジトリ、複数ファイルの一貫性維持に最適

### DeepSeek
- コスト効率に特化
- 大量・低リスクバルク翻訳、内部ドキュメント向け

### Meta NLLB-200
- 200言語対応の翻訳特化オープンソースモデル
- 低リソース言語の翻訳に唯一の選択肢となることも

### Qwen（Alibaba）
- 中国語-英語翻訳に最も強い
- 日本語、韓国語、ベトナム語等のアジア言語に優秀

## マルチモデル戦略

2026年のベストプラクティスは単一モデルの採用ではなく、タスクに応じたモデルの使い分け。

| コンテンツ種別 | 推奨モデルクラス |
|---|---|
| 法務・医療・クリエイティブ（高リスク） | フラッグシップ（GPT-5、Gemini Pro、Claude Opus） |
| Webサイト・UI・一般文書（汎用） | ミッドレンジ（GPT-5-mini、Gemini Flash、Claude Sonnet） |
| チャット・UGC・内部文書（大量・低リスク） | 軽量（GPT-5-nano、Gemini Flash-Lite、DeepSeek） |

## 品質評価と自動ルーティング

- Lokaliseのブラインド比較研究で、LLMが全言語ペアで従来MTを上回ることが確認
- **AIQEスコアリング** — MQM基準で0-100の品質スコアを自動付与し、80以上は自動承認、未満は人間レビュー
- **RAG（検索拡張生成）** — 翻訳メモリの承認済み翻訳を参照させることで一貫性を向上
- 「全文人間レビュー」から「例外のみ人間レビュー」へのワークフロー転換

## LLMの限界と注意点

- **ハルシネーション/ファブリケーション** — ソースに存在しない情報を生成するリスク（医療・法務では致命的）
- **低リソース言語** — 訓練データが少ない言語では品質が低下
- **言語変種** — ポルトガル語（PT vs BR）等の区別が苦手
- **認証翻訳** — LLMでは公式な証明書の発行は不可能
- **データプライバシー** — 機密文書のLLMへのアップロードにはリスクがある
- **モデル更新リスク** — 新バージョンで特定言語の品質が低下する可能性 → 定期スポットチェックが必要
- プロンプト設計で品質は大きく変わる → [[translation-prompt-engineering]] を参照
