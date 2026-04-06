---
title: 翻訳向けLLMモデル比較ガイド
type: source-summary
sources:
  - "raw/articles/List of the Best Large Language Models for Translation.md"
related:
  - "[[llm-translation]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - llm
  - translation
---

## 概要

Crowdinによる翻訳向け主要LLMの包括的比較。GPT-5、Gemini 2.5、Claude 4、LLaMA 4、NLLB-200、Qwen、Lara Translateの各モデルファミリーのスペック・コスト・適用領域を整理。

## GPT-5ファミリー（OpenAI）

- コンテキストウィンドウ最大400Kトークン
- ハルシネーション率がGPT-4oより最大45%低減
- **GPT-5** — 法務・医療等の高リスクコンテンツ、複雑なエージェントワークフロー（$1.25/M入力、$10/M出力）
- **GPT-5-mini** — 汎用翻訳のワークホース、コスト効率的（$0.25/M入力、$2/M出力）
- **GPT-5-nano** — 高速・低コスト、リアルタイムチャットや初稿作成（$0.05/M入力、$0.40/M出力）

## Gemini 2.5ファミリー（Google）

- ネイティブマルチモーダル（テキスト+画像+動画+音声を同時処理）
- コンテキストウィンドウ最大100万トークン
- **Gemini 2.5 Pro** — 複雑な推論、長文コンテンツ（$1.25/M入力、$10/M出力）
- **Gemini 2.5 Flash** — 高速・コスト効率、汎用翻訳（$0.30/M入力、$2.50/M出力）
- **Gemini 2.5 Flash-Lite** — 最安、バルク翻訳（$0.075/M入力、$0.30/M出力）
- 40以上の言語をサポート

## Claude 4ファミリー（Anthropic）

- Constitutional AIフレームワークで安全・倫理的出力
- **Claude 4.1 Opus** — 高リスクコンテンツ、長文、複雑なワークフロー（$15/M入力、$75/M出力）
- **Claude 4 Sonnet** — 汎用翻訳、コスト効率的（$3/M入力、$15/M出力）
- 200Kトークンコンテキスト（1Mベータ）
- マーケティング翻案、トーン・ニュアンス保持に優秀

## Meta LLaMA 4ファミリー & NLLB-200

- **LLaMA 4 Maverick** — クリエイティブ・マルチモーダル対応、100万トークンウィンドウ（~$0.19-0.49/Mトークン）
- **LLaMA 4 Scout** — 1000万トークンウィンドウ（業界最大）、長文一貫性に最適
- **NLLB-200** — 200言語対応の翻訳特化モデル、オープンソースで低コスト、低リソース言語に強い

## Alibaba Qwen

- **Qwen-MT** — 翻訳特化モデル、中日英等のアジア言語に強い、92言語対応
- **Qwen-Plus** — 汎用、100言語以上、バランス型（$0.40/M入力、$1.20/M出力）
- **Qwen-Turbo/Flash** — 高速・低コスト（$0.05-0.16/M入力）

## Lara Translate（Translated社）

- 2500万件の人間翻訳データで訓練された翻訳特化AI
- 200以上の言語、50+ファイル形式対応
- 翻訳スタイル選択可能：Faithful / Fluid / Creative
- 99%の翻訳をP99レイテンシ1.2秒で完了
- 無料プラン有り、Pro €9/月、Team €29/ユーザー/月

## 共通戦略：マルチモデルアプローチ

- 単一モデルではなくタスクに応じた使い分けが最適
- **クリティカルコンテンツ** → フラッグシップモデル（GPT-5、Gemini Pro、Opus）
- **大量汎用コンテンツ** → ミッドレンジ（GPT-5-mini、Flash、Sonnet）
- **低リスク・大量コンテンツ** → 軽量モデル（nano、Flash-Lite、Turbo）
