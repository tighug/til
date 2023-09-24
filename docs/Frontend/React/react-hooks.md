# React Hooks

フック（hook）はReact16.8で追加された新機能です。stateなどのReactの機能を**クラスを書かずに**使えるようになります。

## Usage

### `useState`

関数コンポーネントに状態を定義する。

```tsx
const [count, setCount] = useState(0);
```

### `useEffect`

関数コンポーネントのレンダリング**後**に実行したい関数を定義する。

- DOMの操作
- APIなど外部データの取得

## References

- [React Hooks](https://ja.reactjs.org/docs/hooks-intro.html)
