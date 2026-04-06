---
title: "Factors to Consider When Choosing a Localization Solution for Unity"
source: "https://medium.com/pocket-gems/factors-to-consider-when-choosing-a-localization-solution-for-unity-a7e1323569c5"
author:
  - "[[Pocket Gems]]"
published: 2022-06-17
created: 2026-04-06
description: "Factors to Consider When Choosing a Localization Solution for Unity By Michael Chrien Here at Pocket Gems, we recently released Adventure Chef: Merge Explorer in nine different languages. So, we …"
tags:
  - "clippings"
---
[Sitemap](https://medium.com/sitemap/sitemap.xml)

## [Pocket Gems Tech Blog](https://medium.com/pocket-gems?source=post_page---publication_nav-5be33f7840c4-a7e1323569c5---------------------------------------)

[![Pocket Gems Tech Blog](https://miro.medium.com/v2/resize:fill:38:38/1*zbu-FFnTyd1m3OI_KOfjSA.png)](https://medium.com/pocket-gems?source=post_page---post_publication_sidebar-5be33f7840c4-a7e1323569c5---------------------------------------)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*TnID6JWnkkE8k8IfEdCQ2w.png)

Adventure Chef: Merge Explorer

Here at Pocket Gems, we recently released [Adventure Chef: Merge Explorer](https://apps.apple.com/us/story/id1601333351) in nine different languages. So, we wanted to share some of our learnings from localizing the game in Unity and give you some things to keep in mind as you think about sharing your game with a wider audience.

To maximize player engagement and reach a wider audience, every mobile game should take localization into account during development. Localization is the process of changing text, numerals, images, and other assets in software to make it readable and culturally appropriate for different languages.

Before implementing localization, you should consider the following questions for your game.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*fbyna77Rp-MNIehO)

A map view in Japanese

## What Assets Are You Localizing?

The scope of what you are localizing in your game will impact your approach. At a minimum, you will want to be able to localize strings in your game. Usually this entails a lookup table with a key that’s standard across all languages. Depending on the current language of your game, that key might return a different string value from the table. Are you dynamically substituting or combining strings in your code? You will need to support string substitution and additional context metadata for your table. For string substitution, you can get by with \` [String.Format](https://docs.microsoft.com/en-us/dotnet/api/system.string.format?view=net-6.0) \` in a pinch, but depending on the string and data in the string, you might need to support [additional formatting](https://docs.unity3d.com/Packages/com.unity.localization@1.0/manual/Smart/SmartStrings.html) to properly convey ideas such as gender or amount. Context information is important for the translator of your strings. Different languages might handle certain situations differently depending on how they appear in the game or which character the text is coming from. Providing general information around how the string is being used, who is saying it, their gender, amount, or other information can be invaluable for a translator to properly generate a translation that makes sense for your game.

Are you displaying numbers, currency, or dates? C# includes functionality for handling this, but you need to make sure that you are using the correct [CultureInfo](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo?view=net-6.0) before calling functions that use it. On different platforms, [CultureInfo.CurrentCulture](https://docs.microsoft.com/en-us/dotnet/api/system.globalization.cultureinfo.currentculture?view=net-6.0) will [not necessarily return](https://issuetracker.unity3d.com/issues/en-us-is-always-returned-when-calling-globalization-dot-cultureinfo-dot-currentculture-even-though-the-system-language-is-different) the actual CultureInfo of the device due to Unity’s implementation of Mono. You will need to create a native plugin to get the proper CultureInfo using platform-specific APIs and update the value accordingly. You will also want to make sure that if you are developing for different platforms that you are getting the proper display language from the device. For example, iOS devices have a setting for the device’s region (which includes culture), but a separate override for their preferred language.

Are you interfacing with any external APIs that might be returning text? Features like in-app stores might require strings from an external service that may or may not be localized and should be accounted for when localizing items. If it is localized, how is that service determining which language to use? You will also need to support internal Unity project settings strings that are part of the build. Strings like your app name, description, or feature request descriptions are not necessarily localized — you might need to add support for that.

Are you displaying numbers or text in any assets such as images, textures, or visual effects? You will likely want to localize those as well. You could separate the string from the image, and overlay a separate component to display the string as if it is part of the image. If that is not possible, you could generate a separate lookup table for other assets, but be aware of the memory and performance impact of that solution.

Do you have any Google Play or App Store pages, websites, screenshots, or other marketing materials? It is great that you took the time to localize your game, but when people land on the page to download or purchase it and do not understand it, you have lost a potential player who might have been floored by your amazing in-game translation. A user’s first impression on the page before they acquire the game is just as important, so don’t focus solely on in-game translations.

## Get Pocket Gems’s stories in your inbox

Join Medium for free to get updates from this writer.

Lastly, do you have other assets that might need to be culturally modified? A character waving at another character might not be interpreted the same way by all players across the world. Audio, animations, models, levels, or game data might need to be swapped depending on the context in-game. Each of those swaps will have an impact on the underlying system and all of the testing and support that such a change involves.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*XJjGnp6azkGEsBRE)

A quest description in Spanish

## How Many Languages Are You Supporting?

Each language has their own nuances that need to be accounted for in order to give a culturally appropriate experience. Languages might have different genders for parts of speech and handle quantity differently. It is important that these nuances are captured by your system design and translation. Simply substituting a noun into an already localized string might not reflect the gender or quantity properly in the [surrounding context](https://www.youtube.com/watch?v=OMi6xgdSbMA). Minimizing the combinations of different strings (ideally not having them at all) will allow your game to be properly translated into a variety of languages. If that is not possible, providing enough context to your table metadata will aid your translator.

## Fonts

Make sure the fonts you are using in-game support the languages you are including in your game. [Unicode fonts](https://en.wikipedia.org/wiki/Unicode_font) cannot contain all of the characters for all of the world’s languages as defined by the Unicode font. In practice, you can usually include most of the common characters in a given language family (eg. Latin, Arabic, Cyrillic), but you might need to swap the font or set up a fallback font if you are supporting multiple families. Unity’s Text component and [TextMeshPro](https://docs.unity3d.com/Packages/com.unity.textmeshpro@3.2/manual/FontAssetsFallback.html) both support fallback fonts, but keep in mind that you might need to bundle fonts for families that might not exist on the platform you are developing for. As well, larger character alphabets take up more space and memory, so this should be a consideration when developing for a resource constrained platform. Another option is to just include the glyphs that your game actually uses. TextMeshPro supports modifying a font asset’s [glyph table](https://docs.unity3d.com/Packages/com.unity.textmeshpro@4.0/manual/FontAssetsProperties.html#character-table), so you can only include the glyphs from a given font that your game needs.

## Display

Another consideration is how the language is displayed. Some languages are read in different directions, so do not assume all languages are read from left to right, top to bottom. This might impact how you render and lay out the text in your game. Monospaced fonts or languages with a lot of characters per word (such as German) might cause your text rendering components to overflow. Having a “fake language” that adds random characters to your English translation allows you to quickly verify any text that needs to be localized as well as help you catch any overflows before your translations get back from the translator. If you do find overflowing translations, update your text components to either autosize your fonts, or dynamically increase the size of the text if your layout allows it.

## How Does Localization Impact Your Game’s Performance?

When evaluating your localization implementation, be cognizant of the impacts of that feature on your game’s size, memory usage, performance, and remote content.

## App Size

Including fonts in your game’s build may increase the size of the game. If that’s an issue, you could download the font when required, but you are preventing the player in those languages from playing the game until they do. You could also use system fonts instead of bundling a new font, but it might not look the same as your game’s font, it might not exist on all devices you are targeting, and there might be a memory impact to loading that system font.

## Data Organization

Are you storing all of your translations in a single table or are you planning on using several smaller tables (per language or even per feature)? How do you allow your translations to be updated post-release? How are you managing all of those different tables and developing an API that is easy to use to access those tables? These questions can only be answered for your specific project, platform, and needs, but you should think about these questions before committing to a specific localization solution.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*Wh1_iCtM6NyXkTH6)

An example of a merge tool tip in French

## How Does Localization Impact Your Development Pipeline?

So, you have taken the plunge and are now planning on supporting multiple languages. How do you make it easy to add new strings, send those strings to translators, and then import the translations back in-game? The general developer flow from the packages we investigated was that the developer first adds an English string to the table, then on the component that is displaying the string, you select that string’s key from a dropdown. That might not work for your team — we felt that flow introduced too much friction into the development process, so we created tools to automate parts of it.

Some packages have auto-localization features which send your English strings to an online translation service and autofill the rest of the languages with those translations, but from caveats described earlier, these translations likely will not convey the nuance of the context of the string and may not properly handle substitutions.

Lastly, how does the translation time impact your release cycle? If you are continually releasing updates for your game, you will need to account for translation time and incorporate those translations back into your game before you release your build — or develop a system for remotely delivering those translations to players after the release.

## How Did We Implement Localization?

We evaluated many different Unity localization solutions before choosing one, including [I2-Localization](http://inter-illusion.com/tools/i2-localization/), [LeanLocalization](http://carloswilkes.com/Documentation/LeanLocalization), [Unity’s Localization package](https://docs.unity3d.com/Packages/com.unity.localization@1.0/manual/index.html), and online localization services. Serialization was a large difference between packages. All packages allow importing from CSVs or other other formats, but how that data is serialized in Unity can have a large impact on runtime performance if you are supporting a lot of languages and translations. One solution serialized the translations in a single Game Object, which meant that translations for all languages were loaded into memory at all times.

We ended up using Unity’s Localization Package as it provided an equivalent amount of functionality compared to pay solutions for free. Integration was easier because it is built upon Addressables, which is how we load assets in our game. It includes a “pseudo locale” for testing UI layouts by adding additional characters to the English translation. It has built in exporters and importers for both CSV and Google Sheets, as well as extensible functionality should we choose to manage our translations with an online localization dashboard. There is also support for localizing app descriptions and names which previously just supported English.

On their road map, Unity is actively working on localizing properties within scenes, which should be exciting when it finally goes live. This will allow modification of any serialized property depending on the language selected by the game. Want to change a color based on the language? That functionality should be possible when the update gets in.

We also developed a software layer that wraps Unity’s package and adds our own custom utilities. This allows us to change or update the underlying localization system without impacting the rest of our game code. We created a utility that scans our entire project for tagged localization keys within scripts and Unity assets and automatically adds them to our table. Before a release, we run the utility to add any keys that have been added during the past sprint, and we send those new keys to our translation team. Once the translations are complete, we import them into the game. This workflow allows artists and designers to avoid maintaining localization keys during development. For translations that might take longer than usual, our remote content system allows us to update those tables when they’re ready without needing to wait for a new app release.

With this implementation we feel that Adventure Chef: Merge Explorer has a good framework for supporting different languages moving forward. If you are curious about learning more about Unity’s localization package, we would suggest watching [this overview](https://www.youtube.com/watch?v=qmpswjJuhoc) and digging into the package’s [documentation](https://docs.unity3d.com/Packages/com.unity.localization@1.0/manual/index.html) to see if it fits your project’s needs.