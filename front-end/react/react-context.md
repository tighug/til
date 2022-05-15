# React Context

通常の React アプリでは、データは props を通してトップダウンで渡されます。しかし、UI テーマなどのグローバルなプロパティをバケツリレーのように下層のコンポーネントに渡すことは冗長であり、コンポーネントの密結合も引き起こします（**Prop Drilling**）。コンテクストは各階層で明示的にプロパティを渡すことなく、これを実現します。

## When to Use Context

「**Prop Drilling**」を解消するには以下の三つの方法があり、状況に応じて使い分けます。

1. Children
2. Redux
3. Context

## Usage

## References

- [React Context](https://ja.reactjs.org/docs/context.html)
