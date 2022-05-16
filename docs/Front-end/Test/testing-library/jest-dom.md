# jest-dom

## Installation

```bash
yarn add -D @testing-library/jest-dom
```

## Setup

1. `jest-setup.(js|ts)`に以下を追記する。

```ts
import "@testing-library/jest-dom";
```

2. `jest.config.js`に以下を追記する。

```js
setupFilesAfterEnv: ["<rootDir>/jest-setup.js"];
```

### With TypeScript

`tsconfig.json`に以下を追記する。

```json
"include": [
    "./jest-setup.ts"
],
```

## Custom matchers

| matchers                            | description                |
| ----------------------------------- | -------------------------- |
| `toBeDisabled()`                    | Disabled                   |
| `toBeEnabled()`                     | Enabled                    |
| `toBeEmptyDOMElement()`             | 子要素を持たない           |
| `toBeInTheDocument()`               | ドキュメント内に存在       |
| `toBeValid()`                       | Valid                      |
| `toBeInvalid()`                     | Invalid                    |
| `toBeRequired()`                    | Required                   |
| `toBeVisible()`                     | Visible                    |
| `toContainElement(element)`         | `element`を子に持つ        |
| `toContainHTML(htmlText)`           | `htmlText`を子に持つ       |
| `toHaveAttribute(attr, value?)`     | `attr`を属性に持つ         |
| `toHaveClass(classNames, options?)` | `classNames`をクラスに持つ |
| `toHaveFocus()`                     | Focused                    |
| `toHaveFormValues()`                |                            |
| `toHaveStyle(css)`                  | `css`をスタイルに持つ      |
| `toHaveTextContent(text)`           | テキストが`text`           |
| `toHaveValue(value)`                | 値が`value`                |
| `toHaveDisplayValue()`              |                            |
| `toBeChecked()`                     |                            |
| `toBePartiallyChecked()`            |                            |
| `toHaveDescription()`               |                            |
| `toHaveErrorMessage()`              |                            |

- `button`/`input`/`select`/`textarea`/`optgroup`/`option`/`fieldset`

## References

- [testing-library/jest-dom | GitHub](https://github.com/testing-library/jest-dom)
