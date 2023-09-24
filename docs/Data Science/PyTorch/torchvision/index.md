# torchvision

## Installation

=== "Poetry"

    ```bash
    poetry add torchvision
    ```

## APIs

### transforms

#### Compose

```py
# Params
transforms: list[Transform]

# Return
list[Transform]
```

???+ example

    ```py
    transforms.Compose([
        transforms.CenterCrop(10),
        transforms.PILToTensor(),
        transforms.ConvertImageDtype(torch.float),
    ])
    ```

## References

-   [公式ドキュメント](https://pytorch.org/vision/stable/index.html)
