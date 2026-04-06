---
title: Claude Code Hooks
type: concept
sources:
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
related:
  - "[[harness-engineering]]"
  - "[[deterministic-quality-tools]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - claude-code
  - hooks
  - quality
---

## 概要

Agentのライフサイクルの特定ポイントで自動実行されるシェルコマンド。`.claude/settings.json`に記述。Gitフックがgit操作のbefore/afterで走るように、Claude Code Hooksはあらゆるアクションのbefore/afterで走る。

## 4つのパターン

| パターン | イベント | 役割 |
| --- | --- | --- |
| Safety Gates | PreToolUse | 破壊的コマンドのブロック、機密ファイル編集禁止 |
| Quality Loops | PostToolUse | ファイル編集後のリンター自動実行→自己修正ループ |
| Completion Gates | Stop | テスト通過まで完了させない |
| Observability | 全イベント | 監視パイプラインへのフィード |

## Quality Loopsの仕組み

1. エージェントがコードを書く（PostToolUseイベント発火）
2. Hookがリンター・型チェッカーを自動実行
3. `hookSpecificOutput.additionalContext`を含むJSONでフィードバック注入
4. エージェントが次のアクションで自己修正
5. ファイル書き込みのたびにこのループが繰り返される

**重要**: 通常のstdoutではなく、`additionalContext`を含むJSON形式で返す必要がある。

## CLAUDE.md指示との違い

- CLAUDE.mdに「リンターを実行せよ」→「ほぼ毎回」
- Hookでリンターを実行→「例外なく毎回」
- この差はプロダクションでは致命的

## Codex Hooksとの比較

- Claude Code: 全ツール（Write/Edit/MultiEdit/Bash等）対応、安定版
- Codex: Bashツールのみ対応、実験的（2026-03-26導入）
- Codexはファイル操作をBash経由で行うため実質カバレッジは確保可能
