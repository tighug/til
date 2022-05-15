# React Testing Library

## Installation

```bash
yarn add -D @testing-library/react
```

## API

#### `render`

```ts
function render(ui: React.ReactElement<any>, options?: {}): RenderResult;
```

- options
  - `container`
  - `baseElement`
  - `hydrate`
  - `wrapper`
  - `queries`
- result

#### `cleanup`

`render`でマウントされた Reqct ツリーをアンマウントする。Jest を使用する際には、自動で行われるため不要。

#### `act`

`react-dom/test-utils`の act 関数のラッパー。

## References

- [React Testing Library](https://testing-library.com/docs/react-testing-library/intro/)
- [testing-library/react-testing-library | GitHub](https://github.com/testing-library/react-testing-library)
