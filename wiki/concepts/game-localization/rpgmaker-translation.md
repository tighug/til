---
title: RPG Maker向け翻訳ツールチェーン
type: concept
sources:
  - "raw/articles/davide97lrpgmaker-mv-translator Automatic game data translator for RPGMaker-MV.md"
  - "raw/articles/RPG-Maker-Translation-Toolsrvpacker-txt-rs A CLI tool to parse RPG Maker games' text to .txt and back.md"
  - "raw/articles/Translator++ Ver. 6.12.26 - A blazingly fast Ruby based RPG Maker parser!.md"
related:
  - "[[game-translation-tools]]"
  - "[[unity-auto-translator]]"
  - "[[game-localization]]"
  - "[[ai-game-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - game-translation-tools
---

## 概要

RPG Makerはバージョンごとにデータ保存形式が異なるため、翻訳ツールチェーンもそれぞれに対応した形で発展してきた。主要な課題はデータ形式の解析（パース）と、大量テキストの効率的な翻訳処理である。

## RPG Makerのデータ形式

| RPG Makerバージョン | データ形式 | 備考 |
|---|---|---|
| XP / VX / VX Ace | Ruby Marshal形式 | バイナリ。直接のパースが困難 |
| MV / MZ | JSON形式 | テキストベースで扱いやすい |

## 主要ツール

### Translator++

[[translator-plus-plus]] を参照。

- Dreamsavior氏開発の統合翻訳環境
- Ruby系RPG Maker（XP, VX, VX Ace）とMV/MZの両方に対応
- パーサーの進化:
  - Legacy Parser（RPGMaker Transベース）→ Parser Ver. 2（YAML経由）→ **Parser Ver. 3（TypeScriptによるMarshal直接読み取り、約200倍高速化）**
- Ver. 7が開発中

### rvpacker-txt-rs

[[rvpacker-txt-rs]] を参照。

- RPG-Maker-Translation-Toolsプロジェクトの一部
- Rust製CLI。ゲームファイルのテキストを `.txt` に抽出し、翻訳後に書き戻す
- `<#>` デリミタで原文と訳文を区切るフォーマット
- GUI版（rpgmtranslate-qt）やアセット/アーカイブ復号化ツールも提供

### rpgmaker-mv-translator

[[rpgmaker-mv-translator]] を参照。

- davide97l氏開発のPythonスクリプト
- RPG Maker MV専用。`data/` フォルダ内のJSONファイルを自動翻訳
- Google Translate APIを利用
- print_neatly機能: ダイアログウィンドウ幅に合わせてテキスト整形。文脈を保った翻訳が可能
- ダイアログ系（CommonEvents, Map）とオブジェクト系（装備, アイテム等）で別スクリプト

## 翻訳ワークフロー

典型的なRPG Maker翻訳の流れ:

1. **テキスト抽出**: rvpacker-txt-rs / Translator++ でゲームファイルからテキストを抽出
2. **翻訳**: AI翻訳（Google Translate, DeepL等）で一次翻訳を生成
3. **レビュー・編集**: 人手で翻訳品質を確認・修正（固有名詞、文脈の調整）
4. **書き戻し**: 翻訳済みテキストをゲームファイルに再統合
5. **テストプレイ**: ゲーム内で表示確認（文字切れ、文脈ミス等のチェック）

## 課題

- Ruby Marshal形式のパース性能（Translator++ Ver. 3で大幅改善）
- ダイアログウィンドウへのテキスト収まり（rpgmaker-mv-translatorのprint_neatly等で対応）
- RPG Makerのイベントコマンド内に埋め込まれた制御文字やスクリプトの誤翻訳回避
- 大規模ゲームでの翻訳量（数千のイベント、マップファイル）への対応
