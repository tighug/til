---
title: ハーネスエンジニアリング
type: concept
sources:
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
related:
  - "[[claude-code-hooks]]"
  - "[[deterministic-quality-tools]]"
  - "[[agents-md-design]]"
  - "[[e2e-testing-for-agents]]"
  - "[[coding-agent-autonomy]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - harness-engineering
  - coding-agent
---

## 定義

Mitchell Hashimotoによる元の定義: AGENTS.mdの継続的改善と、Agentが自己検証するためのツール群。

現在の広義: Coding Agentを人間の介入なしに自律稼働させ、出力を安定させるための環境設計全般。Coding Agentの「補助輪」。

**核心: モデルではなくシステムが重要。** 同じモデルでもハーネスを変えるとSWE-benchスコアが22pt変動するが、モデル交換では1ptしか変わらない（Morph分析）。

## 原則

1. **プロンプトではなく仕組みで品質を強制する** — リンター、Hooks、テスト、ADRの組み合わせが複利的に効く
2. **フィードバックは速いほど良い** — PostToolUse Hook(ms) > プリコミット(s) > CI(min) > 人間レビュー(h)
3. **投資は複利で効く** — リンタールール1つ追加すれば以降すべてのセッションでそのミスが防がれる

## この分野の寿命

LLMの能力向上やCoding Agent自体への還元で、数ヶ月〜1年で重要でない分野になる可能性がある。しかし2026年3月時点では重要。

## MVH（最小実行可能ハーネス）

Week 1から始められる段階的アプローチ:
1. CLAUDE.md（50行以下）+ プリコミットフック + PostToolUse Hook
2. テスト/ルール追加、E2Eツール導入
3. カスタムリンター、ADR連携
4. 高度なフィードバックループ、効果測定
