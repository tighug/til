# Go os

## ファイル操作

### Open

```go
file, err := os.Open("flle.txt")
```

### Stat

```go
fileInfo := file.Stat()
fileInfo.Name() // ファイル名（string）
fileInfo.Size() // ファイルサイズ（int64）
fileInfo.Mode() // ファイルのモード（os.FileMode）
fileInfo.ModTime()  // ファイルの最終更新時間（time.Time）
fileInfo.IsDir()  // ディレクトリかどうか（bool）
```

### Create

```go
f, _ := os.Create("foo.txt")  // 新規作成
```

### Remove

```go
err := os.Remove("foo.txt") // 削除
err := os.Remove("foo") // ディレクトリも同じ。空じゃない場合はエラー
err := os.RemoveAll("foo")  // 空じゃないディレクトリの削除
```

### Rename

名前変更、移動

```go
err := os.Rename("foo", "bar")  // fooをbarに名前変更
err := os.Rename("foo", "bar/foo")  // 移動
```

## ディレクトリ操作

### Getwd

```go
dir, err := os.Getwd()  // カレントディレクトリの取得
```

### Chdir

```go
err := os.Chdir("/path/to/dir") // カレントディレクトリの移動
```

### Mkdir

```go
err := os.Mkdir("foo", 0775)  // fooディレクトリを作成。第2引数はパーミッション
err := os.MkdirAll("foo/bar/baz", 0775) // 一括作成
```
