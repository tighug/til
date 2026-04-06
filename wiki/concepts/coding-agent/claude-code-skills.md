---
title: Claude Code Skills
type: concept
sources:
  - "raw/articles/Agentワークフローで人間がボトルネックにならないためのSkill設計.md"
  - "raw/articles/Claude Code 中級者ガイド.md"
related:
  - "[[coding-agent-autonomy]]"
  - "[[agents-md-design]]"
  - "[[harness-engineering]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - claude-code
  - skills
---

## 概要

SKILL.mdのdescriptionに記述されたトリガー条件に合致すると、Agentが自律的にロードする仕組み。特定タスクの実行スキルだけでなく、Agentの行動パターンを変える「メタスキル」としても設計できる。

## メタスキルとしての設計（anti-human-bottleneck）

descriptionに「Agentの内部状態」をトリガーとして記述:

```yaml
description: "Load this skill BEFORE asking the user any question,
  requesting confirmation, seeking approval..."
```

- 「BEFORE asking」がポイント: 聞く前にロードされ、「聞くな、自分でやれ」が注入される
- Agentの発話ではなく内部状態がトリガー

## 設計ガイドライン

- **descriptionがすべて**: 発火条件はここで決まる
- **1ファイルで完結**: 行動指針スキルは分割しない。部分ロードで一貫性が崩れる
- **commands vs skills**: プロジェクト固有→`.claude/commands/`、汎用原則→`~/.claude/skills/`

## Skills vs AGENTS.md

Vercelの実験ではAGENTS.mdがSkillsのeval結果を上回った。ただしSkillsはオンデマンドロードのためコンテキスト効率で優位。用途によって使い分ける。
