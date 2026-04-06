---
title: AGENTS.md / CLAUDE.md 設計
type: concept
sources:
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
  - "raw/articles/Claude Code 中級者ガイド.md"
related:
  - "[[harness-engineering]]"
  - "[[claude-code-skills]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - agents-md
  - claude-code
  - codex
---

## 役割

Agentがセッション起動時に読み込むメモリ。セッションはステートレスなので、常に参照させたい情報をここに記載する。

## 設計原則: ポインタとして設計する

### 書くべきもの
- ルーティング指示: `npm test`で走る、ADRは`/docs/adr/`にある
- 禁止事項の一覧: ADRまたはリンタールールへの参照つき
- ビルド・テスト・デプロイの最低限のコマンド

### 書くべきでないもの
- システムの現状説明（コードとテストが真実のソース）
- 技術スタックの解説（package.json/go.modを読める）
- 冗長なコーディングスタイルガイド（リンターに委ねる）

## サイズの目安

- **理想: 50行以下**
- Anthropic公式: 200行以下（上限であって目標ではない）
- IFScale研究: 150〜200指示でprimacy biasが顕著になり性能劣化
- Claude Codeのシステムプロンプト自体が約50指示→ユーザーのCLAUDE.mdが100行で計150指示

## ポインタ型設計の利点

- ポインタが指すファイルパスが消えれば404エラー→腐敗が機械的に検出可能
- 記述的ドキュメントの腐敗は沈黙のうちに進行するが、壊れたポインタは騒がしく失敗する

## AGENTS.md vs CLAUDE.md

- AGENTS.md: AAIF標準。Codex、Cursor、Devin、Gemini CLI、GitHub Copilot等が読み込む共通フォーマット
- CLAUDE.md: Claude Code固有。AGENTS.mdはネイティブには読まれない
- 両方管理する場合: CLAUDE.md内で`@AGENTS.md`とインクルード
