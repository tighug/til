# Webpack Dev Server

webpack-dev-server は、webpack を使用したフロントエンド開発時に利用できる開発環境向けの Web サーバーです。

## Installation

```bash
yarn add -D webpack-dev-server
```

## CLI

```bash
webpack-dev-server  # Run DevServer
```

## Configuration

`webpack.config.js`の`devServer`内に記述する。

```js
module.exports = {
  devServer: {
    compress: true, // gzip圧縮を有効にする
    contentBase: path.join(__dirname, "build"), // htmlやcssのパス
    watchContentBase: true, // contentBaseの変更を監視する
    headers: { "Access-Control-Allow-Origin": "*" },
    historyApiFallback: {
      verbose: true,
      disableDotRule: false,
    },
    hot: true, // HMRを有効にする
    inline: true, // Auto Reload
    lazy: false, // Auto Reloadを無効にする（hotとは併用できない）
    noInfo: true, // バンドル情報のメッセージを抑制する
    port: 3000, // リッスンするポート
    // バンドルされたファイルのブラウザ上のパス
    publicPath: "/build/",
    watchOptions: {
      agreedTimeout: 300,
      ignored: /node_modules/,
      poll: 100,
    },
    before() {},
  },
};
```

### Auto Reload と Hot Reload

#### Auto Reload

コードに変更があった場合に自動でブラウザをリロードする。`inline`で指定し、デフォルトで有効。`inline`を無効にすると`iframe`モードで実行する。Auto Reloadを無効にするには、`lazy`を有効にする（`watchOptions`も無効になる）。

#### Hot Reload

コードに変更があった場合に変更箇所だけを自動で更新する。`hot`で指定し、デフォルトは無効。
`HotModuleReplacementPlugin`をプラグインに追加する必要がある

## References

- [Webpack DevServer](https://webpack.js.org/configuration/dev-server/)
