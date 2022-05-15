# Go encoding/csv

CSV ファイルの読み書きを行う。

## Installation

```go
import "encoding/csv"
```

## Usage

### Reader

```go
in := `first_name,last_name,username
"Rob","Pike",rob
Ken,Thompson,ken
"Robert","Griesemer","gri"
`
r := csv.NewReader(strings.NewReader(in))

records, err := r.ReadAll()
```

### Writer

```go
records := [][]string{
    {"first_name", "last_name", "username"},
    {"Rob", "Pike", "rob"},
    {"Ken", "Thompson", "ken"},
    {"Robert", "Griesemer", "gri"},
}

w := csv.NewWriter(os.Stdout)
w.WriteAll(records) // 内部のフラッシュを呼び出す
```

## References

- [Go 言語 / encoding/csv](https://xn--go-hh0g6u.com/pkg/encoding/csv/)
