# Jest Styled Components

Jest Styled Components は、Styled Components に対しての Jest によるスナップショットの挙動を改善し、さらにカスタムマッチャーを追加します。

## Installation

=== "Yarn"

    ```bash
    yarn add -D jest-styled-components
    ```

## Usage

```ts
import React from "react";
import styled from "styled-components";
import { render } from "@testing-library/react";
import "jest-styled-components";

const Button = styled.button`
    color: red;
`;

test("it works", () => {
    const { container } = render(<Button />);
    expect(container.firstChild).toMatchSnapshot();
});
```

## Custom Matchers

```ts
const Button = styled.button`
    color: red;
    border: 0.05em solid ${(props) =>
            props.transparent ? "transparent" : "black"};
    cursor: ${(props) => !props.disabled && "pointer"};
    opacity: ${(props) => props.disabled && ".65"};
`;

test("it applies default styles", () => {
    const tree = renderer.create(<Button />).toJSON();
    expect(tree).toHaveStyleRule("color", "red");
    expect(tree).toHaveStyleRule("border", "0.05em solid black");
    expect(tree).toHaveStyleRule("cursor", "pointer");
    expect(tree).not.toHaveStyleRule("opacity"); // equivalent of the following two
    expect(tree).not.toHaveStyleRule("opacity", expect.any(String));
    expect(tree).toHaveStyleRule("opacity", undefined);
});

test("it applies styles according to passed props", () => {
    const tree = renderer.create(<Button disabled transparent />).toJSON();
    expect(tree).toHaveStyleRule(
        "border",
        expect.stringContaining("transparent")
    );
    expect(tree).toHaveStyleRule("cursor", undefined);
    expect(tree).toHaveStyleRule("opacity", ".65");
});
```

## References

-   [styled-components/jest=styled-components](https://github.com/styled-components/jest-styled-components)
