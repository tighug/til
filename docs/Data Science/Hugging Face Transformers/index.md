# Hugging Face Transformers

## インストール

```bash
poetry add transformers
```

## 使い方

推論の手法として、以下の 2 つが提供されています。

-   pipeline
-   tokenizer

pipeline は事前に学習されたモデルを使用する手法で、簡単に実装できます。。tokenizer は直接モデルをカスタマイズ可能です。

### pipeline

```py
from transformers import pipeline

classifier = pipeline("sentiment-analysis")
results = classifier([
    "We are very happy to show you the 🤗 Transformers library.",
    "We hope you don't hate it."
])

for result in results:
    print(f"label: {result['label']}, with score: {round(result['score'], 4)}")

# Output
# label: POSITIVE, with score: 0.9998
# label: NEGATIVE, with score: 0.5309
```

任意のモデルとトークナイザーを使用できます。

## 参考文献

-   [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
