---
title: "Translator++ Ver. 6.12.26 - A blazingly fast Ruby based RPG Maker parser!"
source: "https://www.patreon.com/posts/translator-ver-6-118932228"
author:
  - "[[Dreamsavior]]"
published: 2024-12-30
created: 2026-04-06
description: "Dreamsaviorのコンテンツをさらに楽しみましょう"
tags:
  - "clippings"
---
3日早く会員に公開されました。

![](https://c10.patreonusercontent.com/4/patreon-media/p/post/118932228/619faf0dd865431ca6e65ae3e983db40/eyJ3IjoxMDgwfQ%3D%3D/1.jpg?token-hash=5_PAQg8akZfoo9ylcNVoFDgYMWvMl6yj_ceHcGo8i74%3D&token-time=1776729600) ![](https://c10.patreonusercontent.com/4/patreon-media/p/post/118932228/619faf0dd865431ca6e65ae3e983db40/eyJ3IjoxMDgwfQ%3D%3D/1.jpg?token-hash=5_PAQg8akZfoo9ylcNVoFDgYMWvMl6yj_ceHcGo8i74%3D&token-time=1776729600)

### [Dreamsavior](https://www.patreon.com/dreamsavior)

2024年12月30日

2024年12月30日

**Hello fellow translators,**

Influenza type A is currently spreading in my area. I hope all of you are staying healthy.

If you've seen the latest update, version 6.12.26, you might have noticed a new parser for RMRGSS (Ruby-based RPG Maker: RPG Maker XP, VX, and VX Ace). You might be thinking, “Another parser for RPG Maker?”

Well, I hope this new parser will be the **final and ultimate one** for Ruby-based RPG Maker. It’s not only incredibly fast (about **200 times faster** than the previous parser) but also much more reliable.

Before delving into the details, let me share the story behind why there have been so many different parsers for Ruby-based RPG Maker.

### The Challenges of Translating Ruby-based RPG Maker

The key challenge with translating Ruby-based RPG Maker lies in how earlier versions store data—in Ruby’s Marshal format. At the time, JavaScript couldn’t easily handle this format. So, I relied on a third-party tool called [RPGMaker Trans](https://rpgmakertrans.bitbucket.io/index.html), one of the earliest attempts to provide an easy way to translate RPG Maker games.

While innovative, RPGMaker Trans CLI had notable flaws:

- It couldn’t load all translatable text.
- It frequently crashed without providing error messages.

### RMRGSS Parser Ver. 2

To address these limitations, I developed another parser using the much older script called **RVPacker**, created by akesterson, ymaxkrapzv, and BigBlueHat, with a frontend based on [SiCrane’s YAML importer/exporter](https://www.gamedev.net/forums/topic/646333-rpg-maker-vx-ace-data-conversion-utility/).

This tool converted RPG Maker’s Marshal data into editable YAML files—a format Node.js could handle. Thus, **Parser Ver. 2** was born, making the parser based on RPGMaker Trans the **Legacy Parser**.

Because I developed this parser myself, for the first time, Translator++ had full control over the text being loaded. This parser could load all text from RPG Maker games that RPG Maker Trans previously missed. Moreover, there were no more unexplained crashes.

However, this parser had one major flaw: **Node.js’s YAML library is veeeery slow.** While this wasn’t an issue for small games, larger games took hours to parse—clearly not a viable solution.

### Improving the Legacy Parser

Recognizing this limitation, and given that there wasn’t much I could do about Node’s YAML library performance, I revisited the Legacy Parser. By [forking RPGMaker Trans](https://github.com/dreamsavior/rpgmakertrans) and fixing its issues, I achieved the following:

- All game text could now be loaded.
- Progress indicators were added, so users could see whether the parser was still working or had crashed.

However, the parser’s reliance on TCP communication between Ruby and Python created bottlenecks, particularly with files containing many events (like CommonEvents).

### Refining the YAML Parser

Unsatisfied with these results, I revisited **Parser Ver. 2** and optimized it further. By splitting large files (like CommonEvents) into smaller chunks, I enabled multithreaded processing across CommonEvents's events.

Earlier this month, I released an update for Parser Ver. 2 with significant speed improvements. Projects that previously took an hour to process could now be completed in under 10 minutes.

“This is a great achievement,” I thought—until one of my patrons reached out on Discord and demonstrated that very large games still failed to load or took far too long.

At this point, I gave up on Node’s YAML library.

I had to explore alternatives.

### RMRGSS Parser Ver. 3

Then I discovered an alternative: [a TypeScript implementation of Ruby’s Marshal format](https://github.com/hyrious/marshal).

For the first time, Translator++ could natively interact with Ruby’s Marshal format—eliminating bottlenecks caused by YAML libraries and TCP communication. The result? **An incredibly fast parser.**

Here’s a speed comparison:

**Game A:**

A big sized RPG Maker VX Ace game  
![](https://c10.patreonusercontent.com/4/patreon-media/p/post/118932228/6b0ea7b6bf754af899e3cfb9b79eba6f/eyJhIjoxLCJ3Ijo4MjB9/1.jpg?token-hash=fsCmgKsnHKqmx7ic-P3pyRalMeF2TE2mz4BZlFdFT6U%3D&token-time=1776729600)

**Game B:**

Even bigger RPG Maker VX Ace game  
![](https://c10.patreonusercontent.com/4/patreon-media/p/post/118932228/bc23f465babc4cfa95b6a9ac9ef8b073/eyJhIjoxLCJ3Ijo4MjB9/1.jpg?token-hash=rI0bunpZlNMMhLyIdNWDQNRKJwCbXFnksux2Zeb5lJw%3D&token-time=1776729600)

Apparently, the structure of game events significantly affects parsing speed. Although Game B is larger than Game A, **Parser Ver. 3** processed it faster, while **Parser Ver. 2** struggled for over 3 excruciating hours. Given these results, I didn’t dare test it with the Legacy Parser.

### A Fitting Closure

I hope **Parser Ver. 3** will serve as the ultimate solution, fully replacing both the Legacy Parser and Parser Ver. 2.

As we approach 2025, it’s surprising to think I’m still working on parsers for RPG Maker engines that released over 13 years ago.

The **RMRGSS Parser Ver. 3** update is included in Translator++ Version 6.12.26—a perfect way to conclude Version 6.

Stay tuned for even more exciting developments in Translator++ Version 7.

See you next year!

Cheers,  

Dreamsavior

---

### [Dreamsavior](https://www.patreon.com/dreamsavior)

2024年12月30日

2024年12月30日

**Hello fellow translators,**

Influenza type A is currently spreading in my area. I hope all of you are staying healthy.

If you've seen the latest update, version 6.12.26, you might have noticed a new parser for RMRGSS (Ruby-based RPG Maker: RPG Maker XP, VX, and VX Ace). You might be thinking, “Another parser for RPG Maker?”

Well, I hope this new parser will be the **final and ultimate one** for Ruby-based RPG Maker. It’s not only incredibly fast (about **200 times faster** than the previous parser) but also much more reliable.

Before delving into the details, let me share the story behind why there have been so many different parsers for Ruby-based RPG Maker.

### The Challenges of Translating Ruby-based RPG Maker

The key challenge with translating Ruby-based RPG Maker lies in how earlier versions store data—in Ruby’s Marshal format. At the time, JavaScript couldn’t easily handle this format. So, I relied on a third-party tool called [RPGMaker Trans](https://rpgmakertrans.bitbucket.io/index.html), one of the earliest attempts to provide an easy way to translate RPG Maker games.

While innovative, RPGMaker Trans CLI had notable flaws:

- It couldn’t load all translatable text.
- It frequently crashed without providing error messages.

### RMRGSS Parser Ver. 2

To address these limitations, I developed another parser using the much older script called **RVPacker**, created by akesterson, ymaxkrapzv, and BigBlueHat, with a frontend based on [SiCrane’s YAML importer/exporter](https://www.gamedev.net/forums/topic/646333-rpg-maker-vx-ace-data-conversion-utility/).

This tool converted RPG Maker’s Marshal data into editable YAML files—a format Node.js could handle. Thus, **Parser Ver. 2** was born, making the parser based on RPGMaker Trans the **Legacy Parser**.

Because I developed this parser myself, for the first time, Translator++ had full control over the text being loaded. This parser could load all text from RPG Maker games that RPG Maker Trans previously missed. Moreover, there were no more unexplained crashes.

However, this parser had one major flaw: **Node.js’s YAML library is veeeery slow.** While this wasn’t an issue for small games, larger games took hours to parse—clearly not a viable solution.

### Improving the Legacy Parser

Recognizing this limitation, and given that there wasn’t much I could do about Node’s YAML library performance, I revisited the Legacy Parser. By [forking RPGMaker Trans](https://github.com/dreamsavior/rpgmakertrans) and fixing its issues, I achieved the following:

- All game text could now be loaded.
- Progress indicators were added, so users could see whether the parser was still working or had crashed.

However, the parser’s reliance on TCP communication between Ruby and Python created bottlenecks, particularly with files containing many events (like CommonEvents).

### Refining the YAML Parser

Unsatisfied with these results, I revisited **Parser Ver. 2** and optimized it further. By splitting large files (like CommonEvents) into smaller chunks, I enabled multithreaded processing across CommonEvents's events.

Earlier this month, I released an update for Parser Ver. 2 with significant speed improvements. Projects that previously took an hour to process could now be completed in under 10 minutes.

“This is a great achievement,” I thought—until one of my patrons reached out on Discord and demonstrated that very large games still failed to load or took far too long.

At this point, I gave up on Node’s YAML library.

I had to explore alternatives.

### RMRGSS Parser Ver. 3

Then I discovered an alternative: [a TypeScript implementation of Ruby’s Marshal format](https://github.com/hyrious/marshal).

For the first time, Translator++ could natively interact with Ruby’s Marshal format—eliminating bottlenecks caused by YAML libraries and TCP communication. The result? **An incredibly fast parser.**

Here’s a speed comparison:

**Game A:**

A big sized RPG Maker VX Ace game  
![](https://c10.patreonusercontent.com/4/patreon-media/p/post/118932228/6b0ea7b6bf754af899e3cfb9b79eba6f/eyJhIjoxLCJ3Ijo4MjB9/1.jpg?token-hash=fsCmgKsnHKqmx7ic-P3pyRalMeF2TE2mz4BZlFdFT6U%3D&token-time=1776729600)

**Game B:**

Even bigger RPG Maker VX Ace game  
![](https://c10.patreonusercontent.com/4/patreon-media/p/post/118932228/bc23f465babc4cfa95b6a9ac9ef8b073/eyJhIjoxLCJ3Ijo4MjB9/1.jpg?token-hash=rI0bunpZlNMMhLyIdNWDQNRKJwCbXFnksux2Zeb5lJw%3D&token-time=1776729600)

Apparently, the structure of game events significantly affects parsing speed. Although Game B is larger than Game A, **Parser Ver. 3** processed it faster, while **Parser Ver. 2** struggled for over 3 excruciating hours. Given these results, I didn’t dare test it with the Legacy Parser.

### A Fitting Closure

I hope **Parser Ver. 3** will serve as the ultimate solution, fully replacing both the Legacy Parser and Parser Ver. 2.

As we approach 2025, it’s surprising to think I’m still working on parsers for RPG Maker engines that released over 13 years ago.

The **RMRGSS Parser Ver. 3** update is included in Translator++ Version 6.12.26—a perfect way to conclude Version 6.

Stay tuned for even more exciting developments in Translator++ Version 7.

See you next year!

Cheers,  

Dreamsavior

---

アプリを使って、すべての投稿をもっと楽しみましょう。