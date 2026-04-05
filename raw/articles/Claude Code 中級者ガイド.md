---
title: "Claude Code 中級者ガイド"
source: "https://zenn.dev/medicalforce/articles/8bc0b6afbbb8a7"
author:
published: 2025-06-17
created: 2026-04-05
description:
tags:
  - "clippings"
---
627

326

こんにちは、Gatsbyです。  
`Claude` やばいですね、シンギュラリティを感じます。  
早く使いこなせる様にならないとやばいと焦る日々を送ってますが、キャッチアップしたくても **公式ドキュメントがかなり分厚いし、 `Claude` の情報が散乱** してるので、自分なりにまとめてみました！  
この記事では、自分がキャッチアップした情報を基に **`Claude　Code` 中級者への最短距離を説明しています** （各機能の詳細は別記事で説明します）。  
皆さんの一助になれば幸いです 🙇

## インストールと初期セットアップ💻

1. `Claude Code` をインストールします。
	```
	npm install -g @anthropic-ai/claude-code
	```
2. `claude` を起動します。セッションが開始されます。
	```
	claude
	```
3. まずはプロジェクトの要約をさせます。
	```
	> summarize this project
	```
	このステップは非常に重要です。 `Claude` が現状のコード、ディレクトリ構成、技術スタックなどを正確に理解することで、後続のタスクにおける **回答精度が飛躍的に向上** します。 **これはベストプラクティスです** 。
4. `/init` コマンドで `CLAUDE.md` ファイルを作成させます。
	```
	> /init
	```
	先ほど要約した内容を `CLAUDE.md` に書き出してくれます。  
	**`CLAUDE.md` は `Claude` のセッション起動時に読み込まれるメモリ** です。

参照： [Initialize your project - Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/setup#initialize-your-project)

これで初期セットアップは完了です。この状態でも `Claude` は十分な力を発揮しますが、 **中級者としてさらに精度を向上させるには、これから紹介するチューニングやコツが必要** になってきます。

## 精度を劇的に向上させるベストプラクティス

誰でも今日から実践できる、 `Claude` の精度を上げるためのTipsを紹介します。

## CLAUDE.mdでコンテキストを永続化する

**`Claude` のセッションはステートレス** です。つまり、一度セッションを終了すると、そこでの会話内容はメモリから消えてしまいます。当然、セッションごとにプロジェクトのコードやディレクトリ構成、技術スタックなどの情報もリセットされます。

そこで、 **常に参照させたい、またはセッションを跨いで記憶させておきたい情報は、 `/init` コマンドで作成した `CLAUDE.md` に記載しましょう。** `CLAUDE.md` は、新しいセッションが開始されるたびに自動的に読み込まれるため、 `Claude` は常に最新のプロジェクトコンテキストを把握できます。

しかし、コンテキストをゼロから記述するのは大変なので、公式のサンプルプロンプトを活用し効率的に `CLAUDE.md` を充実させましょう。以下は、日本語で出力するように少しチューニングを加えたプロンプト例です。

```
> what does this project do?, and write it in Japanse in CLAUDE.md
> give me an overview of this codebase, and write it in Japanse in CLAUDE.md
> what technologies does this project use?, and write it in Japanse in CLAUDE.md
> explain the main architecture patterns used here, and write it in Japanse in CLAUDE.md
> where is the main entry point?, and write it in Japanse in CLAUDE.md
> explain the folder structure, and write it in Japanse in CLAUDE.md
> analyze the database schema, and write it in Japanse in CLAUDE.md
> what are the key data models?, and write it in Japanse in CLAUDE.md
> how does error handling work in this app?, and write it in Japanse in CLAUDE.md
> how is authentication handled?, and write it in Japanse in CLAUDE.md
```

参照：

- [Ask your first question - Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/quickstart#step-2%3A-ask-your-first-question)
- [Understand new codebases - Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/common-workflows#understand-new-codebases)

## プロンプトに大量のテキストを入力しない

どうやら、プロンプトに大量のテキストを直接入力すると、 `Claude` は処理に苦戦するようです。  
これはLLMの特性によるものです。  
なので、 **大量の指示や設定をしたい場合は、ファイルに記述し読み込ませましょう** 。効率的に処理し、より良い回答を生成できます。

参照： [Handling large inputs - Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/setup#handling-large-inputs)

## ultrathink

`Claude` には、その思考の深さを制御する概念が存在します。特定の単語を使用することで、消費トークンは増えますが、より深く思考し、回答の精度を高めることができます。  
**Maxプランならどれだけトークンを消費しても値段は変わらないので常に `ultrathink` がおすすめです。**

- `think` (上限4,000トークン)
- `think hard` (上限10,000トークン)
- `think harder` (上限31,999トークン)
- `ultrathink` (上限31,999トークン)

上記のように、思考深度は `ultrathink` が最も深く、複雑な問題に対してより質の高い回答を得たい場合に有効です。

**※補足**  
**ちなみに、これは公式ドキュメントには記載されていません** 。 `@anthropic-ai/claude-code` の `cli.js` に直接記述されています。  
確認手順は以下です。

1. `Claude Code` のインストールパスに移動  
	自分は `bun` を使っていますが、 **npm, anyenvなどを使っている場合は、 `which claude` でインストールパスをご確認ください** 。
	```
	cd ~/.bun/install/global/node_modules/@anthropic-ai/claude-code
	```
2. minifyを元に戻す  
	当前ですが、パッケージとして配布されてるので **そのままだと `minify` されていて見にくい** です。  
	`prettier` でフォーマットしましょう。
	```
	bunx prettier --write cli.js
	```
3. お好みのエディタで開いて検索  
	自分は `Cursor` 使ってるので以下コマンドでファイルを開いています。  
	**お好みのエディタで開いていただいて、あとは `cmd + F` で `ultrathink` で検索してご確認いただけます** 。
	```
	cursor cli.js （ここからは cmd + F で ultrathink と検索をかけてください。）
	```

念の為、バージョン `1.0.29` （2025-06-20日時点） でのコードのスクショを置いておきます。

![](https://storage.googleapis.com/zenn-user-upload/2fcdc3b39868-20250620.png)

参照： [https://simonwillison.net/2025/Apr/19/claude-code-best-practices/](https://simonwillison.net/2025/Apr/19/claude-code-best-practices/)

## Explore, Plan, Code, Commit

`Claude` は特定の `Workflow` に依存することなく柔軟に指示ができる反面、 **フワッとした指示だと変に行間を読んで明後日の方向に進んでしまいます** 。  
より良い精度と確実なアウトプットを得るには、 **いきなりタスク実装を投げるのではなく、コード理解、設計、実装、コミットの順番で命令を実行** することがベストプラクティスとされています。

1. **Explore**  
	まずはコードベースや関連ファイルなどを理解させるフェーズ。
	```
	> find the files that handle user authentication
	```
2. **Plan**  
	実装の計画や設計について深く考えさせるフェーズ。  
	ここで `ultrathink` を使うと効果的です。
	```
	> ultrathink how to implement Role Based User Authentication
	```
3. **Code**  
	計画に基づき、具体的なコード実装を依頼するフェーズ。
	```
	> implement its solution
	```
4. **Commit**  
	実装された変更内容をコミットさせるフェーズ。
	```
	> commit this
	```

このように、段階を踏みながら命令をすることで、精度が劇的に向上します。

参照： [Explore, Plan, Code, Commit - Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-best-practices#a-explore-plan-code-commit)

## TDD（テスト駆動開発）

`TDD` の説明は省きます。  
`TDD Workflow` は `Anthropic` お墨付きのワークフローです。

1. テストの実装を命令  
	まずは、 **実装したい機能のテストコードを `Claude` に実装させ** 、それをコミットします。  
	このテストは、最初は失敗するように（機能が未実装なので）なります。
2. テストをパスする実装を命令  
	次に、 **テストコードを修正せずに、そのテストがパスするように実装コードを書くよう `Claude` に命令** します。  
	こうすることで、アウトプットのブレが格段に少なくなります。

良さげのプロンプトがあったので貼っておきます。

<iframe src="https://embed.zenn.studio/tweet#zenn-embedded__65daf7e9f8f8e" frameborder="0" height="48"></iframe>

## /clear

セッション内での会話が長くなると、 `Claude` がこれまでの会話の流れに引き摺られ、 **文脈を誤解したり、変な回答をすることがあります** 。  
そう感じた際は、プロンプトで `/clear` コマンドを実行することで **これまでの会話をリセット** できます。

## claude --resume

一度閉じたけどやっぱりこのセッションを再開したい・・・ってことありませんか？  
例えば、割り込みタスクのために起動中のセッションを閉じて、別ブランチに切り替えて新しくセッションを立ち上げ、割り込みタスクが終われば元のブランチに戻って・・・などなど。

その際に便利なオプションが `--resume`, `-r` です。  
このオプションを実行すると、 **過去のセッション（公式ドキュメントでは `conversation` と表現されています）の一覧が表示** されます。戻りたいセッションを選ぶことでセッションを再開できます。

```
claude --resume
```

過去のセッションが何日前まで保存されるかについては、分かりませんでした。。。

参照： [Resume previous conversations - Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/common-workflows#resume-previous-conversations)

## 処理完了を通知させる

`Claude` は複雑なタスクを実行する際に、平気で10分、20分と処理を続けたり、時には沈黙したりすることがあります。これでは「いつ終わるのか」が分からず、作業効率が落ちてしまいます。

**タスク完了後に通知を受け取る設定** をしておきましょう。

```
claude config set --global preferredNotifChannel terminal_bell
```

参照： [Notification setup - Anthropic Docs](https://docs.anthropic.com/en/docs/claude-code/setup#notification-setup)

## npx ccusage

毎日どれだけ `Claude` を使い倒してるか気になりませんか？自分は気になります！  
元を取りたいので、最近はどれだけ酷使できるかを日々模索しながら使ってます（本末転倒）。  
このコマンドを実行することで、 **日々のトークン使用量や、もし従量課金だった場合の課金額を確認できます** 。

```
npx ccusage
```

毎日の使用状況をチェックして、ニヤニヤしながら効率的な利用を目指しましょう！

参照： [Claude Codeの使用料金を可視化するCLIツール「ccusage」を作った](https://zenn.dev/ryoppippi/articles/6c9a8fe6629cd6)

## その他Pro tips

その他、ここには挙げていませんが、細かいテクニック集は以下をご確認ください。

上記以外にも、 `Claude Code` を使いこなすための細かいテクニック集が公式ドキュメントで公開されています。ぜひこちらも確認して、 **Claude玄人(笑)** になりましょう 💪

<iframe src="https://embed.zenn.studio/card#zenn-embedded__e6bab34ab49b5" frameborder="0" height="122"></iframe>

<iframe src="https://embed.zenn.studio/card#zenn-embedded__92a32823865a1" frameborder="0" height="122"></iframe>

<iframe src="https://embed.zenn.studio/card#zenn-embedded__7e024cc2b117f" frameborder="0" height="122"></iframe>

## まとめ

これで皆さんも `Claude Code` 中級者ですね！  
今回紹介したベストプラクティスを意識し、 `CLAUDE.md` でのメモリ管理、段階的なワークフロー、TDDの実践、そして設定のチューニングなどを活用して、 **Claude玄人(笑)** になりましょう 👴

P.S. 『Claude Code 玄人ガイド』作成中です笑

627

326