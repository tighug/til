# Meleon UI

## Features

- Material Design
- Support for theming

## Competitors

| library                                                                               | styling           | testing                                            |
| ------------------------------------------------------------------------------------- | ----------------- | -------------------------------------------------- |
| [Material-UI](https://github.com/mui-org/material-ui)                                 | emotion           | chai, karma, mocha                                 |
| [React-Bootstrap](https://github.com/react-bootstrap/react-bootstrap)                 | bootstrap         | chai, enzyme, karma, mocha, sinon                  |
| [Blueprint](https://github.com/palantir/blueprint)                                    | scss              | chai, enzyme, karma, mocha, sinon, testing-library |
| [chakra ui](https://github.com/chakra-ui/chakra-ui/)                                  | emotion           | jest, storybook                                    |
| [Semantic UI React](https://github.com/Semantic-Org/Semantic-UI-React)                | css               | chai, cypress, enzyme karma, sinon                 |
| [Evergreen](https://github.com/segmentio/evergreen/)                                  | glamor            | storybook, testing-library, enzyme, sinon          |
| [reactstrap](https://github.com/reactstrap/reactstrap)                                | bootstrap         | enzyme                                             |
| [Rebass](https://github.com/rebassjs/rebass)                                          | styled-system     | jest                                               |
| [Grommet](https://github.com/grommet/grommet)                                         | styled-components | jest, storybook, testing-library                   |
| [React Suite](https://github.com/rsuite/rsuite)                                       | less              | chai, karma, mocha, sinon                          |
| [Ant Design](https://github.com/ant-design/ant-design/)                               | less              | enzyme, jest                                       |
| [React Data Table Component](https://github.com/jbetancur/react-data-table-component) | styled-components | testing-library, jest                              |
| [Pal.js UI](https://github.com/paljs/ui)                                              | styled-components | -                                                  |
| [grape-ui](https://github.com/napagroup/grape-ui-react)                               | styled-components | jest, testing-library, storybook                   |

## Components

> Vuetify, Material-UI

- Alerts
- Application
- Aspect ratio
- Avatars
- Badges
- Banners
- Bars
  - App bars
  - Toolbars
  - System bars
- Bottom navigation
- Bottom sheets
- Breadcrumbs
- Buttons
- Calendars
- Cards
- Carousels
- Chips
- Dialogs
- Dividers
- Expansion panels
- Footers
- Form inputs & controls
  - Autocompletes
  - Checkboxes
  - Combobox
  - File inputs
  - Forms
  - Inputs
  - Overflow buttons
  - Radio buttons
  - Range sliders
  - Selects
  - Sliders
  - Switches
  - Textareas
  - Text fields
- Grid system
- Groups
  - Button groups
  - Chip groups
  - Item groups
  - List item groups
  - Slide groups
  - Windows
- Hover
- Icons
- Images
- Lazy
- Lists
- Menus
- Navigation drawers
- Overlays
- Pagination
- Parallax
- Pickers
  - Color pickers
  - Date pickers
  - Time pickers
- Progress
  - Progress circular
  - Progress linear
- Ratings
- Sheets
- Skeleton loaders
- Snackbars
- Sparklines
- Steppers
- Subheaders
- Tables
- Tabs
- Timelines
- Tooltips
- Treeview
- Virtual scroller

## Dependencies

- React
  - `react`：本体
  - `react-dom`：DOM レンダリングのための API
  - `react-is`：特定の React 要素であるかを判定する API
- Styled Components
  - `styled-components`：本体
- Others
  - `classnames`：条件からクラスネームを生成する API
  - `meleon-palette` : カラーパレット

## Dev Dependencies

### Type Checking

- TypeScript
  - `typescript`：本体
  - `ts-node`：コンパイルと実行を同時に行うコマンド

### Lintting & Formatting

- Prettier
  - `prettier`：本体
- ESLint
  - `eslint`：本体
  - `eslint-plugin-prettier`：Prettier と併用するプラグイン
  - `eslint-config-prettier`：Prettier と併用する時の設定
  - `@typescript-eslint/eslint-plugin`：TypeScript と併用するプラグイン
  - `@typescript-eslint/parser`：TypeScript と併用するパーサー
  - `eslint-plugin-react`：React と併用するプラグイン
- Stylelint
  - `stylelint`：本体
  - `stylelint-config-recommended`：推奨設定
  - `stylelint-order`：記述順序ルールの導入
  - `stylelint-config-recess-order`：twitter/recess の記述順序設定
  - `stylelint-prettier`：Prettier と併用するプラグイン
  - `stylelint-config-prettier`：Prettier と併用する時の設定

### Testing

- Jest
  - `jest`：本体
  - `jest-styled-components` : Styled Component 用のカスタムマッチャー
  - `@types/jest`：TypeScript 用の型定義
  - `ts-jest`：TypeScript で書かれたテストのトランスフォーマー
- React Testing Library
  - `@testing-library/react`：本体
  - `@testing-library/jest-dom` : 追加のカスタムマッチャー
- Storybook
  - `@storybook/react`：React 用の Storybook 本体
  - `@storybook/addon-essentials`：必須のアドオン
  - `@storybook/addon-postcss` : postcss のアドオン

### CI

- `semantic-release`

## Workflow

ブランチモデル ：GitHub Flow

1. `main`ブランチから`topic`ブランチをチェックアウト
2. `topic`ブランチをプッシュ
3. PR を作成
4. ★ テストを実行
5. `main`ブランチにマージ
6. ★ `main`ブランチにタグ付け
7. ★ タグをもとにリリースを作成
8. ★ NPM ライブラリに公開
9. ★ GitHub Pages に公開
