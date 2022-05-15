# npm

npm（Node Packages Manager）は**世界最大のソフトウェアレジストリ**です。npm は 3 つのコンポーネントで構成されています。

- Website
- CLI
- Registry

## Installation

[Node.js](./Nodejs.md)のインストールを参照して下さい。

## Usage

よく使うコマンドだけを抜粋します。

- `npm init` : カレントディレクトリの管理を開始
- `npm ls` : インストールパッケージ一覧
  - `-g` : グローバルで実行
  - `--depth [number]` ： 表示する階層の深さを指定
- `npm i [package]` : パッケージをインストール
  - `-g` : グローバルで実行
  - `-S` : 同時に`dependencies`に記録
  - `-D` : 同時に`devDependencies`に記録
  - パッケージ無指定 : `package.json`に記述された全パッケージを対象
- `npm un [package]` : パッケージを削除
  - `-g` : グローバルで実行
  - `-S` : 同時に`dependencies`から削除
  - `-D` : 同時に`devDependencies`から削除
- `npm update [package]` : パッケージを更新
  - `-g` : グローバルで実行
  - パッケージ無指定 : `package.json`に記述された全パッケージを対象
- `npm run [script name]` : `package.json`の`script`に定義済みのコマンドを実行
  - スクリプト無指定 : 定義済みのコマンドの一覧を表示
- `npm run env` : 環境変数の表示

## Configuration

Ref : [npm-package.json](https://docs.npmjs.com/files/package.json)

`package.json`に記述します。

- `name` : パッケージ名
- `version` : バージョン（[SemVer](https://developerexperience.io/practices/semantic-versioning)に従う）
- `description` : 説明
- `keyword` : キーワード
- `homepage` : プロジェクトのホームページ
- `bug` : issue や buy の報告場所
- `license` : ライセンス
- `author` : 作者
- `files`
- `main` : エントリポイント
- `repository`
- `scripts`
- `dependencies`
- `devDepandencies`
- `engines`
- `private`

## References

- [npm](https://www.npmjs.com/)
- [npm と yarn のコマンド早見表](https://qiita.com/rubytomato@github/items/1696530bb9fd59aa28d8)
