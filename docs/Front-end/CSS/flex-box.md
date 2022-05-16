# CSS Flexbox

```css
display: flex;
```

## コンテナ

### `flex-direction`

子要素の並ぶ向き

```css
flex-direction: row;
```

- row
- row-reverse
- column
- column-reverse

### `flex-wrap`

子要素の折返し

```css
flex-wrap: wrap;
```

- nowrap
- wrap
- wrap-reerse

### `flex-flow`

`flex-direction`と`flex-wrap`をまとめて指定

```css
flex-flow: row wrap;
```

### `justify-content`

水平方向の並べ方

```css
justify-content: flex-end;
```

- flex-start
- flex-end
- center
- space-between
- space-around

### `align-items`

垂直方向の並べ方

```css
align-items: center;
```

- stretch
- flex-start
- flex-end
- center
- baseline

### `align-content`

複数行にしたときの並べ方

```css
align-content: space-between;
```

- stretch
- flex-start
- flex-end
- center
- space-between
- space-around

## アイテム

### `order`

順序の指定

```css
order: 2;
```

### `flex-grow`

子要素の伸び比率

```css
flex-grow: 2;
```

### `flex-shrink`

子要素の縮み比率

```css
flex-shrink: 2;
```

### `flex-basis`

子要素のベースとなる幅の指定

```css
flex-basis: 200px;
```

### `flex`

`flex-grow`、`flex-shrink`、`flex-basis`をまとめて指定

```css
flex: 0 1 30%;
```

### `align-self`

子要素の垂直方向の並べ方

```css
align-self: flex-end;
```

- auto
- flex-start
- flex-end
- center
- stretch
- baseline
