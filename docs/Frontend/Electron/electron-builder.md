# electron-builder

electron-builder とは、配布用の Electron アプリをパッケージ化するライブラリです。Auto Update 機能をサポートしています。

## Installation

=== "Yarn"

    ```bash
    yarn add -D electron-builder
    ```

## CLI

Ref : [electron-builder Command Line Interface (CLI)](https://www.electron.build/cli)

```bash
electron-builder build  # Build
electron-builder install-app-deps # Install appdeps
```

`insatll-app-deps`は、インストールされている ELectron のバージョンに従って、依存する Native モジュールをインストールする。`package.json`の`scripts`に以下を足せば事足りる。

```json title="package.json"
"scripts": {
  // yarn install実行後に自動で呼ばれる
  "postinstall": "electron-builder install-app-deps"
}
```

## Configuration

Ref : [electron-builder Common Configuration](https://www.electron.build/configuration/configuration)

`package.json`の`build`内、もしくは`electron-builder.yml`に記述します。

### mac

-   `category` : Mac アプリのカテゴリ（[参照](https://developer.apple.com/library/ios/documentation/General/Reference/InfoPlistKeyReference/Articles/LaunchServicesKeys.html#//apple_ref/doc/uid/TP40009250-SW8)）
-   `target` : パッケージタイプ（dmg, mas, pkg...）
-   `identity` : 署名時に利用する証明書名
-   `icon` : アイコン`icon.icns`へのパス
-   `darkModeSupport` : ダークモードがサポートされているか

#### dmg

-   `contents` :

### win

-   `target` : パッケージタイプ（msi, nsis...）
-   `icon` : アイコン`icon.ico`へのパス

## Example

```yml
productName: "ElectronApp"
appId: "com.example.app"
files:
    - "build/"
directories:
    output: "release"
win:
mac:
dmg:
linux:
```

## Icons

## Auto Update

## References

-   [electron-builder](https://www.electron.build/)
