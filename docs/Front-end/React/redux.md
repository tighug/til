# Redux

Redux とは、**JavaScript アプリ用の予測可能な状態コンテナ**です。React で利用する場合には、[React Redux](./ReactRedux.md)も併せて参照してください。また、公式推奨のツールキットとして[Redux Toolkit](./ReduxToolkit.md)が利用できます。

## Installation

```bash
yarn add redux
```

## Usage

### State

状態を格納するオブジェクト

```js
{ count: 0, }
```

### Reducer

受け取った Action に応じて State を変更し、新たな State を返す関数。

```js
function reducer(state, action) {
  switch (action.type) {
    case "INCREMENT":
      return { count: state.count + 1 };
    case "ADD":
      return { count: state.count + action.payload };
    default:
      return state;
  }
}
```

### Action

```js
{ type: 'INCREMENT' } // typeがStateに対する操作を表す
{ type: 'ADD', payload: 3 } // payloadは任意の引数
```

### Action Creator

```js
function increment() {
  return { type: "INCREMENT" };
}

function add(number) {
  return { type: "ADD", payload: number };
}
```

## With Redux Toolkit

## With Hooks

## References

- [Redux](https://redux.js.org/)
- [Redux 入門【ダイジェスト版】10 分で理解する Redux の基礎](https://qiita.com/kitagawamac/items/49a1f03445b19cf407b7)
- [Hook と Redux Toolkit で React Redux に入門する
  ](https://www.hypertextcandy.com/learn-react-redux-with-hooks-and-redux-starter-kit)
