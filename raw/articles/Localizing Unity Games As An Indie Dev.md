---
title: "Localizing Unity Games As An Indie Dev"
source: "https://www.bjmalicoat.com/projects/localizingunitygames"
author:
published:
created: 2026-04-06
description:
tags:
  - "clippings"
---
The source files discussed here are located on the [Bird Cartel GitHub](https://github.com/birdcartel/unity_loc).

I released [Pine Tar Poker](https://pinetarpoker.com/) in English at the end of 2022. I’d never localized a personal project before, but I had experience localizing games and apps professionally. I looked at existing Unity solutions but I couldn’t find exactly what I was looking for.

My ideal setup was one that was equally easy for me as the developer as it would be for a number of translators working async to me. I’m pretty happy with what I ended up with, though there are a few spots that could be smoothed out.

## Translation Side

In my experience translators tend to work out of bespoke translation tools/websites or simple spreadsheets. As primarily a solo developer, I didn’t want to invest in a dedicated tool, so I opted for Google Sheets.

Google Sheets gives me a few really useful features:

- **Scoped write-access per translator, preventing inadvertent edits or leaks.**
- **Version history to review changes.**
- **Ability to quickly generate realistic placeholder text.**
- **Ability to download strings per language from Unity.**

My sheets setup is two-fold. First, I have the main file which is a collated version of all string IDs, descriptions, and translated strings. This file is broken up into a number of referential “export” sheets (tabs at the bottom of the file), one per language. These export sheets have extraneous information like descriptions and comments removed. These export sheets will ultimately produce a key/value file that Unity will use directly, again, one per language.

![](https://www.bjmalicoat.com/img/ptp_loc_gsheets.png "Google Sheet overview") ![](https://www.bjmalicoat.com/img/ptp_loc_export.png "Export sheet overview")

The second set of files are broken-out, writable sheets per language. I invite the translator to this file and it’s basically theirs to party in. Out of caution, I don’t have any direct link from the main file to these files. I’d rather do a one-time update manually when a translator is finished. This lack of linkage can create some problems that I’ll get into in the Issues section.

Before any translators enter the picture, I fill out the string ID, description, and English translation. Then I use the formula `=GOOGLETRANSLATE($B2, "en", "fr")` to generate placeholder text in French for example. I can drag this formula across every cell in the French column and then repeat it for the other languages. **I would never ship this placeholder text**, but it lets me test out basic functionality (e.g. can I even download the French strings) as well as test to make sure my font has the appropriate characters and my UI can roughly accommodate the space required for the new language.

To summarize, once things are setup, a translator can come in and fill out all the cells using the context I provided. Once complete, I paste all those translations into the main file and then download them from Unity.

## Development Side

On the Unity side there are a few key pieces:

- **String Downloader**
- **Font Asset Generation**
- **Localization Manager**
- **Localized Text Mesh**

## String Downloader

Did you know you can write scripts for Google Sheets? You can do powerful collation and calculations and I’m sure lots of other neat stuff! In my case, I simply wanted to expose my strings on a web endpoint. Luckily I found someone [had already written this](https://gist.github.com/dhlavaty/9cb9f50aed62320329636e805e654eae).

![](https://www.bjmalicoat.com/img/ptp_loc_gsheetscripts.png "Google sheets scripts")

Once installed and deployed, you end up with a string like `https://script.google.com/macros/s/[big_guid_string]/exec`. By appending `?sheet=FrenchExport` we can get a JSON payload of our French strings!

```
{
  "data": [
    ["BASIC_TABLE_DEAL_HIT_TARGET", "DISTRIBUER"],
    ["TOP_SCORES_TITLE", "Meilleurs scores"],
    ["HAND_TYPE_PINE_TAR", "PINE TAR"],
    ["HAND_TYPE_PEASANTS", "PAYSANS"],
    ...
  ]
}
```

To keep things simpler in Unity, I use the [SystemLanguage enum](https://docs.unity3d.com/ScriptReference/SystemLanguage.html) when passing around languages. I named my export sheets with the same names so I can easily template in language names to download them:

```
public static void FetchStrings(SystemLanguage language)
{
    string fullUrl = string.Format(baseUrl + "?sheet={0}Export", language);

    UnityWebRequest www = UnityWebRequest.Get(fullUrl);
    request = www.SendWebRequest();

    ...
}
```

Now that we’ve got the JSON strings, we can parse them into CSV and save them in the `Resources` directory. Having the strings is great, but if we just tried to render them, we’d quickly run into issues with Chinese and Japanese. These two popular languages, among others, have characters that aren’t always available in every font. To solve this, we need to know what characters we are using.

![](https://www.bjmalicoat.com/img/ptp_loc_resources.png "CSV Resources in Unity")

## Font Asset Generation

I’m using TextMeshPro, the de facto text rendering component in Unity. TMP uses font assets to know how to render characters from a font. You can give TMP a font and it will generate a texture that it will sample with an [SDF shader](https://steamcdn-a.akamaihd.net/apps/valve/2007/SIGGRAPH2007_AlphaTestedMagnification.pdf) to render the character.

![](https://www.bjmalicoat.com/img/ptp_loc_asset_creator.png "Generating an SDF font asset")

In Latin character set languages, you can get away with not specifying characters to use. However, once you get into Chinese and Japanese and other languages with vast amounts of characters, you don’t really want to pay for the large texture size (and corresponding low resolution characters!). Using Japanese for example, we probably want characters from a [few Unicode ranges](http://www.rikai.com/library/kanjitables/kanji_codes.unicode.shtml). Plugging all that in and letting the Font Asset Creator chew on it to pack an 8K texture, takes 1382578.40ms. I guess TMP thinks it’ll be fast enough to be measured in milliseconds, but that’s more than 23 minutes on my M1 MacBook Pro! The results aren’t great either!

![](https://www.bjmalicoat.com/img/ptp_loc_eightk.png "Huge unusable font atlas")

To get around this, I scan through every character in every language and emit a list of all the used characters. Some characters are used more dynamically, outside of localized strings, so I make sure to add all numbers and the English alphabet in upper and lower case. With that, I can generate a font with just the used characters. With the subset of characters I can generate a 1024x1024 texture in half a second. Milliseconds make sense again!

![](https://www.bjmalicoat.com/img/ptp_loc_usedchars.png "Nice small usable font atlas")

## Localization Manager

Now that we’ve got our strings and our fonts figured out, it’s time to use them. Localization Manager is the script that actually gets and sets the current language. When the language is changed, Localization Manager raises an event for anyone interested. The most interested party is going to be the Localized Text Mesh below.

In addition to handling the current language, Localization Manager also handles the fonts for the languages. Perhaps unsurprisingly, most fonts are written with an audience in mind. It takes work to make a single glyph, so if you have no intention of your font being used in another language, you might avoid supporting it. For us, this means we need to be able to swap fonts based on if characters are present. I like to use Google Fonts to both find fonts I like and also to test which characters they have.

Take a look at this font [Rubik when we try to preview Japanese](https://fonts.google.com/specimen/Rubik?preview.text=%E8%A6%8B%E3%81%A4%E3%81%8B%E3%82%8A%E3%81%BE%E3%81%9B%E3%82%93&preview.text_type=custom&query=rubik):

![](https://www.bjmalicoat.com/img/ptp_loc_squares.png "Missing characters")

Ahh the dreaded □□□□□. If we’re not careful, □□□□□ will hit us in Unity too. Let’s try to make a font asset using Japanese characters and the Rubik font in Unity.

![](https://www.bjmalicoat.com/img/ptp_loc_unitymissing.png "Missing characters in Unity font")

At least TMP is kind enough to tell us **Missing characters: 492**. If that number is above 0, you might be headed for the land of □□□□. You can configure a fallback font in TMP (`Edit> Project Settings> TextMesh Pro> Settings`), but that means you can’t control the look of your game. Personally, I’d rather pick a font I know has the characters I need. If you’re dealing with any user-generated input (e.g. someone can enter their name), you won’t be so lucky and you’ll probably want a fallback font.

Once we have fonts that match our character sets, we can use Localization Manager to assign them to the languages we support.

![](https://www.bjmalicoat.com/img/ptp_loc_manager.png "Assigning fonts")

You’ll notice we only actually use two fonts. One for Japanese and Chinese and then another for all other languages. You might be able to find fonts that have everything you need, but if not, it’s nice to have the flexibility to assign per language. **Update**: [Raymonf on Hacker News](https://news.ycombinator.com/item?id=34730792) mentioned you should **not** use one font for Japanese and Chinese and included this [helpful link](https://heistak.github.io/your-code-displays-japanese-wrong/) as to why.

If your game uses world-space (3D) Text Mesh Pro components and UI-space (Canvas) Text Mesh Pro components, [there’s some interesting behavior to be aware of](https://forum.unity.com/threads/tmpro-text-is-not-visible-on-a-device.636085/). For this reason, the setup in Pine Tar Poker uses two font assets per language, one for the world-space text and one for the UI-space text. I believe I could get away with just having separate materials, but I don’t have a device that exhibits the missing text issue caused by using the same material, so I can’t verify that myself!

![](https://www.bjmalicoat.com/img/ptp_loc_ui_manager.png "UI Fonts require more fonts...")

## Localized Text Mesh

To recap, we’ve downloaded our strings, ensured we can render them, and we’re aware of the current language. The final piece of the puzzle is to inject our localized strings into a TextMeshPro component. For this, I made a simple script called LocalizedTextMesh that handles looking up the string and font asset for the current language in addition to listening for language changes. There are a few ways this component is used.

### Static String

This is the most straight-forward usage and usually used for something like a label. If we have the word `History`, we can just slap a LocalizedTextMesh component on that game object and feed it `MAIN_MENU_HISTORY` or whatever our string ID is. Now the string is correct in all languages.

![](https://www.bjmalicoat.com/img/ptp_loc_textmesh.png "Static usage of Localized Text Mesh")

### Formatted String

Often times you need to format in values and the positions of those values change based on the language. To support this, LocalizedTextMesh has a parameters option that takes a set of strings to format into the value retrieved from the passed in string ID. Here we see the text `{0} LEFT` localized to `还剩 {0}次` for Simplified Chinese. We can pass in the value of 2 to produce the desired result.

![](https://www.bjmalicoat.com/img/ptp_loc_formatter.png "Formatted localized string")

### Dynamic String

Sometimes you just want to come up with a string based on some logic and then display it. For that reason, `LocalizedTextMesh` has a `SetText` method. Additionally, `LocalizationManager` allows programmatic lookup by string ID as well for cases where you want to have the localized string and set it into a TextMeshPro component yourself. Here’s an example where we show whether sound effects are on or off:

```
if (Player.Instance.SFXOn)
{
    m_text.SetText("SETTINGS_SFX_ON");
}
else
{
    m_text.SetText("SETTINGS_SFX_OFF");
}
```

I originally designed `LocalizedTextMesh` as a drop in replacement, but I opted for a `SetText` method so it was easy to search for localized and unlocalized situations. Searching `.text = "` would show me all cases where I’m setting text on a TextMeshPro component directly.

## Issues

A few things I’d like to improve over time:

It’d be nice if the Download Strings context menu also generated the used characters and saved a new font asset.

There are a lot of sheets to juggle when you have the main sheet + one more per language. If I add a new string, I have to remember to add it to all the sheets, this is error prone but it’s a trade-off of protecting the main sheet from errant translator edits. I’m guessing there is some referential way to do it though…

When I was using Unity at Microsoft, one of the perf guidelines was to serialize references at editor-time, hence LocalizedTextMesh takes a TextMeshPro reference instead of finding it at startup time. I’m not sure if the guideline is still true 8 years later, but I still do it which means when you add a LocalizedTextMesh you have to take an extra two seconds to add the reference. Additionally, LocalizedTextMesh doesn’t `RequireComponent` of a TextMeshPro since I’m not sure if you’re using UI-space or world-space text, there goes another two seconds!

## Additional Thoughts

## App Store Screenshots

I wrote an editor tool to take screenshots and made it “loc-aware”, so now I can generate 3 different resolutions across 8 languages with 1 click!

![](https://www.bjmalicoat.com/img/ptp_loc_screenshots.gif "GIF of the same screen cycling through multiple languages")

## Localization Guide

Note: There are some spoilers in the Localization Guide 👀

I put together a [Localization Guide](https://docs.google.com/presentation/d/1b8QwWIaT3apNPj4s_fOoBxqgTW0V-IaM1OjmhnCiXY0/edit?usp=sharing) based on nothing other than empathy for translators who see a single cell in a spreadsheet and are expected to make great choices with no context. The translators I worked with who were used to that single cell context seemed to appreciate this slide show and I think it resulted in higher quality translations that captured my intent and tone more. I also sent each translator an iOS or Android code so they could experience the game in English.

## Sourcing Translators

There are many translation services available. For this experiment, I opted to find translators on [fiverr.com](https://fiverr.com/). The main benefit for me was talking directly to the people who are doing the translation and making sure we’re on the same page. The downside is the time spent getting on the same page is multiplied by the number of translators. Presumably a translation service would have one liaison who effectively builds and communicates the same Localization Guide amongst their team of translators… though maybe that’s not how it always works.

I was pretty happy with the results of fiverr. I may have been lucky and found quality people or maybe because I’m not fluent in other languages the translations are bad and they were just nice to talk to:) I asked each translator how they’d like to appear in the credits, both so that they were properly credited and also so that they felt they had some skin in the game.

## Worth The Effort?

It’s too early to tell if the sales to new regions outweigh the cost of paying translators, but finances aside, it’s deeply satisfying to see the game I made rendered in languages I can’t speak. The idea that more people can natively play Pine Tar Poker makes me proud. Using the above toolchain shrinks the technical cost to marginal. In fact, my next game [Well Word](https://www.bjmalicoat.com/projects/wellword), is already set up to be localized, even though it’s only in beta.

Pine Tar Poker is available on [iOS](https://apps.apple.com/us/app/pine-tar-poker/id1606835767#?platform=iphone) and [Android](https://play.google.com/store/apps/details?id=com.bmalicoat.pinetarpoker&gl=US) in English 🇺🇸, French 🇫🇷, Italian 🇮🇹, German 🇩🇪, Spanish 🇲🇽, Portuguese 🇧🇷, Japanese 🇯🇵, and Simplified Chinese 🇨🇳.