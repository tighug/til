# Storybook

Storybook は UI 開発のためのツールです。

## Installation

```bash
npx sb init
```

## CLI

### `start-storybook`

```bash
# Start in dev mode
yarn start-storybook [options]
```

- `-p [number]`: ポート番号
- `-h [string]`: ホスト
- `-s [dir-names]`: 静的ファイルのディレクトリ
- `--debug-webpack`: 最終的な webpack 設定を表示（debug 用）
- `--docs`: ドキュメントモードを有効にする

### `build-storybook`

```bash
yarn build-storybook [options]
```

- `-s [dir-names]`: 静的ファイルのディレクトリ
- `-o [dir-name]`: ビルドファイルの出力先ディレクトリ
- `-w`: ウォッチモードを有効にする
- `--debug-webpack`: 最終的な webpack 設定を表示（debug 用）
- `--docs`: ドキュメントモードを有効にする

## Usage

```ts
import React from "react";
import { Story } from "@storybook/react";
import { Button, ButtonProps } from "./Button";

export default {
  title: "Button",
  component: Button,
};

const Template: Story<ButtonProps> = (args) => <Button {...args} />;
export const Primary = Template.bind({});

Primary.args = {
  primary: true,
  label: "Primary",
};
```

## Addons

### Storybook Essentials

```bash
yarn add -D @storybook/addon-essentials
```

以下のアドオンが含まれています。

- Actions (`@storybook/addon-actions`)
- Backgrounds (`@storybook/addon-backgrounds`)
- Controls (`@storybook/addon-controls`)
- Docs (`@storybook/addon-docs`)
- Viewport (`@storybook/addon-viewport`)
- Toolbars (`@storybook/addon-toolbars`)

## Configuration

`.storybook/`内に記述します。

### `main.js`

```js
module.exports = {
  stories: [""], // ストーリーファイルの場所
  addons: [], // 使用するアドオンのリスト
  // webpackのカスタム構成
  webpackFinal: (config) => {
    config.plugins.push(...);
    return config;
  },
  // babelのカスタム構成
  babel: async (options) => ({
    ...options,
    // any extra options you want to set
  }),
};
```

### `manager.js`

```js
addons.setConfig({
  isFullscreen: false, // フルスクリーン表示
  showNav: true, // navパネルを表示
  showPanel: true, // addonパネルを表示
  panelPosition: "bottom", // addonパネルの位置
  enableShortcuts: true, // ショートカットを有効にする
  isToolshown: true, // ツールバーを表示
  theme: undefined, // 適用するtheme
  selectedPanel: undefined, //
  initialActive: "sidebar", // モバイル時、デフォルトで有効なタブ
  sidebar: {
    showRoots: false, // ルートレベルのノードを表示
    collapsedRoots: ["other"], // デフォルトで畳むノード
    renderLabel: (item) => <abbr title="...">{item.name}</abbr>,
  },
});
```

### `preview.js`

```js
import React from "react";
import { ThemeProvider } from "styled-components";

// すべてのストーリーをラップするデコレーター
export const decorators = [
  (Story) => (
    <ThemeProvider theme="default">
      <Story />
    </ThemeProvider>
  ),
];

// すべてのストーリーのパラメーター
export const parameters = {
  backgrounds: {
    values: [
      { name: "red", value: "#f00" },
      { name: "green", value: "#0f0" },
    ],
  },
};

export const globalTypes = {
  theme: {
    name: "Theme",
    description: "Global theme for components",
    defaultValue: "light",
    toolbar: {
      icon: "circlehollow",
      items: ["light", "dark"],
    },
  },
};
```

## References

- [Storybook](https://storybook.js.org/)
