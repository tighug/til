# Clean Architecture

Clean Architecture とは、**大規模プロジェクトの設計において関心事の分離をするための設計手法**です。4 層の同心円図のイメージが特徴的で、各円はソフトウェアの領域を表します。「**依存性は内側だけに向かう**」というルールを持ちます。

![CleanArchitecture](images/clean-architecture.jpg)
Ref : [The Clean Code Blog](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

## Concept

### Enterprise Business Rules (domain)

ビジネスロジックを表現するオブジェクトが所属するレイヤー。

| 要素           | 依存               | 説明                                                                                                         |
| -------------- | ------------------ | ------------------------------------------------------------------------------------------------------------ |
| **model**      | -                  | ドメインモデル。ビジネスロジックをここに書く                                                                 |
| **repository** | model              | ドメインオブジェクトを取得・保存するインタフェース                                                           |
| **service**    | model / repository | ドメインオブジェクトに責務を持たせるものではないケース。または複数のドメインモデルを操作する時に使うシナリオ |

### Application Business Rules (usecase)

「ソフトウェアが何をできるのか」を表現するオブジェクトが所属するレイヤー。

| 要素        | 依存   | 説明                               |
| ----------- | ------ | ---------------------------------- |
| **usecase** | domain | ユースケースに応じた関数を用意する |

### Interface Adapters（interface）

入力、永続化、表示を担当するオブジェクトが所属するレイヤー。

| 要素           | 依存            | 説明                                  |
| -------------- | --------------- | ------------------------------------- |
| **gateway**    | domain、usecase | DB や API の操作。repository を実装。 |
| **controller** | domain          | データ加工。入力のための変換。        |
| **presenter**  | domain          | データ加工。出力のための変換。        |

### Frameworks & Drivers

Web フレームワークやデータベース操作オブジェクトなどが所属するレイヤー。

- Web
- Devices
- DB
- External Interfaces
- UI

## References

- [クリーンアーキテクチャー（翻訳）](https://blog.tai2.net/the_clean_architecture.html)
- [実装クリーンアーキテクチャー（Qiita）](https://qiita.com/nrslib/items/a5f902c4defc83bd46b8)
- [Clean Arichitecture を Node.js+TypeScript で実装してみる](https://blog.spacemarket.com/code/clean-architecture-node/)
- [iOS Clean Architecture | 騒音のない世界 BLOG](http://noiselessworld.hatenablog.jp/entry/ios-clean-architecture)
- [Clean Architecture で実装する時に知っておきたかったこと](https://christina04.hatenablog.com/entry/go-clean-architecture)
