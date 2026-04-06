---
title: Translator++
type: source-summary
sources:
  - "raw/articles/Translator++ Ver. 6.12.26 - A blazingly fast Ruby based RPG Maker parser!.md"
related:
  - "[[rpgmaker-translation]]"
  - "[[game-translation-tools]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - game-translation-tools
---

## 概要

Dreamsavior氏が開発するRPG Maker翻訳ツール。Ver. 6.12.26でRubyベースRPG Maker（XP, VX, VX Ace）向けの高速パーサー（Ver. 3）を搭載。

## 要点

- Ruby系RPG Maker（XP, VX, VX Ace）のデータはRubyのMarshal形式で保存されている
- パーサーの歴史（課題と進化）
  - **Legacy Parser**: RPGMaker Transベース。テキストの読み込み漏れやクラッシュの問題あり
  - **Parser Ver. 2**: RVPackerベースでYAML経由。全テキスト読み込み可能になったが、Node.jsのYAMLライブラリが遅く大規模ゲームで数時間かかる
  - Legacy Parserの改良版: RPGMaker Transをforkして修正。RubyとPython間のTCP通信がボトルネック
  - Parser Ver. 2改良版: CommonEventsをイベント単位で分割しマルチスレッド処理。1時間→10分に短縮
  - **Parser Ver. 3（最新）**: TypeScriptによるRuby Marshal形式の直接読み取り。YAML/TCP通信を排除し、従来比**約200倍の高速化**
- Ver. 3により Legacy Parser と Ver. 2 の両方を完全に置き換えることが目標
- Ver. 7の開発が進行中
