# SOLID

## 単一責任の原則

SRP : Single Responsibility Principle

モジュールを変更する理由は唯 1 つであるべきである。
（モジュールは唯 1 つのアクターに対して責務を負うべきである）

- 症例
  - あるアクターの処理を変更するとき、別のアクターに影響を及ぼす
  - 別々のアクターの変更が衝突する
- 解決策
  - アクターの異なるコードは分割する（同じクラスに含めない）

## オープン・クローズドの原則

OCP : Open-Closed Principles

ソフトウェアの構成要素は拡張に対しては開いていて、修正に対して閉じていなければならない

- 症例
  - インフラ等の下位レベルの変更が、ビジネスロジック等の上位レベルに影響を与える
- 解決策
  - インターフェイス等を用いた依存関係逆転により、依存の方向を制御する

## リスコフの置換原則

LSP : Liskov Substitution Principles

## インターフェイス分離の原則

Interface Segregation Principles

## 依存関係逆転の原則

DIP : Dependency Inversion Principles
