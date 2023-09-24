# Datasets

## 使い方

```py
from torchtext.datasets import IMDB

train_iter = IMDB(split='train')

def tokenize(label, line):
    return line.split()

tokens = []
for label, line in train_iter:
    tokens += tokenize(label, line)
```

## データセット

### テキスト分類

| Dataset              | Description                                           |
| -------------------- | ----------------------------------------------------- |
| AG_NEWS              | AG コーパス内ニュース記事のテキストとラベル(4 種類)   |
| AmazonReviewFull     | Amazon のレビューのタイトルと内容とラベル(5 段階評価) |
| AmazonReviewPolarity | Amazon のレビューのタイトルと内容とラベル(2 段階評価) |
| CoLA                 | 出版物の文章と注釈とラベル                            |
| DBPedia              | WPLE の記事のタイトルと内容とラベル(14 種類)          |
| IMDb                 | 映画のレビューの内容とラベル（2 種類）                |
| MNLI                 | 自然言語推論。前提と仮説とラベル                      |
| MRPC                 | 2 つの文と同じ意味かを表すラベル                      |
| QNLI                 | 質問と文と正しい回答かを表すラベル                    |
| QQP                  | Quara の質問と文と正しい回答かを表すラベル            |
| RTE                  | 2 つの文と同じ意味かを表すラベル                      |
| SogouNews            |                                                       |
| SST2                 |                                                       |
| STSB                 |                                                       |
| WNLI                 |                                                       |
| YahooAnswers         |                                                       |
| YelpReviewFull       |                                                       |
| YelpReviewPolarity   |                                                       |

### 言語モデリング

| Datasets     | Description |
| ------------ | ----------- |
| PennTreebank |             |
| WikiText-2   |             |
| WikiText103  |             |

### 機械翻訳

| Datasets  | Description |
| --------- | ----------- |
| IWSLT2016 |             |
| IWSLT2017 |             |
| Multi30k  |             |

### シーケンスのタグ付け

| Datasets          | Description |
| ----------------- | ----------- |
| CoNLL2000Chunking |             |
| UDPOS             |             |

### 質疑応答

| Datasets  | Description |
| --------- | ----------- |
| SQuAD 1.0 |             |
| SQuAD 2.0 |             |

### 教師なし学習

| Datasets | Description |
| -------- | ----------- |
| CC100    |             |
| EnWik9   |             |

## 参考文献

-   [torchtext.datasets - Torchtext](https://pytorch.org/text/stable/datasets.html)
-   [GLUE - 英語圏における自然言語処理の標準ベンチマーク | npaka | note](https://note.com/npaka/n/n5086fc19c5fc)
