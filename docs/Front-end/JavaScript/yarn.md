# Yarn

Yarn は**Node.js のパッケージマネージャー**です。

## Installation

=== "macOS"

    ```bash
    brew install yarn
    ```

## CLI

| command                             | description                                          |
| ----------------------------------- | ---------------------------------------------------- |
| `yarn help`                         | コマンドリストを表示                                 |
| `yarn init`                         | 新しいプロジェクトを開始                             |
| `yarn` (`yarn install`)             | `package.json`に記録されたパッケージをインストール   |
| `yarn add [package]@[version]`      | `dependencies`にパッケージを追加                     |
| `yarn add -D [package]@[version]`   | `devDependencies`にパッケージを追加                  |
| `yarn upgrade --latest`             | パッケージすべてを最新版に更新                       |
| `yarn upgrade [package] --latest`   | 指定したパッケージを最新版に更新                     |
| `yarn upgrade-interactive --latest` | パッケージをインタラクティブに最新版に更新           |
| `yarn list --depth=0`               | インストールしたパッケージの一覧を表示               |
| `yarn remove [package]`             | パッケージの削除                                     |
| `yarn run`                          | スクリプトの一覧を表示                               |
| `yarn run [script]`                 | `package.json`の`script`に定義されたスクリプトを実行 |
| `yarn run env`                      | スクリプトで使用可能な環境変数の表示                 |
| `yarn audit`                        | パッケージの脆弱性監査を実行                         |
| `yarn autoclean`                    | パッケージから不要なファイルを削除                   |
| `yarn bin`                          | bin フォルダーの場所を表示                           |
| `yarn create`                       | `create-*`系パッケージから新規プロジェクトを作成     |
| `yarn import`                       | `package-lock.json`から`yarn.lock`を生成             |
| `yarn info [package] [field]`       | パッケージの情報を表示                               |
| `yarn login`                        | npm レジストリのユーザー名と電子メールを保存         |
| `yarn logout`                       | npm レジストリのユーザー名と電子メールを削除         |
| `yarn outdated`                     | 古いパッケージの依存関係を表示                       |
| `yarn publish`                      | パッケージを rpm レジストリに公開                    |
| `yarn publish --tag <tag>`          | パッケージをタグ付きで rpm レジストリに公開          |
| `yarn version`                      | パッケージのバージョンを更新                         |

## References

-   [yarn](https://classic.yarnpkg.com/en/)
