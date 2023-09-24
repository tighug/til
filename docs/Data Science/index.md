# Machine Learning

## Deep Learning

Deep Learning ≒ 良い関数を見つけて使うこと
（見つける → 学習、使う → 推論）

### 学習とは

1. 「良さ」とは何かを決める →「良さ関数（誤差関数）」を決める
2. 「使う関数」を決める → パラメーターを決める
    1. 「複雑性（表現力）」と「計算可能性」が必要 → 少ないパラメーターで複雑な関数
    2. 非線形と線形を組み合わせる
3. 「2 の関数」の中から「1 の関数」を最大にする関数を探す

### 代表的なレイヤー

-   全結合層（dense layer）
    -   「活性化関数」と「すべての変数を使う一次関数」の組み合わせ
    -   活性化関数：ReLU、softmax
    -   全結合 ReLU + 全結合 ReLU + 全結合 softmax
-   畳み込み層（convolution layer）
    -   CNN（Convolutional Neural Network）でよく使われる
    -   同じ位置にあるものをかけて足す ≒ 内積
    -   画像の局所的特徴（境界、線）を抽出可能
-   プーリング層
    -   CNN でよく使われる
    -   情報を失わずに圧縮
    -   平行移動に関する頑健性
    -   パラメタ数削減

## Machine Learning

### 流れ

0. prepare data
1. model
2. loss and optimizer
3. training loop

## Memo

1. ダウンロード
2. 前処理
3. 学習
4. 推論
5. 評価
6. ビルド
7. システム評価
