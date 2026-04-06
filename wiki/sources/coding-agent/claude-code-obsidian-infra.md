---
title: "Claude Code × Obsidian によってインフラ管理が拡がる価値を考える"
type: source-summary
sources:
  - "raw/articles/Claude Code × Obsidian によってインフラ管理が拡がる価値を考える.md"
related:
  - "[[mcp]]"
  - "[[coding-agent-autonomy]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - claude-code
  - obsidian
  - infrastructure
  - mcp
  - ssh-monitoring
---

## 要約

Claude Code + MCP + Obsidianの組み合わせで、SSH操作のリアルタイム監視を中核に、手順書自動生成・AWSリソース確認・インフラ俯瞰図作成まで広がったインフラ管理の実践記録。

## 監視プロトコルの進化

### v1.0: ポーリング方式の限界
- SSHセッションの入出力を`.live`ファイルに書き込み、MCP経由で参照
- 問題: ポーリング間隔によるタイムディレイ、無駄なAPI呼び出し

### v2.0: インフラエンジニアの「癖」に着目
- 空Enter（プロンプト再表示）をシグナルとして活用
- `wait_for_command` MCPツールを追加: `completed`（コマンド完了）と`prompt_only`（空Enter）を区別
- ポーリング不要でリアルタイムに反応

## 監視からの広がり

1. **SSH作業の円滑化**: エラー即時検知→手順書修正→他サーバーでの予防
2. **手順書自動生成**: セッションログから成功コマンドのみ抽出、切り戻し手順も自動生成
3. **インフラ俯瞰図**: AWS CLIで実態確認→Obsidian Canvas（JSON形式）を直接編集

## Obsidian選定理由

- ローカルMarkdownファイル: MCPから直接読み書き可能
- Canvas（JSON形式）: AIエージェントが直接編集可能
- テキストベースで軽量

## 工夫

- 監視ループの継続: ユーザー入力を待たずに即座に次の`wait_for_command`を呼ぶ
- 文脈喪失対策: `.live`ファイル検知→`current_task`読み込み→手順書検索→ログからステップ判断
- 手順書の書き方: 1ステップ1コマンド、期待値を明記
