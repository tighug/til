# HTML

HTML（Hypertext Markup Language）は、ウェブページを表現するために使用するマークアップ言語です。

## `<head>`と`<body>`

### `head`に記述する要素

- `<title>`
- `<meta>`
  - `charset`
  - `name`
  - `content`
- `<link>`
  - `rel`
  - `href`
  - `type`
- `<script>`

## 見出し

```html
<h1>Header 1</h1>
<h2>Header 2</h2>
<h3>Header 3</h3>
...
<h6>Header 6</h6>
```

- `<h1>`はページごとに 1 つだけ
- 見出しの順序は連続させる

## リスト

順序なし

```html
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Citrus</li>
</ul>
```

順序有り

```html
<ol>
  <li>First</li>
  <li>Second</li>
  <li>Third</li>
</ol>
```

## 強調

- `<em>` : 斜め文字
- `<strong>` : 太字

## リンク

```html
<a
  href="https://www.mozilla.org/ja/"
  title="The best place to find more information about Mozilla's
          mission and how to contribute"
  >the Mozilla homepage</a
>.
```

- できるだけ相対リンクを使う
- ダウンロードへのリンクは`download`属性

## 説明リスト

```html
<dl>
  <dt>独白</dt>
  <dd>
    ドラマでは、登場人物が自分自身にしゃべりかけ、内なる考えや感情や、そうなった過程を(他の登場人物ではなく)観客に対して表現します。
  </dd>
  <dt>独白</dt>
  <dd>
    ドラマで、登場人物が自分の考えを観客や他の登場人物に伝わるように喋ります。
  </dd>
  <dt>ひそひそ話</dt>
  <dd>
    ドラマで、登場人物が観客のみに対し、ユーモアやドラマチックな効果を狙ってコメントをします。これは通常は感情や、考えや、追加の背景情報です。
  </dd>
</dl>
```

## 引用

ブロッククォート

```html
<blockquote
  cite="https://developer.mozilla.org/ja/docs/Web/HTML/Element/blockquote"
>
  <p>
    The HTML blockquote Element indicates that the enclosed text is an extended
    quotation.
  </p>
</blockquote>
```

インラインクォート

```html
<p>
  <q cite="https://developer.mozilla.org/ja/docs/Web/HTML/Element/q"
    >intended for short quotations that don't require paragraph breaks.</q
  >
</p>
```

## 略語

```html
<p>
  We use <abbr title="Hypertext Markup Language">HTML</abbr> to structure our
  web documents.
</p>
```

## ソースコード

- `<code>` : ソースコード
- `<pre>` : 空白 (通常はコードブロック) を保持する
- `<var>` : 変数名
- `<kbd>` : キーボード入力
- `<samp>` : プログラムの出力

```html
<pre><code>var para = document.querySelector('p');

para.onclick = function() {
  alert('Owww, stop poking me!');
}</code></pre>

<p>
  You shouldn't use presentational elements like <code>&lt;font&gt;</code> and
  <code>&lt;center&gt;</code>.
</p>

<p>
  In the above JavaScript example, <var>para</var> represents a paragraph
  element.
</p>

<p>Select all the text with <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>A</kbd>.</p>

<pre>$ <kbd>ping mozilla.org</kbd>
<samp>PING mozilla.org (63.245.215.20): 56 data bytes
64 bytes from 63.245.215.20: icmp_seq=0 ttl=40 time=158.233 ms</samp></pre>
```

## 日付と時刻

```html
<time datetime="2016-01-20">20 January 2016</time>
```

## セマンティック要素

- `<header>` : ヘッダー
  - `<body>`の子である時、グローバルヘッダー
  - `<article>`または`<section>`の子である時、
- `<nav>` : ナビゲーションバー
- `<main>` : メインコンテンツ
  - ページごとに一回
  - `<body>`の中に直接入れる
  - 他の要素の中に入れない
- `<article>` : 記事
  - ページの残りの部分なしで、それ自体が意味を成すブロックを囲む
- `<section>` : セクション
  - ある機能を構成する部分をグループ化する
  - 各セクションは見出しで始める
- `<aside>` : サイドバー
  - メインコンテンツに直接関連しないコンテンツ
  - 用語集エントリ、著者略歴、関連リンクなど
- `<footer>` : フッター

## 非セマンティック要素

- `<div>` : ブロック要素
- `<span>` : インライン要素

## 改行と水平線

- `<br>` : 改行
- `<hr>` : 水平線

## 画像

```html
<img src="画像ソース" alt="代替テキスト" />
```

図表・キャプション

```html
<figure>
  <img
    src="images/dinosaur.jpg"
    alt="恐竜の骨格の頭と胴体、
            それは長い鋭い歯を持つ大きな頭を持っています"
    width="400"
    height="341"
  />

  <figcaption>マンチェスター大学博物館に展示されている T-Rex。</figcaption>
</figure>
```

## ビデオ

```html
<video controls>
  <source src="rabbit320.mp4" type="video/mp4" />
  <source src="rabbit320.webm" type="video/webm" />
  <p>
    お使いのブラウザは HTML5 動画をサポートしていません。その代わりに<a
      href="rabbit320.mp4"
      >動画へのリンク</a
    >があります。
  </p>
</video>
```

## 音声

```html
<audio controls>
  <source src="viper.mp3" type="audio/mp3" />
  <source src="viper.ogg" type="audio/ogg" />
  <p>
    お使いのブラウザは HTML5 音声をサポートしていません。代わりに<a
      href="viper.mp3"
      >音声へのリンク</a
    >があります。
  </p>
</audio>
```
