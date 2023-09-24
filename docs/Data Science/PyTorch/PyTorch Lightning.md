# PyTorch Lightning

## インストール

```bash
poetry add pytorch-lightning
```

## 使い方

### LightingModule

| method                                  | desctiption |
| --------------------------------------- | ----------- |
| `__init__(self)`                        |             |
| `forward(self)`                         |             |
| `training_step(self, batch, batch_idx)` |             |
| `validation_step(self)`                 |             |
| `test_step(self)`                       |             |
| `predict_step(self)`                    |             |
| `configure_optimizers(self)`            |             |

### Trainer

```py
model = MyLightningModule()

trainer = Trainer()
trainer.fit(model, train_dataloader, val_dataloader)
```

## 参考文献

-   [PyTorch Lightning](https://pytorch-lightning.readthedocs.io/en/stable/)
