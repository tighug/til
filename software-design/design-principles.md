# Design Principles

オブジェクト指向における設計原則をまとめたものです。

- [新人プログラマが知るべきプログラミングの原則６選！ | Qiita](https://qiita.com/ryotanatsume/items/018cae5c5be8faba367a)
- [開発者が知っておくべき SOLID の原則](https://postd.cc/solid-principles-every-developer-should-know/)
- [オブジェクト指向設計原則とは | Qiita](https://qiita.com/UWControl/items/98671f53120ae47ff93a)
- [オブジェクト指向の設計原則の概要とそれが重要な理由 | Qiita](https://qiita.com/shoichiimamura/items/21655fe9db7a39ffb113)

## SOLID

SOLID とは、オブジェクト指向における 5 つの原則をまとめたものです。

### 1. 単一責任の原則

SRP：Single Responsibility Principle

クラスを変更する理由は 1 つ以上存在してはならない。

### 2. オープン・クローズドの原則

OCP：Open-Closed Principle

1. 拡張に対して開かれている（Open）
2. 修正に対して閉じている（Closed）

### 3. リスコフの置換原則

LSP：Liskov Substitution Principle

派生型はその基本型と置換可能でなければならない。

### 4. インターフェイス分離の法則

ISP：Interface Segregation Principle

クライアントに、クライアントが利用しないメソッドへの依存を強制してはならない。

### 5. 依存関係逆転の原則

DIP：Dependency Inversion Principle

1. 上位のモジュールは下位のモジュールに依存してはならない、どちらのモジュールも「抽象」に依存すべきである
2. 「抽象」は実装の詳細に依存してはならない。実装の詳細が「抽象」に依存すべきである

## KISS

KISS：Keep It Simple, Stupid

短くシンプルでわかりやすくすべきである。

## YAGNI

YAGNI：You Aren't Going to Need it.

汎用性よりも単純性を優先すべきである。
