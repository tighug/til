---
title: 決定論的品質ツール
type: concept
sources:
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
related:
  - "[[harness-engineering]]"
  - "[[claude-code-hooks]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - linting
  - quality
  - tooling
---

## 原則

> "LLMは従来のリンターやフォーマッターと比較して高価で遅い。決定論的ツールが使える場面では常にそちらを使うべきだ。" — HumanLayer

リンター・フォーマッター・型チェッカーは腐敗しない。設定が変わればCIが壊れて即座に検出される。

## 推奨ツールスタック（2026年3月時点）

### TypeScript/JavaScript
- PostToolUse: Oxlint（リント、ESLintの50-100倍高速）+ Biome（フォーマット）
- プリコミット: Oxlint + tsc --noEmit
- CI: ESLint（カスタムアーキテクチャルール）+ テストスイート

### Python
- PostToolUse: Ruff check --fix → Ruff format
- プリコミット: Ruff + mypy
- CI: Ruff + mypy + pytest

### Go
- PostToolUse: gofumpt + golangci-lint（高速サブセット）
- プリコミット: golangci-lint --fix
- CI: golangci-lint（フル）+ go test

### Rust
- PostToolUse: rustfmt
- プリコミット: cargo clippy（pedantic, deny allow_attributes）

## エラーメッセージを修正指示にする

OpenAIチームの手法: カスタムリンターのエラーメッセージに「何が間違っているか」「なぜこのルールがあるか（ADR参照）」「具体的な修正手順」を含める。エージェントはリンターエラーを無視できない（CIが通らない）が、ドキュメントは無視できる。

## AI生成コード固有のアンチパターン

1. TypeScript any乱用（型推論失敗→anyに逃げる）
2. コード重複（検索せず新規生成）
3. ゴーストファイル（修正ではなく類似ファイル作成）
4. コメント洪水（90-100%で観察）
5. セキュリティ脆弱性（36-40%に含まれる）

## リンター設定保護

エージェントがリンターエラーに対してコード修正ではなく設定変更を行う行為をPreToolUseフックで防止する。
