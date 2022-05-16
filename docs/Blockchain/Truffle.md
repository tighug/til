# Truffle

Truffle とは、**スマートコントラクトの開発に必要な、コンパイル・リンク・デプロイ・バイナリ管理の機能を持つ統合開発管理フレームワーク**です。分散型アプリケーション（Dapp）の作成が可能です。

- [Truffle](https://www.trufflesuite.com/docs/truffle/overview)

## Installation

```bash
yarn global add truffle
```

## Usage

新規プロジェクトの作成

```bash
truffle init
```

### Command

- `truffle compile` コンパイル。`build`ディレクトリが作られる。
  - `--all` 変更ファイルだけでなく全てをコンパイル
- `truffle migrate` マイグレーション
  - `--reset` 全てを最初から実行する
- `truffle develop` コンソール起動

## Directory

- `contracts/` スマートコントラクト置き場
- `migrations/` デプロイファイル置き場
- `test/` テストファイル置き場
- `truffle.js` Truffle の設定ファイル
- `truffle-config.js` Truffle の設定ファイルの雛形

## Migration

ファイル名の先頭には番号を付ける（e.g. 4_example_migration）。番号順に Migrate が実行される。

## Config- `truffle.js`
