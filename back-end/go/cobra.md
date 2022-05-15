# Cobra

## Installation

```bash
go get github.com/spf13/cobra/cobra@v1.0.0
```

## Usage

### Cobra Generator

```bash
cobra init --pkg-name [pkgName]

cobra add [command]
```

### Flags

### Persistent

設定したコマンドと、その配下のコマンドで利用可能。
グローバルフラグを設定するには、ルートコマンドにこれを設定すればいい。

```go
rootCmd.PersistentFlags().BoolVarP(&Verbose, "verbose", "v", false, "verbose output")
```

### Local

設定したコマンドだけで利用可能。

```go
localCmd.Flags().StringVarP(&Source, "source", "s", "", "Source directory to read from")
```

### Flags with Config

フラグで Viper で読み取る設定を上書き可能。

```go
rootCmd.PersistentFlags().StringVar(&author, "author", "YOUR NAME", "Author name for copyright attribution")
viper.BindPFlag("author", rootCmd.PersistentFlags().Lookup("author")) // フラグで設定ファイルを上書き
```

## References

- [spf13/cobra | GitHub](https://github.com/spf13/cobra)
