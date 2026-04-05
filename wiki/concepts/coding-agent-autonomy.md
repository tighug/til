---
title: Coding Agentの自律化
type: concept
sources:
  - "raw/articles/Agentワークフローで人間がボトルネックにならないためのSkill設計.md"
  - "raw/articles/Claude Code × Obsidian によってインフラ管理が拡がる価値を考える.md"
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
related:
  - "[[ralph-loop]]"
  - "[[claude-code-skills]]"
  - "[[harness-engineering]]"
  - "[[mcp]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - coding-agent
  - autonomy
---

## 問題: 人間がボトルネック

Agentは秒単位で動けるのに、人間の確認待ちで数分止まる。1回のやりとりで2-5分のコンテキストスイッチ。10回聞かれたら30分以上が消える。

問題の本質: Agentが「人間に聞くべきかどうか」の判断を保守的にしすぎている。

## 自律化のアプローチ

### 1. 行動原則の注入（Skill設計）
- 「聞こうとした瞬間」をトリガーにSkillをロードし自己解決に誘導
- 人間を呼んでいいのは物理的にAgentにできないことだけ

### 2. 自己検証手段の提供（MCP + E2E）
- chrome MCP / Playwright: ブラウザ操作・スクリーンショット
- SSH監視プロトコル: リアルタイムコマンド結果の把握
- テスト実行: 機能検証の自動化

### 3. 構造的強制（Hooks + リンター）
- PostToolUse Hookでファイル編集のたびに品質チェック
- Stop Hookでテスト通過を完了条件にする
- プリコミットフックでゲートを設ける

### 4. 自律実行ループ（Ralph loop）
- タスクリスト完了までAgentを繰り返し走らせる
- テストで完了を判定、人間のレビューを待たない

## 人間が介入すべき場面

- 物理的にAgentにできないこと: SMS認証、CAPTCHA、生体認証
- 問題の特定と解決（日常的な確認や承認ではなく）
- 人間を「高レイテンシ・低帯域のツール」として扱う: 認知負荷を最小化、選択肢は2-4個、推奨をマーク
