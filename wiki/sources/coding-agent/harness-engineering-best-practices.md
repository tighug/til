---
title: "Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス"
type: source-summary
sources:
  - "raw/articles/Codex ユーザーのための誰でもわかるHarness Engineeringベストプラクティス.md"
related:
  - "[[harness-engineering]]"
  - "[[claude-code-hooks]]"
  - "[[agents-md-design]]"
  - "[[e2e-testing-for-agents]]"
  - "[[deterministic-quality-tools]]"
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - harness-engineering
  - claude-code
  - codex
  - linting
  - testing
  - hooks
---

## 要約

逆瀬川氏による、2026年3月時点のハーネスエンジニアリングの包括的ベストプラクティス。7つのトピック、アンチパターン、最小実行可能ハーネス（MVH）までを網羅。

## 7つの原則

### 1. リポジトリ衛生
- 置くべきもの: 実行可能アーティファクト（コード、テスト、リンター設定等）とADR
- 置くべきでないもの: 説明文書、手書きAPI説明（腐敗してエージェントが誤認するリスク）
- テストはドキュメントより腐敗に強い

### 2. 決定論的ツールで品質強制
- 「LLMは従来のリンターと比較して高価で遅い」（HumanLayer）
- Hooksの4パターン: Safety Gates / Quality Loops / Completion Gates / Observability
- PostToolUse Hookで`additionalContext`としてフィードバック注入→自己修正ループ
- 推奨ツール: Oxlint+Biome（TS）、Ruff（Python）、golangci-lint（Go）
- リンター設定保護: エージェントのルール改竄を防ぐPreToolUseフック

### 3. AGENTS.md/CLAUDE.mdをポインタとして設計
- 50行以下を目指す。150指示でprimacy biasが顕著に
- 書くべき: ルーティング指示、禁止事項、ビルド/テストコマンド
- 書くべきでない: システム現状説明、冗長なスタイルガイド

### 4. 計画と実行を分離
- 計画→承認→実行のフロー。無駄な努力を防ぎアーキテクチャ制御を維持
- タスクを小さく分割し、一度に一つだけ取り組ませる

### 5. E2Eテスト戦略
- エージェントに「目」を与える。Playwright CLI/agent-browser推奨
- アクセシビリティツリーがユニバーサルインターフェース
- Web/モバイル/CLI/API/デスクトップ/インフラ/AI-MLまで網羅

### 6. セッション間の状態管理
- 起動ルーチン標準化、Gitをセッション間ブリッジとして使用
- 進捗記録にJSON（Markdownより編集ミスが少ない）

### 7. プラットフォーム固有戦略（Codex vs Claude Code）
- 同じモデルでもハーネスを変えるとSWE-benchスコアが22pt変動（Morph分析）
- Claude Code: 作業場型、Hooksが全ツール対応で安定版
- Codex: 密室型、非同期サンドボックスでの並列実行が強み
- ハイブリッド推奨: Claude Codeで計画→Codexで並列実行→Claude Codeでレビュー

## アンチパターン
1. プロンプトだけに頼る（仕組みで解決せよ）
2. リポジトリに説明文書を蓄積（テストとADRに置換）
3. AGENTS.mdを巨大にする（50行以下を目指す）
4. エージェント専用インフラを構築（優れた開発者インフラを構築せよ — Stripe）
5. ハーネスなしでスケール（複利的な認知的負債が生まれる）

## MVH（最小実行可能ハーネス）ロードマップ
- Week 1: CLAUDE.md作成、プリコミットフック、PostToolUse Hook
- Week 2-4: テスト/ルール追加、E2Eツール導入、Stop Hook
- Month 2-3: カスタムリンター、ADR連携、Safety Gates
- Month 3+: 高度なフィードバックループ、効果測定
