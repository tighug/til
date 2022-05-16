# Make

## Syntax

```makefile
target: prerequisites
  command
  command
  command
```

`command`のことを`recipe`と呼ぶ。インデントは`<TAB>`。

## Command

以下で`target`の`recipe`が呼び出される。
`target`を省略すると、一番上の`target`が対象になる。

```bash
make [target]
```

## Usage

all：一度に複数のターゲットを呼び出す

```makefile
all: hello generate
```

自動変数

- `$@`；`target`名
- `$%`
- `$<`：最初の`prerequisites`名
- `$^`：すべての`prerequisites`名

## References

- [What is a Makefile and how does it work?](https://opensource.com/article/18/8/what-how-makefile)
