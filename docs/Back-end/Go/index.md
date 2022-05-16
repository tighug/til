# Go

Go は 2009 年に Google によって発表されたプログラミング言語です。

## Installation

=== "macOS"

    ```bash
    brew install go
    ```

## Integrations

=== "VS Code"

1. [拡張機能](https://marketplace.visualstudio.com/items?itemName=golang.go)をインストール
2. VS Code 上でコマンドパレットを開き、`Go: Install/Update Tools`を実行
3. すべてのツールを選択して`OK`

## CLI

| command               | description                                  |
| --------------------- | -------------------------------------------- |
| `go version`          | Go のバージョンを表示                        |
| `go doc <pkg>`        | パッケージのドキュメントを表示               |
| `go env`              | Go に関する環境変数を表示                    |
| `go fmt`              | `.go`ファイルをフォーマット                  |
| `go get -u [package]` | 依存パッケージをインストール                 |
| `go list`             | パッケージとモジュールを一覧で表示           |
| `go build [packages]` | プログラムをコンパイル                       |
| `go run`              | プログラムをコンパイルして実行               |
| `go install`          | パッケージと依存をコンパイルしてインストール |

## Syntax

### Packages

-   パッケージ名はインポートパスの最後の要素と同じ
-   大文字で始まる名前はエクスポートされる

```go
import (
    "fmt"
    "math/rand"
)

func main() {
	fmt.Println(math.Pi)
}
```

### Functions

-   複数の同じ型の引数が並ぶ場合、最後以外の型を省略できる
-   複数の値を返せる

```go
func swap(x, y string) (string, string) {
	return y, x
}
```

-   返り値には名前を付けられる

```go
func split(sum int) (x, y int) {
	x = sum * 4 / 9
	y = sum - x
	return
}
```

### Variables

-   変数の宣言には、`var`を使う方法と`:=`を使う方法の 2 つがある
    -   `var`: どこでも使える
    -   `:=`: 関数内で使える。初期化が必要。型を省略できる
-   複数の同じ型の変数が並ぶ場合、最後以外の型を省略できる

```go
var i, j int = 1, 2
var c, python, java　= true, false, "no!"

func main() {
	k := 3
}
```

基本の型

```go
// Bool型（ゼロ値: false）
bool

// 文字列型（ゼロ値: ""）
string

// 数値型（ゼロ値: 0）
int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr
byte // alias for uint8
rune // alias for int32
float32 float64
complex64 complex128
```

型変換

```go
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)
```

固定値

```go
const Pi = 3.14
```

### For

-   セミコロンで 3 つに区切られる
    -   init 文: 最初の反復の前に実行される
    -   条件式: すべての反復の前に評価される
    -   post 文: すべての反復の最後に実行される

```go
for i := 0; i < 10; i++ {
    sum += i
}
```

-   Go には`while`はなく、`for`を使って表す

```go
for sum < 1000 {
	sum += sum
}
```

-   無限ループは次で表す

```go
for {
}
```

### If

-   条件式の前に、init 文を記述できる

```go
if v := math.Pow(x, n); v < lim {
    return v
} else {
    fmt.Printf("%g >= %g\n", v, lim)
}
```

### Switch

-   連続する if-else 文を短く書く方法
-   break は必要ない

```go
switch os := runtime.GOOS; os {
	case "darwin":
		fmt.Println("OS X.")
	case "linux":
		fmt.Println("Linux.")
	default: // freebsd, openbsd, plan9, windows...
		fmt.Printf("%s.\n", os)
}
```

-   条件式は省略可能
-   case は、固定値である必要はない

```go
t := time.Now()
switch {
case t.Hour() < 12:
    fmt.Println("Good morning!")
case t.Hour() < 17:
    fmt.Println("Good afternoon.")
default:
    fmt.Println("Good evening.")
}
```

### Defer

-   関数が`return`されるまで処理を延期する
-   複数の`defer`はスタックし、LIFO の順に呼ばれる

```go
func main() {
	defer fmt.Println("world")

	fmt.Println("hello")
}
```

### Pointers

-   `*T`: T 型のポインタ
-   `&i`: 値 i のポインタ
-   `*p`: ポインタ p の値

```go
var p *int
i := 42
p = &i // point to i
fmt.Println(*p) // read i through the pointer
*p = 21         // set i through the pointer
```

### Structs

-   構造体はフィールドの集合体
-   フィールドにはドットを使ってアクセスする

```go
type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	v.X = 4
}
```

-   構造体にはポインタを使ってアクセス可能`(*p).X`
-   記述が面倒なため`p.X`でもアクセス可能

```go
func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9
	fmt.Println(v)
}
```

-   `Name: value`でフィールドのサブセットだけを指定できる
-   省略されたサブセットにはゼロ値が割り当てられる

```go
var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	p  = &Vertex{1, 2} // has type *Vertex
)
```

### Arrays

-   `[n]T`で T 型のサイズ n の配列を表現する
-   固定長のため、スライスを使用する方が一般的
-   ゼロ値は`nil`

```go
var a [10]int
```

### Slices

-   `[]T`で T 型のスライスを表現する
-   可変長
-   ゼロ値は`nil`

```go
var s []int
```

-   `low`以上`high`未満の範囲で配列を切り出す

```go
a[low : high]
```

-   スライスは配列の参照のようなもので、スライス自体はデータを格納しない
-   スライスの要素を変更すると、基となる配列の要素が変更される
-   以下のスライスの宣言は、同じ大きさの配列を同時に生成する

```go
[]bool{true, true, false}
```

-   以下のスライスはすべて等価

```go
var a [10] int

a[0:10]
a[:10]
a[0:]
a[:]
```

-   スライスは大きさ（length）と容量（capacity）の両方を持つ
    -   length: スライスの要素数
    -   capacity: スライスの最初の要素から数えた、基となる配列の要素数

```go
len(s)
cap(s)
```

-   `make`関数で動的サイズの配列を作成できる

```go
a := make([]int, 5)  // len(a)=5
```

-   `append`関数でスライスに要素を追加できる

```go
var s []int
s = append(s, 0)
s = append(s, 1)
s = append(s, 2, 3, 4)
```

-   `for`文では`range`を使って、スライスやマップを反復処理できる

```go
var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	for i, v := range pow {
		fmt.Printf("2**%d = %d\n", i, v)
	}
}
```

### Maps

-   マップは`key`と`value`の組み合わせの集合体
-   ゼロ値は`nil`

```go
type Vertex struct {
	Lat, Long float64
}

var m map[string]Vertex

func main() {
    m = make(map[string]Vertex)
}
```

-   リテラル
-   トップレベルの型がただの型名であれば省略可能

```go
var m = map[string]Vertex{
	"Bell Labs": Vertex{
		40.68433, -74.39967,
	},
	"Google": Vertex{
		37.42202, -122.08408,
	},
}

var m = map[string]Vertex{
	"Bell Labs": {40.68433, -74.39967},
	"Google":    {37.42202, -122.08408},
}
```

-   以下でマップの要素を変更したり、取得したりできる

```go
m[key] = elem
elem = m[key]
```

-   以下で要素を削除できる

```go
delete(m, key)
```

-   要素が存在するかどうかは以下でチェックできる

```go
elem, ok = m[key]
```

### Methods

-   Go にクラスの概念はないが、型に対してメソッドを定義できる
-   メソッドはレシーバー引数を持つ関数

```go
type Vertex struct {
	X, Y float64
}

func (v Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func main() {
	v := Vertex{3, 4}
	fmt.Println(v.Abs())
}
```

-   レシーバーの型には、値レシーバー`T`の代わりにポインタレシーバー`*T`を宣言できる
-   ポインタレシーバーの場合、レシーバーを変更できる
-   メソッドはレシーバーを変更することがよくあるため、ポインタレシーバーの方が一般的

```go
func (v *Vertex) Scale(f float64) {
	v.X = v.X * f
	v.Y = v.Y * f
}

func main() {
	v := Vertex{3, 4}
	v.Scale(10)
	fmt.Println(v.Abs())
}
```

-   簡単のため、値を通してメソッドを呼び出しても、ポインタを通して呼び出したとして解釈される

```go
var v Vertex
v.Scale(5)  // OK
p := &v
p.Scale(10) // OK
```

### Interfaces

```go
type Abser interface {
	Abs() float64
}

func main() {
	var a Abser
	f := MyFloat(-math.Sqrt2)
	v := Vertex{3, 4}

	a = f  // a MyFloat implements Abser
	a = &v // a *Vertex implements Abser

	// In the following line, v is a Vertex (not *Vertex)
	// and does NOT implement Abser.
	a = v

	fmt.Println(a.Abs())
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
	if f < 0 {
		return float64(-f)
	}
	return float64(f)
}

type Vertex struct {
	X, Y float64
}

func (v *Vertex) Abs() float64 {
	return math.Sqrt(v.X*v.X + v.Y*v.Y)
}
```

-   インターフェイスは暗黙的に実装される

```go
type I interface {
	M()
}

type T struct {
	S string
}

// This method means type T implements the interface I,
// but we don't need to explicitly declare that it does so.
func (t T) M() {
	fmt.Println(t.S)
}

func main() {
	var i I = T{"hello"}
	i.M()
}
```

-   空のインターフェイス`interface{}`は、型が不明な値を表す

```go
var i interface{}
```

-   不明な型に対して、以下のように型アサーションを使用できる

```go
s, ok := i.(string)
```

-   Type switches

```go
switch v := i.(type) {
case int:
	fmt.Printf("Twice %v is %v\n", v, v*2)
case string:
	fmt.Printf("%q is %v bytes long\n", v, len(v))
default:
	fmt.Printf("I don't know about type %T!\n", v)
}
```

### Errors

```go
i, err := strconv.Atoi("42")
if err != nil {
    fmt.Printf("couldn't convert number: %v\n", err)
    return
}
```

## Modules

| command       | description                                      |
| ------------- | ------------------------------------------------ |
| `go mod init` | カレントディレクトリを新規モジュールとして初期化 |
| `go mod tidy` | 不足モジュールを追加、未使用モジュールの削除     |

## References

-   [Go](https://golang.org/)
-   [Go By Example（日本語訳）](https://www.spinute.org/go-by-example/)
