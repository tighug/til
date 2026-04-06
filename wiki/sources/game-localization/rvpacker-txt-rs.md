---
title: rvpacker-txt-rs
type: source-summary
sources:
  - "raw/articles/RPG-Maker-Translation-Toolsrvpacker-txt-rs A CLI tool to parse RPG Maker games' text to .txt and back.md"
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

RPG Makerゲームのテキストを `.txt` ファイルに変換し、翻訳後に元形式に書き戻すRust製CLIツール。RPG-Maker-Translation-Toolsプロジェクトの一部。

## 要点

- 元の `rvpacker`（Ruby版、削除済み）のRust書き直し版
- RPG Makerのゲームファイルからテキストを `.txt` に抽出（read）、翻訳済み `.txt` から書き戻し（write）
- テキストフォーマット: 各行のオリジナルテキストの後に `<#>` デリミタを挿入、その後に翻訳テキストを記述
  - 改行は `\#` に置換
- 使用例
  - `rvpacker-txt-rs read -i "C:/Game"` → `translation` フォルダにテキスト抽出
  - `rvpacker-txt-rs write -i "C:/Game"` → `output` フォルダにRPG Makerファイルとして書き戻し
- 関連ツール（同プロジェクト）
  - rpgmtranslate-qt: GUIエディタ
  - rpgm-asset-decrypter-rs: アセット復号化CLI
  - rpgm-archive-decrypter: アーカイブ復号化CLI
  - rpgmdec: 復号化GUI
- ライセンス: WTFPL
