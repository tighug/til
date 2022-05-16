# Go os/exec

外部コマンドを実行する。

## Installation

```go
import "os/exec"
```

## Usage

### Command

外部コマンドを実行する。

```go
cmd := exec.Command("ls", "-la")

err := cmd.Run()  // 出力なし
stdout, err := cmd.Output() // 標準出力を返す
stdoutStderr, err := cmd.CombinedOutput() // 標準出力と標準エラー出力を返す

err := cmd.Start() // コマンドを開始。完了を待たない
err := cmd.Wait() // Startしたコマンドの完了を待つ

// パイプを使いたいとき。Start, Waitと一緒に使う
stdin, err := cmd.StdinPipe() // コマンドの標準入力に接続されるパイプ（io.WriteCloser, error）
stdout, err := cmd.StdoutPipe() // コマンドの標準出力に接続されるパイプ（io.ReadCloser, error）
stderr, err := cmd.StderrPipe() // コマンドの標準エラー出力に接続されるパイプ（io.ReadCloser, error）

cmd.Stdin = os.Stdin  // コマンドの標準入力先（io.Reader）
cmd.Stdout = os.Stdout  // コマンドの標準出力先（io.Writer）
cmd.Stderr = os.Stderr  // コマンドの標準出力先（io.Writer）
```
