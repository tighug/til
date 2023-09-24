# GORM

## Installation

```bash
go get -u gorm.io/gorm

# driver
go get -u gorm.io/driver/sqlite  # SQLite
```

## Basic Usage

データベース接続

=== "MySQL"

    ```go
    import (
        "gorm.io/driver/mysql"
        "gorm.io/gorm"
    )

    dsn := "user:pass@tcp(127.0.0.1:3306)/dbname?charset=utf8mb4&parseTime=True&loc=Local"
    db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})
    ```

=== "PostgreSQL"

    ```go
    import (
        "gorm.io/driver/postgres"
        "gorm.io/gorm"
    )

    dsn := "host=localhost user=gorm password=gorm dbname=gorm port=9920 sslmode=disable TimeZone=Asia/Shanghai"
    db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    ```

=== "SQLite"

    ```go
    import (
        "gorm.io/driver/sqlite"
        "gorm.io/gorm"
    )

    db, err := gorm.Open(sqlite.Open("gorm.db"), &gorm.Config{})
    ```

## CRUD

```go
// Create
user := User{Name: "Jinzhu", Age: 18}
result := db.Create(&user)

// Read

```

## Association

## References

-   [GORM](https://gorm.io/)
