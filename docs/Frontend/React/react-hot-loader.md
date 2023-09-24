# React Hot Loader

## Installation

```bash
yarn add react-hot-loader
```

1 `.babel.config.json`を修正する

```json
{
  "plugins": ["react-hot-loader/babel"]
}
```

2 Root コンポーネントを修正する

```jsx
// App.jsx
import { hot } from "react-hot-loader/root";
const App = () => <div>Hello World!</div>;
export default hot(App);
```

### With Hooks

```bash
yarn add @hot-loader/react-dom
```

`webpack.config.js`を修正する。

```js
resolve: {
    alias: {
      'react-dom': '@hot-loader/react-dom'
    }
}
```

## References

- [gaearon/react-hot-loader](https://github.com/gaearon/react-hot-loader)
- [hot-loader](https://github.com/hot-loader/react-dom)
