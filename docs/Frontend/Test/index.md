# テスト

## The Testing Trophy

- End to end : E2E テスト
  - Cypress
- Integration : 統合テスト
  - Jest
  - react-testing-library
- Unit : ユニットテスト
  - Jest
- Static : 静的テスト
  - Prettier : フォーマッター
  - ESLint : リンター
  - TypeScript : タイプチェッカー

## Best Practices

- 内部テストを避ける
  - false negative : 動作が同じでもテストに失敗する
  - false positive : コードが壊れていてもテストに成功する
- テストは決定論的であるべき
- 不要な Expect やテストを避ける
- Arrange-Act-Assert (AAA) Patterns

## References

- [Testing JavaScript](https://testingjavascript.com/)
- [Modern React testing](https://blog.sapegin.me/all/react-testing-1-best-practices/)
- [Testing Overview - React](https://ja.reactjs.org/docs/testing.html)
- [JavaScriipt Testing Best Practices](https://github.com/goldbergyoni/javascript-testing-best-practices/)
