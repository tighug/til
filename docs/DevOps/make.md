# Make

> GNU Make is a tool which controls the generation of executables and
> other non-source files of a program from the program's source files.

## インストール

=== "Mac"

    ```bash
    xcode-select --install
    ```

=== "Windows"

    [GNUの公式サイト](https://www.gnu.org/software/make/)からインストーラーをダウンロードする。

=== "Ubuntu"

    ```bash
    sudo apt-get update
    sudo apt-get install make
    ```

## 使い方

### コマンド

```bash
make [target]
```

## Makefile

ルールは以下のフォーマットに従います。

```makefile
target: prerequisites
    recipe
    recipe
    recipe
```

### 自動変数

| 自動変数 | 説明         |
| -------- | ------------ |
| `$@`     | ターゲット名 |

## 参考

- [GNU make](https://www.gnu.org/software/make/manual/make.html)
- [Makefile Tutorial](https://makefiletutorial.com/)
