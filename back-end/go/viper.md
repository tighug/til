# Viper

## Installation

```bash
go get github.com/spf13/viper
```

## Usage

```go
// デフォルト値
viper.SetDefault("key", value)

// 設定ファイルの読み取り
viper.SetConfigName("config")
viper.AddConfigPath(path)
err := viper.ReadInConfig()

// 値の取り出し
GetBool(key string)
GetFloat64(key string)
GetInt(key string)
GetString(key string)
```
