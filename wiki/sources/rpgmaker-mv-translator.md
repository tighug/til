---
title: rpgmaker-mv-translator
type: source-summary
sources:
  - "raw/articles/davide97lrpgmaker-mv-translator Automatic game data translator for RPGMaker-MV.md"
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

RPG Maker MVゲームのデータファイルをGoogle Translate APIを使って自動翻訳するPythonツール。davide97l氏が開発。

## 要点

- 対象: RPG Maker MV の `data/` フォルダ内JSONファイル
- 翻訳対象ファイル
  - ダイアログ系: `CommonEvents.json`、`MapXXX.json`（大量のゲーム内セリフ）
  - オブジェクト系: `Armors.json`、`Weapons.json`、`Items.json`、`Skills.json`、`Enemies.json`、`MapInfos.json`、`Classes.json`、`States.json`、`Actors.json`
- 翻訳エンジン: Google Translate API（インターネット接続必須）
- **print_neatly機能**: 翻訳後テキストをダイアログウィンドウ幅に自動整形。行単位ではなくダイアログウィンドウ単位で翻訳するため文脈精度も向上
- 2つのスクリプト
  - `dialogs_translator.py`: ダイアログファイル（CommonEvents, Map系）用
  - `objects_translator.py`: オブジェクトファイル（装備、アイテム等）用
- 引数: `--source_lang`（原文言語）、`--dest_lang`（翻訳先言語）、`--print_neatly`、`--max_len`（ダイアログ幅）、`--verbose`
- 出力は `dialogs_xx` / `objects_xx` フォルダに保存、ゲームの `data/` に上書きコピーして適用
