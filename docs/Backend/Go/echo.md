# Echo

## Installation

```bash
go get -u github.com/labstack/echo/v4
```

## Basic Usage

```go title="server.go"
package main

import (
    "het/http"

    "github.com/labstack/echo/v4"
)

func main() {
    e := echo.New()
    e.Get("/", hello)
    e.Logger.Fatal(e.Start(":1323"))
}

func hello(c echo.Context) error {
    return c.String(http.StatusOK, "Hello, World!")
}
```

サーバー開始

```bash
go run server.go
```

## Request

## Response

## References

-   [Echo](https://echo.labstack.com/)
