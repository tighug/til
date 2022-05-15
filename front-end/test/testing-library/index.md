# Testing Library

## Installation

```bash
yarn add -D @testing-library/react # For React
yarn add -D @testing-library/jest-dom # For Jest
yarn add -D eslint-plugin-jest-dom # For Jest with ESLint
```

## API

```ts
import { render, screen } from "@testing-library/react";

test("should show login form", () => {
  render(<Login />);
  const input = screen.getByLabelText("Username");
  // Events and assertions...
});
```

The former ones

| queries         | No Match    | 1 Match | 1+ Match | Await? |
| --------------- | ----------- | ------- | -------- | ------ |
| `getBy...`      | throw       | return  | throw    | No     |
| `queryBy...`    | throw       | return  | throw    | Yes    |
| `findBy...`     | null        | return  | throw    | No     |
| `getAllBy...`   | throw       | array   | array    | No     |
| `queryAllBy...` | empty array | array   | array    | Yes    |
| `findAllBy...`  | throw       | array   | array    | No     |

The latter ones

- `...LabelText`
- `...PlaceholderText`
- `...Text`
- `...DisplayValue`
- `...AltText`
- `...Title`
- `...Role`
- `...TestId`

## References

- [Testing Library](https://testing-library.com/docs/)
