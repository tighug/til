# Nuxt.js

Nuxt.js とは、**Vue.js アプリケーションを構築するためのフレームワーク**です。以下のパッケージを含んでいます。

-   Vue 2
-   Vue Router
-   Vuex（ストアオプションを利用している場合）
-   Vue Server Renderer（`mode: 'spa'`を利用している場合を除く）
-   Vue Meta

参照：

-   [NuxtJS](https://ja.nuxtjs.org/guide)

## Installation

スターターキットが用意されているので、以下から始めると楽です。

=== "Yarn"

    ```bash
    yarn create nuxt-app
    ```

## Directory Structure

＊付きは、ほぼ必須のディレクトリです。

### `assets/`

-   静的に配信したいアセットのうち、webpack に含むものを配置

### `components/`＊

-   コンポーネントを定義する。
-   ファイル名は UpperCamelCase で宣言。
-   テンプレートから使用する時のタグは kebab-case

### `layouts/`＊

-   ヘッダーやフッターなど、所謂テンプレートの「がわ」を定義
-   デフォルトでは全ページに default.vue が適用される
-   変更する際は各ページの header プロパティで指定

### `middleware/`

-   ルーティングに割り込む処理をアプリケーション全体に適用する

### `pages/`＊

-   nuxt のアプリケーションの各ページを記載
-   ファイル階層がそのまま URL になる

### `plugins/`

-   グローバルで使用したいライブラリや関数などを登録する

### `static/`

-   静的に配信したいアセットのうち、webpack に含まないものを配置

### `store/`＊

-   Vuex の store ファイルを格納する

## Config - `nuxt.config.js`

| config       | description                                                   |
| ------------ | ------------------------------------------------------------- |
| `build`      | loaders、filenames や webpack の設定等、`build`に関わる設定   |
| `css`        | すべてのページで利用したい CSS ファイル/モジュール/ライブラリ |
| `dev`        | development または production                                 |
| `env`        | 環境変数                                                      |
| `generate`   | 動的なルーティングに用いるパラメータ                          |
| `head`       | デフォルトのメタタグ                                          |
| `loading`    | デフォルトのローディングコンポーネント                        |
| `modules`    | 追加する Nuxt モジュール                                      |
| `modulesDir` | node_modules ディレクトリの場所                               |
| `plugins`    | Vue.js アプリのインスタンス化前に実行したい JS plugin         |
| `rootDir`    | Nuxt.js アプリケーションのワークスペースの場所                |
| `router`     | デフォルトの Vue Router 設定を上書き                          |
| `server`     | サーバーインスタンスにおける接続変数                          |
| `srcDir`     | ソースディレクトリの場所                                      |
| `dir`        | カスタムディレクトリ                                          |
| `transition` | ページトランジションのデフォルトプロパティ                    |

## Component Options

### `asyncData`

-   テンプレートに出力する変数（コンポーネントデータ）を定義する。
-   universal モードの時、サーバーサイドで実行される
-   サーバーサイドで実行される関数内では this にアクセスできないため、引数に context を受け取る。
-   content 経由で Vue にグローバルで定義されている機能が参照できる
    -   Vuex の store, ルーティングパラメーター
    -   クライアントサイドでは通常通り this を触っているのと同じ動作になる
-   pages でのみ使用できる

### `computed`

-   ゲッターを配置する
-   テンプレートからは関数としてではなく変数として呼び出す

### `methods`

-   普通の関数群を定義
-   setter やその他の更新処理・操作など

### `fetch`

-   サーバーサイドで created よりも先に呼ばれる
-   Vuex ストアを準備するために使用
-   コンポーネントデータは準備できない
-   pages でのみ使用できる

### `created`

-   Vue.js の`created`イベントのタイミングで動作する
-   サーバーサイドとクライアントサイドの両方で呼ばれる

### `mounted`

-   Vue.js の`mounted`イベントのタイミングで動作する
-   universal モードでもクライアントサイドで実行される
-   window オブジェクトの操作など、クライアントサイドでだけ動かしたい処理を記述する

### `components`

-   コンポーネントを呼び出す
-   テンプレートで呼び出す時、タグ名はケバブケースになる

## Commands

| command         | description                                                      |
| --------------- | ---------------------------------------------------------------- |
| `nuxt`          | 開発サーバーを`localhost:3000`で起動する。（HR 付き）            |
| `nuxt build`    | webpack でビルドしする                                           |
| `nuxt start`    | プロダクションモードでサーバーを起動する（※`build`後に実行する） |
| `nuxt generate` | アプリケーションをビルドし、ルートごとに HTML ファイルを生成する |
