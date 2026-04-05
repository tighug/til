---
title: シンプリシティの価値
type: concept
sources:
  - "raw/articles/Nobody Gets Promoted for Simplicity.md"
related: []
created: 2026-04-05
updated: 2026-04-05
public: true
tags:
  - engineering-culture
  - simplicity
  - career
---

## 核心

> "Simplicity is a great virtue, but it requires hard work to achieve and education to appreciate." — Edsger Dijkstra

組織のインセンティブ構造が複雑性を報酬し、シンプリシティを無視する。面接・設計レビュー・昇進のすべてで。

## 正当な複雑性 vs 不当な複雑性

- **正当**: 「DBの限界に達したのでシャーディングが必要」
- **不当（unearned complexity）**: 「3年後にDB限界に達するかもしれないから今シャーディングする」

> "Anyone can add complexity. It takes experience and confidence to leave it out."

## シンプリシティを可視化する方法

「feature Xを実装した」（3語）→「event-driven architectureを含む3つのアプローチを評価し、直接的な実装が要件を満たすと判断し、2日で出荷、6ヶ月間ゼロインシデント」

**避けた複雑性を決定として文書化する。** 構築しなかったものについて説得力のある物語は書けないが、構築しないことを選んだ判断は書ける。

## リーダーの役割

- 質問を変える: 「スケールは？」→「最もシンプルに出荷できるバージョンは？何がきっかけでより複雑にすべき？」
- シンプリシティをデフォルトにし、複雑性に立証責任を負わせる
- コードを削除した人、「まだ不要」と言った人を公に称賛する
