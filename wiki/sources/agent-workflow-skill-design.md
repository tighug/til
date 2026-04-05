---
title: "Agentワークフローで人間がボトルネックにならないためのSkill設計"
type: source-summary
sources:
  - "raw/articles/Agentワークフローで人間がボトルネックにならないためのSkill設計.md"
related:
  - "[[claude-code-skills]]"
  - "[[ralph-loop]]"
  - "[[coding-agent-autonomy]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - claude-code
  - skills
  - agent-autonomy
---

## 要約

逆瀬川氏による、Claude Code Skillを使ってAgentワークフローの人間ボトルネックを解消する設計パターンの解説。

## 核心

- Agentは「pushしていいですか？」等の確認で頻繁に停止し、1回あたり2-5分のコンテキストスイッチが発生する
- Skillのdescriptionに「人間に聞こうとした瞬間」をトリガーとして記述すると、聞く前にスキルがロードされて自己解決に誘導できる
- スキル本文の核心: 「pushしていいか聞くな。pushしろ」「正しいか聞くな。自分で検証しろ」
- 人間を呼んでいいのは物理的にAgentにできないこと（SMS認証、CAPTCHA等）だけ

## 自己検証の手段

- chrome MCP: ブラウザ操作・スクリーンショット・コンソールエラー確認
- Playwright / curl: chrome MCPがない環境でのフォールバック
- テスト実行・git diff: コード検証

## Ralph loopとの補完関係

| レイヤー | 役割 |
| --- | --- |
| Ralph loop（外側） | タスク完了まで繰り返し実行。コンテキスト制約を克服 |
| anti-human-bottleneck（内側） | 各実行内で人間を待たずに進む |

## 設計パターンとしてのポイント

- descriptionがすべて: Agentの内部状態（「質問しようかな」）をトリガーにする
- 1ファイルで完結: 行動指針スキルは分割しない。部分ロードで一貫性が崩れる
- commands vs skills: プロジェクト固有の検証手順は`.claude/commands/`、汎用的行動原則は`~/.claude/skills/`
