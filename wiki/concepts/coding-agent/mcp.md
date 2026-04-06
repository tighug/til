---
title: Model Context Protocol (MCP)
type: concept
sources:
  - "raw/articles/Claude Code × Obsidian によってインフラ管理が拡がる価値を考える.md"
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
related:
  - "[[coding-agent-autonomy]]"
  - "[[e2e-testing-for-agents]]"
  - "[[harness-engineering]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - mcp
  - claude-code
  - tooling
---

## 概要

AIエージェントが外部ツール・サービスと標準化されたプロトコルで通信するための仕組み。エージェントの「手」を拡張する。

## 実用例

### SSH監視（Claude Code × Obsidian記事）
- `watch_sessions`: セッション開始を検知
- `wait_for_command`: コマンド完了/空Enterを検知して返す
- `read_live_session`: セッションログ全体を取得

### ブラウザ操作
- chrome MCP: スクリーンショット、コンソールエラー確認、ネットワーク監視、フォーム操作
- Playwright MCP: アクセシビリティツリーベースのUI操作（ただしトークン消費が大きい）

### E2Eテスト
- Playwright MCP: 26以上のツール定義、トークン消費約114Kと重い
- Playwright CLI: MCPの約4倍のトークン効率（約27K）
- agent-browser: 最もトークン効率が高い（MCPの5.7倍）

### モバイル
- XcodeBuildMCP: iOS開発向け59ツール
- mobile-mcp: プラットフォーム非依存

## MCP Tax

MCPツールの定義自体がコンテキストウィンドウを消費する問題。Claude CodeのMCP Tool Searchはツール記述のオンデマンドロードでコンテキスト消費を最大85%削減。
