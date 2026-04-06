---
title: "Claude Code 中級者ガイド"
type: source-summary
sources:
  - "raw/articles/Claude Code 中級者ガイド.md"
related:
  - "[[agents-md-design]]"
  - "[[claude-code-skills]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - claude-code
  - best-practices
---

## 要約

Gatsby氏によるClaude Codeの中級者向けベストプラクティス集。公式ドキュメントと散在する情報をまとめたもの。

## 主要Tips

### CLAUDE.mdでコンテキストを永続化
- セッションはステートレス。セッションを跨いで記憶させたい情報はCLAUDE.mdに記載
- 公式サンプルプロンプト（`what does this project do?`等）で効率的に充実させる

### ultrathink
- 思考深度を制御するキーワード: think → think hard → think harder → ultrathink
- ultrathinkが最も深い（上限31,999トークン）
- 公式ドキュメント未記載、cli.jsに直接記述

### Explore, Plan, Code, Commit
- いきなりタスク実装を投げず、コード理解→設計→実装→コミットの順で命令
- Planフェーズでultrathinkを使うと効果的

### TDD（テスト駆動開発）
- Anthropicお墨付きのワークフロー
- テスト実装→テストをパスする実装の順で命令することで、アウトプットのブレが格段に少なくなる

### その他
- `/clear`: 会話が長くなり文脈誤解が起きたらリセット
- `claude --resume`: 過去のセッション再開
- `preferredNotifChannel terminal_bell`: 処理完了通知
- `npx ccusage`: トークン使用量の可視化
