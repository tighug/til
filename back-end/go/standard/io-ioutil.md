# Go io/ioutil

I/O に役立つ関数を提供する。

## Installation

```go
import "io/ioutil"
```

## Usage

```go
// ディレクトリ内のファイルを返す（[]os.FileInfo, error）
files, err := ioutil.ReadDir(".")

// ファイルの内容を返す（[]byte, error）
content, err := ioutil.ReadFile("testdata/hello")

// ファイルにデータを書き込む。ファイルがある場合は上書き、ない場合は新規作成
err := ioutil.WriteFile("testdata/hello", []byte("Hello"), 0755)
```

## References

- [Go 言語 / ioutil](https://xn--go-hh0g6u.com/pkg/io/ioutil/)
