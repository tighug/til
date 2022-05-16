# CSS

## カスケードと継承

-   カスケード : 後に書かれたルールが優先される
-   詳細度
-   継承

## セレクター

-   要素 : `h1 { }`
-   全称 : `* { }`
-   クラス : `.box { }`
-   ID : `#unique { }`
-   属性 : `a[title] { }`
-   擬似クラス : `p:first-child { }`
-   疑似要素 : `p::first-line { }`
-   子孫結合子 : `article p { }`
-   子結合子 : `article > p { }`
-   隣接兄弟結合子 : `h1 + p { }`
-   一般兄弟結合子 : `h1 - p { }`

## ボックスモデル

-   block と inline
    -   block
        -   新しい行に改行される
        -   `width`と`height`が適用される
        -   `padding`/`margin`/`border`により、他の要素が押しのけられる
    -   inline
        -   `width`と`height`が適用されない
        -   新しい行に改行されない
        -   `padding`/`margin`/`border`により、他の要素が押しのけられない
-   `box-sizing`
    -   `content-box` : `width`/`height`に`padding`/`border`を含まない
    -   `border-box` : `width`/`height`に`padding`/`border`を含む

## セレクター

-   タイプセレクター
-   class
-   id
-   ユニバーサルセレクター

## 属性によるセレクター

### 擬似クラスと疑似要素によるセレクター

-   :first-child, :first-of-type
-   :not
-   :hover
-   ::after, ::before
-   ::first-line

### 結合子

-   子孫結合子
-   子結合子
-   隣接兄弟結合子
-   一般兄弟結合子

## カスケード・詳細度・継承

## ボックスモデル

-   Content
-   Padding
-   Margin
-   Border

## ブロックボックスとインラインボックス

## Flexbox

## overflow

-   visible
-   hidden
-   scroll

## Best Practices

## References

-   [MDN](https://developer.mozilla.org/en-US/docs/Web/CSS)
-   [Flexbox spec](https://www.w3.org/TR/css-flexbox-1/)
-   [How to learn CSS](https://www.smashingmagazine.com/2019/01/how-to-learn-css/)
-   [CSS Tricks Almanac](https://css-tricks.com/almanac/)
-   [Flexbox zombie](https://geddski.teachable.com/p/flexbox-zombies)
