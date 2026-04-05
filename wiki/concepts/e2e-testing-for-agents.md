---
title: エージェント向けE2Eテスト
type: concept
sources:
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
related:
  - "[[harness-engineering]]"
  - "[[mcp]]"
  - "[[deterministic-quality-tools]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - testing
  - e2e
  - coding-agent
---

## なぜ必要か

エージェントは自分が書いたコードを「見る」手段がなければ、コンパイルが通っただけで「完了」と宣言する。ブラウザ自動化等を組み合わせることで人間と同じ視点で検証できる。

## ユニバーサル原則

1. **構造化テキスト出力を優先**: JSON、アクセシビリティツリー、CLI標準出力
2. **検証を決定論的にする**: エージェント生成テストを決定論的に実行。エージェント自身をCIに入れない
3. **フィードバックループを閉じる**: build → run → verify → fix のサイクルを自律的に

## アプリケーション別ツール選定

| アプリタイプ | 推奨ツール |
| --- | --- |
| Web | Playwright CLI / agent-browser |
| モバイル（iOS） | XcodeBuildMCP + Xcode 26.3 |
| モバイル（クロス） | Detox + mobile-mcp |
| CLI | bats-core / pexpect |
| API | Hurl（プレーンテキスト、エージェント相性最高） |
| デスクトップ（Windows） | Terminator |
| インフラ | terraform test / Conftest + OPA |
| AI/ML | DeepEval / promptfoo / RAGAS |

## Webツール比較

| ツール | トークン消費 | 用途 |
| --- | --- | --- |
| Playwright MCP | ~114K | テストスイート生成（Planner/Generator/Healer） |
| Playwright CLI | ~27K（MCPの4倍効率） | E2Eテストの主力 |
| agent-browser | ~5.5K（MCPの5.7倍効率） | セルフテストループ、探索的テスト |

## アクセシビリティツリーがユニバーサルインターフェース

Web/モバイル/デスクトップすべてでアクセシビリティツリーを介してUI操作が可能。スクリーンショットは視覚的バグ検出に限定し、操作・アサーションにはアクセシビリティツリーを優先する。
