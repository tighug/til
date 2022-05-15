# Semantic HTML

## Tags

### section

見出しを含む、テーマ別のコンテンツのグループ

```html
<section>
  <h1>WWF</h1>
  <p>The World Wide Fund for Nature (WWF) is</p>
</section>
```

### article

独立した、自己完結型のコンテンツ。
記事はそれ自体で意味があり、他の要素から独立して読むことができるはず

```html
<article>
  <h1>What Does WWF Do?</h1>
  <p>
    WWF's mission is to stop the degradation of our planet's natural
    environment, and build a future in which humans live in harmony with nature.
  </p>
</article>
```

### header

文書またはセクションのヘッダー。
1 つのドキュメントに複数の要素を含めることができる

```html
<article>
  <header>
    <h1>What Does WWF Do?</h1>
    <p>WWF's mission:</p>
  </header>
  <p>
    WWF's mission is to stop the degradation of our planet's natural
    environment, and build a future in which humans live in harmony with nature.
  </p>
</article>
```

### footer

文書またはセクションのフッター。
ドキュメントの作成者、著作権情報、利用規約へのリンク、連絡先情報などが含まれる。
1 つのドキュメントに複数の要素を含めることができる

```html
<footer>
  <p>Posted by: Hege Refsnes</p>
  <p>
    Contact information:
    <a href="mailto:someone@example.com"> someone@example.com</a>.
  </p>
</footer>
```

### main

ドキュメントの主な内容。
サイドバー、ナビゲーションリンク、著作権情報、サイトのロゴ、検索フォームなど、
ドキュメント全体で繰り返されるコンテンツを含めることはできない

### nav

ナビゲーションリンクのセット

```html
<nav>
  <a href="/html/">HTML</a> | <a href="/css/">CSS</a> |
  <a href="/js/">JavaScript</a> |
  <a href="/jquery/">jQuery</a>
</nav>
```

### aside

内容とは別のコンテンツ。
周囲のコンテンツに関連しなければならない

```html
<p>My family and I visited The Epcot center this summer.</p>

<aside>
  <h4>Epcot Center</h4>
  <p>The Epcot Center is a theme park in Disney World, Florida.</p>
</aside>
```

### figure

### figcaption

## References

- [HTML Semantic Elements | w3schools.com](https://www.w3schools.com/html/html5_semantic_elements.asp)
