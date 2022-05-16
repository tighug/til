# Vue.js

Vue.js とは、**UI を構築するための JavaScript フレームワーク**の一つです。コンポーネント指向を特徴とします。

-   [Vue.js](https://jp.vuejs.org/v2/guide/index.html)

## Installation

=== "Yarn"

    ```bash
    yarn add vue
    ```

## Component Options

参照：[コンポーネントオプション | API リファレンス | Vue.js](https://012-jp.vuejs.org/api/options.html)

### 類似オプションの比較

#### `computed`と`data`

値の変更が無いのであれば、computed で定義します。

-   `data`
    -   処理上で変更されている可能性がある
    -   他人が書いたコードなどの場合、変更されているか調査する必要が出てくる
-   `computed`
    -   setter がない場合、read only になるため変更の可能性を考慮せずに済む[参考](https://qiita.com/k-okina/items/512b9e502f8db49981f3#1-data%E3%82%92%E6%A5%B5%E5%8A%9B%E5%AE%9A%E7%BE%A9%E3%81%97%E3%81%AA%E3%81%84)

#### `computed`と`methods`

テンプレート内にロジックを記述すると使い回すことができないが、`computed`、`methods`を利用することでロジックを使い回せます。パフォーマンス、キャッシュの有無を考えて使い分けます。([参考](https://jp.vuejs.org/v2/guide/computed.html#%E7%AE%97%E5%87%BA%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3-vs-%E3%83%A1%E3%82%BD%E3%83%83%E3%83%89))

-   `computed`
    -   依存するものが更新されたときにだけ、処理を再実行する
    -   それ以外は、キャッシュが利用される
-   `methods`
    -   常に再描画されると実行される

#### `computed`と`watch`

`computed`よりも`watch`の方が冗長な記述になるため、基本的には`computed`を利用する。
`watch`は、データの変更に応じて非同期処理をしたいときなどに利用する。[参考](https://jp.vuejs.org/v2/guide/computed.html#%E7%AE%97%E5%87%BA%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3-vs-%E7%9B%A3%E8%A6%96%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3)

## Tips

### Chrome 拡張機能

[Vue Devtools](https://chrome.google.com/webstore/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)

### Webpack と併用する場合

```js title="webpack.config.js"
resolve: {
  alias: {
    'vue$': 'vue/dist/vue.esm.js'
  }
}
```
