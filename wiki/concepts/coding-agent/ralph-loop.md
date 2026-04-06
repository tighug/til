---
title: Ralph Loop
type: concept
sources:
  - "raw/articles/Agentワークフローで人間がボトルネックにならないためのSkill設計.md"
related:
  - "[[coding-agent-autonomy]]"
  - "[[harness-engineering]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - coding-agent
  - autonomous-loop
---

## 概要

snarktank/ralphが発端のパターン。PRDのタスクリストが全部完了するまでAgentを繰り返し走らせる自律実行ループ。

## 仕組み

- 各イテレーションは新鮮なコンテキストで起動
- 状態はgit履歴とprogress.txtで引き継ぐ
- コンテキストウィンドウの制約を、タスク分割と状態永続化で回避
- **本質: Agentの判断ではなくテストで完了を判定する**（Matthew Berman）

## anti-human-bottleneckスキルとの補完関係

| レイヤー | 役割 | 解決する問題 |
| --- | --- | --- |
| Ralph loop（外側） | タスク完了まで繰り返し実行 | コンテキスト制約、タスク管理 |
| anti-human-bottleneck（内側） | 各実行内で人間を待たずに進む | 判断停止、確認待ち |

Ralph loopだけだと各イテレーション内でAgentが確認待ちで止まる可能性があり、スキルだけだとコンテキスト制約でいずれ限界が来る。二重構造で完全自律に近づく。

## 引用

> "Ralph loops remove human bottlenecks by allowing AI to work autonomously on long-running tasks." — Addy Osmani

> "Everything is a ralph loop." — Geoffrey Huntley
