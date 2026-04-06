---
title: "Localizing Unity Games Step by Step"
source: "https://phrase.com/blog/posts/localizing-unity-games-official-localization-package/"
author:
  - "[[Mohammad Ashour]]"
published: 2021-02-11
created: 2026-04-06
description: "Learn all the tricks to using Unity’s first-party localization package to make your games available to the world."
tags:
  - "clippings"
---
Unity is [arguably one of the most popular](https://www.statista.com/statistics/321059/game-engines-used-by-video-game-developers-uk/) off-the-shelf engines for independent game developers. Breakout indies like [Cuphead](https://en.wikipedia.org/wiki/Cuphead), [Overcooked](https://en.wikipedia.org/wiki/Overcooked), [Hollow Knight](https://en.wikipedia.org/wiki/Hollow_Knight), [Ori and the Blind Forest](https://en.wikipedia.org/wiki/Ori_and_the_Blind_Forest), and [Monument Valley](https://en.wikipedia.org/wiki/Monument_Valley_\(video_game\)) all have Unity at the heart of their technology. Even some AAA goliaths like Blizzard’s [Hearthstone](https://en.wikipedia.org/wiki/Hearthstone) are made with the engine.

🗒 *Note »* Have you heard of the no-strings-attached alternative to Unity, Godot? Here’s [how to go about game localization in Godot](https://phrase.com/blog/posts/godot-game-localization/).

If you’re making commercial games with Unity, and have been kind enough to land on our little article here, you’re probably looking at expanding your game’s global reach through internationalization (i18n) and localization (l10n). So how do you go about internationalizing and localizing a Unity game?

You could roll your own solution, use an open-source library, or maybe pay for a package from the Unity Asset Store. Another option: the good people at Unity Technologies have been hard at work on a [first-party localization package](https://docs.unity3d.com/Packages/com.unity.localization@0.10/manual/index.html). It’s in preview as we write this, but it’s [not far from being released](https://forum.unity.com/threads/any-idea-on-rough-release-dates.1051058/#post-6797840) according to the Unity team, so we think it’s one to consider.

In this article, we’ll go through how to use the official Unity package to localize our games. We’ll build a small demo, primarily focused on UI and text, and proceed to install, set up, and utilize the package to localize this demo.

## Our Demo Project

Our demo starts with some UI that represents some messages we might typically display in a game.  
![Demo project game UI | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-demo-ui-before-i18n.png.webp)  
Here’s a look at our hierarchy. Nothing too crazy going on here: we’re using TextMeshPro (TMP) for our text UI rendering.  
![Demo project hierarchy | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-hierarchy-before-i18n.png.webp)

> 🔗 *Resource »* Grab the Unity project from our GitHub repo. The start branch has the demo as it is here, before localizing. The main branch has the completed project after localization.

### Versions of Unity & Packages Used

Here are the versions of Unity and packages we’re using in this article:

- Unity 2019.4.21f1
- [Localization 0.10.0-preview](https://docs.unity3d.com/Packages/com.unity.localization@0.10/manual/index.html) (official Unity i18n package)
- [Peyman Narimani](https://github.com/pnarimani) ’s [RTL Text Mesh Pro](https://github.com/mnarimani/RTLTMPro) 3.3.1 (for right-to-left rendering of TMPro components)

> 🔗 *Resource »* We’re using the Pixel Art GUI Elements provided by the talented Mounir Tohami. Two Google Fonts are utilized in our project as well: [Jost](https://fonts.google.com/specimen/Jost?sort=date&preview.text_type=custom) for Latin alphabets (English and French) and [Cairo](https://fonts.google.com/specimen/Cairo?sort=date&preview.text_type=custom&query=cairo) for Arabic.

### A Note On Addressables

The Unity localization package is built on [Addressables](https://docs.unity3d.com/Manual/com.unity.addressables.html), a system that allows us to load assets asynchronously, locally or from the network. Covering addressables is a bit outside the scope of this guide, and the localization package is designed so we don’t need to understand addressables fully before we start localizing. In those cases where we need to interact with the addressable system directly, we’ll be sure to mention it.

## Installation and Setup

Ok, let’s install the localization package. In Unity’s main menu, we’ll go to *Window ➞ Package Manager*.  
![Unity Main Window Package Manager | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-package-manager.png.webp)  
You’ll be utterly shocked to realize that this opens the *Package Manager* window. On this window, let’s click the plus sign and select *Add package from git URL*. In the ensuing text field, we’ll enter `com.unity.localization` and click the *Add* button to install the package.  
![Package Manager URL Window | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-add-i18n-package.png.webp)

### Creating the Localization Settings Asset

Once the package is installed we’ll need to create our project’s localization settings. We can do this by navigating to *Edit ➞ Project Settings ➞ Localization* and clicking the *Create* button.  
![Localization Project Settings | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-create-localization-settings.png.webp)  
This will both create the settings asset and activate it in our project. If you’re organizing your Unity project by asset type, you might want to create a `Localization` folder to keep your settings assets file, as well as future localization assets we’ll be creating.

### Adding Supported Locales

Let’s generate the locales our game will support. We can always change this later, but for now, we’ll support Arabic (ar), English (en), and French (fr). After making sure we’re at the *Edit ➞ Project Settings ➞ Localization* window, we can click the *Locale Generator* button to create our locale assets.  
![Locale Generator](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-locale-generator-btn.png.webp)  
We’ll be presented with a list of locales; we can check the ones we want to support and click *Generate*.  
![Selected Locales | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-locale-generator-window.png.webp)  
This will create locale assets for us, which we can place in our `Localization` folder.

## Active Locale Resolution

The localization package will attempt to resolve the active locale at runtime depending on the *Locale Selectors* order in our *Localization Settings*.  
![Locale Selectors | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-locale-selectors.png.webp)  
By default, the package will:

1. look for a locale specified with a command-line flag (this could be useful for automated testing, for example), and if that fails
2. attempt to determine the operating system locale (*System Locale*) and use that, and if that fails
3. use an explicitly-set locale, which we need to provide as our default locale.

> ✋🏽 *Heads up »* The package will fall back on more generalized locales if it needs to. For example, if the locale resolution settles on `en-CA` (Canadian English) as the active locale, and doesn’t find that exact locale in the list of supported locales, it will attempt to fall back to the more general `en` if `en` is supported.

### Setting the Default Locale

We can specify the default locale the package will use when it can’t determine the locale another way by going expanding the *Specific Locale Selector* section under *Locale Selectors*. From there, we can click the search target circle at the end of the *Locale Id* field and select one of our supported locales.  
![Default Locale Setup | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-select-default-locale.png.webp)  
We’ll select English for our project. Now, if all other locale-resolution strategies fail, our game will default to English as the default runtime locale.

> 🗒 *Note »* You can alter the order of the resolution strategies by dragging their rows in the *Localization Settings* window. We’ll use this later to force a default locale instead of using the one set in the user’s operating system when testing our production builds.

## Managing Translations

The official localization package will have us creating string table collections and populating them with translatable strings that we can then use in our components.

### Creating a Strings Table Collection

To create a new collection, we can go to *Window ➞ Asset Management ➞ Localization Tables* and click the *New Table Collection* button.  
![Strings Table Collection | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-create-string-table-collection.png.webp)  
After selecting which locales will be covered by the table, we can give our table a name and click *Create String Table Collection*. I’ve called my table `UI` and, when prompted, opted to save it under `Localizations/Table Collections/UI`. A handful of files related to this table will now live in that folder.

> 🗒 *Note »* You may have noticed a *Create Asset Table Collection* button on the *Localization Tables* window. This is because the official localization package can localize not only strings, but textures, audio, ScriptableObjects, and more. Check out the official [Quick Start Guide](https://docs.unity3d.com/Packages/com.unity.localization@0.10/manual/QuickStartGuide.html) for more info.

### Adding Translated Strings

With our strings table collection in place, we can now start adding our [translations](https://phrase.com/blog/posts/machine-translation/) to it.  
![Adding Translated Strings | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-add-string-key.png.webp)  
Clicking *Add New Entry* creates a new row in our table. We should give our row a `Key`, which we’ll use to refer to this entry in our components. And we can add a translation string for each of our supported locales.

> 🗒 *Note »* You can open localized table collections at any time by going to *Window ➞ Asset Management ➞ Localization Tables*.

## Right-to-Left Text

Before we go further, I want to make a short stop and tackle right-to-left (RTL) text rendering using TextMeshPro in Unity. TMP currently has no official support for RTL. The Unity team are working on it, but in the meantime, we have to use third-party packages for RTL rendering. I’ve opted to use [Peyman Narimani](https://github.com/pnarimani) ’s open-source [RTL Text Mesh Pro](https://github.com/mnarimani/RTLTMPro) since it worked well for me. Let’s go over how to use it in our project.

> 🗒 *Note »* If you’re not supporting a RTL language in your game, feel free to skip this section.

### Installing RTL Text Mesh Pro

To get started with RTL Text Mesh Pro (RTLTMP), we can head over to the library’s [releases page](https://github.com/mnarimani/RTLTMPro/releases) and grab the latest release. The `.unitypacakge` file associated with the release makes for easy installation into our project.  
With the `.unitypackage` file on hand, we can head over to Unity and go to *Assets ➞ Import Package ➞ Custom Package*. We can then select the `.unitypackage` file, keep all the folders and files checked, and click *Import*. This should install the package, creating a new folder in our project called `RTLTMPro`.

### The RTL Text Mesh Pro Component

Ok, let’s add our RTLTMP components so that we can get RTL text rendered in our game. In our hierarchy, we can right-click the game object we want to add our component to, and select one of the new `UI/* - RTLTMP` components.  
![RTL Text Mesh Pro Component | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-adding-rtltmp-component.png.webp)  
You’ll notice that the RTLTMP package has added a corresponding RTL component for each native TextMeshPro component. Let’s add a `Text - RTLTMP` component.  
That’s about it. The new text component can be used exactly like a normal TextMeshPro component. We just need to make sure to provide an RTL font asset under the *Font Asset* field. RTLTMP comes with some RTL font assets that we can use in our projects. They reside in `Assets/RTLTMPro/Fonts` and support at least Arabic and Farsi. We also need to add our RTL text to the *RTL Text Input Box*.  
![Translated UI | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-rtl-text.png.webp)  
Works like a charm. “What about localization,” I hear you asking? Localizing RTLTMP components is exactly like localizing TextMeshPro components, and we’ll cover that next.

> 🗒 *Note »* Instead of using the font assets that come with RTLTMP, we could [make our own](https://github.com/mnarimani/RTLTMPro#how-to-use). I’ve created a font asset based on the Cairo Google font and added it to [our GitHub repo](https://github.com/PhraseApp-Blog/unity-i18n-2021/tree/main/Assets/_Project/Fonts). I should mention that I found creating my own usable RTL font to be a bit tricky, and needed to tweak the font asset settings to make it render with the Arabic characters looking correctly connected (kind of 💔). If you want me to dive deeper into custom RTL font creation, let me know in the comments below.

## Localizing TextMesh Pro Text

We’ve done enough setup methinks. Let us localize, fellow devs. First, we’ll create either a TMP or RTLTMP component, depending on whether or not we’re supporting RTL text (see the previous section if you are). We localize the component by adding a *Localize String Event* component to the game object.  
![Localize String Event component | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-add-localized-string-event-component.png.webp)  
The *Localized String Event* component is provided by the official Unity localization package. It allows us to use a translation entry from one of our string table collections, providing it to one of our other components. We do this by hooking into the *Update String* event of the component.  
First, we’ll make sure we have a translation in our previously created string table collection. We can head over to *Window ➞ Asset Management ➞ Localization Tables* and make sure that the *Selected Table Collection* is the one we created previously (I called mine `UI`).  
We can then click the *Add New Entry* button at the bottom of the window, and enter a *Key* and translation for our entry. I’m adding a `new_ability_discovered` key to my table.  
![Adding Translated Strings | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-add-string-key-1.png.webp)  
Now we can head back over to our hierarchy and provide the key we just added to the *String Reference* field on our *Localized String Event* component.  
We should also add an item to the *Update String* list. This works like a normal Unity event: we drag the game object that we want to update to the object field. In our case, this is the object that houses our TMP component. We then use the function dropdown to select *TextMeshPro ➞ Text* (or *RTLTextMeshPro ➞ Text*).  
![Update String list | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-update-localized-tmp-text.png.webp)  
Now, when the locale changes (or when the localization system initializes), our TMP text will render its text in the active locale. We can run our game and use the debugging locale switcher in the top-right of the *Game* view to test this.  
![Game view | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-debugging-locale-switcher.png.webp)  
![Overview Localized UI | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-translated-basic-strings.png.webp)  
Our first translation. Take pride, friends. As per usual with Unity, there’s a bit of setup and learning to get localization working, but the system is quite powerful and flexible as we’ll see.

> 🗒 *Note »* A handy shortcut: instead of adding the *Localized String Event* component manually, we can also right-click the TMP (or RTLTMP) component and select *Localize*. This adds the localizing component and wires it to the update event automatically. We just have to select our translation key and we’re off and running.

### Interpolation

We often want to include dynamic text in our translated strings. Something like “Axion55 stole the flag!”, where “Axion55” is a username that can change at runtime. Let’s see how we can use *Smart Strings* to achieve this with Unity localization.  
We’ll add a new entry to our string table collection.  
![String table collection | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-interpolation-setting-strings.png.webp)  
I’m adding a string that reads “{Character} has leveled up!”. We have to check the *Smart* checkbox above each translation that will use interpolation. Notice that `{Character}` is a special sequence that will be replaced at runtime. We need to use the same `{VariableName}` sequence in all the entry’s translations to have it swapped for the actual value at runtime.  
We can use the *Debug* toggle next to a translation to see if we’ve formatted our text correctly for the *Smart Strings* system. We’ll get syntax highlighting in debug mode that should indicate whether our text is correct or not.  
![Smart Strings Formatting | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-interpolation-smart-string-debug.png.webp)  
Now we can provide the actual value to our *Localized String Event* component so that it will be used at runtime. First, let’s create a trivial MonoBehaviour to house our value.

using UnityEngine;

public class Values: MonoBehaviour

{

public string Character = "Tinka";

}

using UnityEngine; public class Values: MonoBehaviour { public string Character = "Tinka"; }

```
using UnityEngine;
public class Values : MonoBehaviour
{
    public string Character = "Tinka";
}
```

Next, let’s wire this to our *Localized String Event* component.  
![Localized String Event | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-interpolation-providing-values.png.webp)  
We can add the `Values` script as a component to our game object and drag it into the *Format Arguments* collection in our *Localized String Event* component. Of course, we also need to make sure that we’ve selected the correct key in the *String Reference* field of our *Localized String Event*. Now our TMP component will show our translations with the `Values.Character` value interpolated.  
![Translated UI interpolated | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-interpolated-text.png.webp)

> 🗒 *Note »* The string in the value-providing component must have the exact same name as the variable in our translation string (`Character` in the previous example).

This gives us basic interpolation, but it won’t update the TMP text if `Values.Character` changes at runtime. We’ll explore how to update translated text when its variable dependencies change when we discuss global variables a bit later.

> ✋🏽 *Heads up »* If you’re using RTLTMP (see above), make sure to select the *Force Fix* option on the component if your text begins with left-to-right text. Otherwise all the text the component renders will be left-to-right.

> 🔗 *Resource »* Unity’s localization package uses a fork of the popular C# [*Smart Strings*](https://docs.unity3d.com/Packages/com.unity.localization@0.10/manual/SmartStrings.html) library for its dynamic string formatting. *Smart Strings* is a drop-in replacement for the native.NET [string.Format()](https://docs.microsoft.com/en-us/dotnet/api/system.string.format?view=net-5.0). This means that any [format strings](https://docs.microsoft.com/en-us/dotnet/api/system.string.format?view=net-5.0#Starting) that we can use with `string.Format` can also be used with *Smart Strings*. We go into this a bit later when we cover number and date formatting.

### Plurals

“You have earned 3 gold coin!” Oops. We can do better with our plurals. Luckily, *Smart Strings* have excellent support for dynamic plural strings. Let’s add a new key to our string table collection to see this in action.  
![Adding new String to Smart Strings | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-plurals-setting-strings.png.webp)  
We’re interpolating a count value in our translations. Let’s take a look at the English format and break it down.

Your party has {ComboPointCount:plural:{} combo point|{} combo points}.

Your party has {ComboPointCount:plural:{} combo point|{} combo points}.

```
Your party has {ComboPointCount:plural:{} combo point|{} combo points}.
```

`ComboPointCount` is the integer value that we’ll use to determine the plural format to use. English has two plural formats: *one* and *other*. We can add these to our translation in order, separated by a `|` character. `{}` is a placeholder that will be swapped out for the value of `ComboPointCount` at runtime. And we use the optional `:plural:` designation to make it clear what the intention of our format is. This will render as follows in English.  
![UI without plurals | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-plurals-en-forms.png.webp)  
French, like English, has two plural forms, so its format is similar to the English one. Arabic, however, has six plural forms: *zero*, *one*, *two*, *few*, *many*, and *other*. As the figure above demonstrates, we provide these forms as we do in English, in order and separated by a `|`. Our Arabic translation then renders like so:  
![Arabic UI plural forms | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-plural-ar-forms.png.webp)  
Notice that *Smart Strings* is smart enough to know that Arabic has six plural forms. We don’t have to do anything other than provide those forms.

> ✋🏽 *Heads up »* For each translation, make sure to provide *all* the language’s plural forms, or you’ll get errors when the localization library can’t find the form corresponding to the given count.

Of course, to get this rendering we need to add our new key to a *Localized String Event* that updates a TMP component. And just like we did in the previous *Interpolation* section, we must provide this component with a modified `Values` MonoBehaviour that looks like the following.

using UnityEngine;

public class Values: MonoBehaviour

{

public string Character = "Tinka";

public int ComboPointCount = 200;

}

using UnityEngine; public class Values: MonoBehaviour { public string Character = "Tinka"; public int ComboPointCount = 200; }

```
using UnityEngine;
public class Values : MonoBehaviour
{
    public string Character = "Tinka";
    public int ComboPointCount = 200;
}
```

> 🔗 *Resource »* The [Unicode CLDR charts](https://unicode-org.github.io/cldr-staging/charts/latest/supplemental/language_plural_rules.html) are an excellent listing of per-language plural rules for your perusal.

### Number Formatting

*Smart Strings* can also be used to interpolate localized numbers. By default, numbers will get formatted per the rules of their locale. A new entry in our string table collection can help demonstrate.  
![Smart String localized numbers | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-number-formatting-setting-strings.png.webp)  
In addition to the normal `{VariableName}` specifier, notice the trailing `:C` in our format string. This is a standard.NET format specifier that results in a localized currency value. Once we’ve wired up our *Localized String Event* to our TMP component and provided a `Values.StolenAmount` `float` for the runtime value, we’ll see our translations rendered as follows.  
![Localized UI with plurals | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-currency-en-ar-fr.png.webp)  
Note that we’re seeing the currency, thousands separator, and decimal separator in each locale. English (en) defaults to US English, so its currency is formatted as US dollars. French (fr) defaults to France French, so it gives us Euros. Arabic (ar) defaults to Saudi Arabian Arabic, so its currency is displayed as Saudi Riyals.

> 🔗 *Resource »* We have complete control over the formatting of our numbers because we can use all.NET format specifiers with *Smart Strings*. In the example above we’ve used a [standard numeric format string](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-numeric-format-strings) to specify currency. We can also use [custom numeric format strings](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-numeric-format-strings) to exert more granular control over our number formatting.

### Date Formatting

Similar to number formatting, we can control date formats with *Smart Strings* as well. Let’s add a new entry to our string table collection that displays a date.  
![Smart string date formatting | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-date-formatting-setting-strings.png.webp)  
`d MMM` is a [custom date format specifier](https://docs.microsoft.com/en-us/dotnet/standard/base-types/custom-date-and-time-format-strings) that results in the numeric day of the month, followed by the abbreviated name of the month, in the given date. We can update our `Values` MonoBehaviour with a `Date` value and wire everything up to a *Localized String Event* to see the translated rendering.

using UnityEngine;

public class Values: MonoBehaviour

{

public string Character = "Tinka";

public int ComboPointCount = 200;

public float StolenAmount = 1014.99f;

public DateTime Today = DateTime.Now;

}

using UnityEngine; public class Values: MonoBehaviour { public string Character = "Tinka"; public int ComboPointCount = 200; public float StolenAmount = 1014.99f; public DateTime Today = DateTime.Now; }

```
using UnityEngine;
public class Values : MonoBehaviour
{
    public string Character = "Tinka";
    public int ComboPointCount = 200;
    public float StolenAmount = 1014.99f;
    public DateTime Today = DateTime.Now;
}
```

![UI with localized date format | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-date-formatting-en-ar-fr.png.webp)  
The above dates are presented in the calendars of their respective locales. English and French are using the Gregorian calendar whereas Arabic is using the Hijri calendar. This is because English (en), French (fr) and Arabic (ar) use the USA, France, and Saudi Arabic locales by default.

> 🔗 *Resource »* In addition to custom date formats, we of course also have [standard date formats](https://docs.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings).

## Global Variables

In the examples above we were able to provide dynamic values that are used in our translation strings at runtime. However, these values are a one-and-done deal: runtime changes to these values will not cause our translation strings to re-render. If we want reactive dynamic interpolation in our translation strings, we can use global variables.  
Global variables are part of the official localization package, and they solve the reactivity problem for us. Let’s create some global variables to see how they work.

### Creating a Global Variables Group

In our project view, we can right-click and select *Create ➞ Localization ➞ Global Variables Group*. This will create a new global variables group asset in our project. I’ve placed mine in a `Localization/Global Variables` folder. Clicking the asset reveals a collection in the *Inspector* that we can add to.  
![Asset in Inspector | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-global-variables-inspector.png.webp)  
Let’s add a string variable by clicking the *➕* icon and selecting *String*. We can give our string a key of `character` and a value of `Awi`. We’ll use this string in a translation shortly.

### Adding Global Variables to Localization Settings

In order to expose our global variables to our translations, we have to wire them up to our settings. Let’s open our *Localization Settings* and find the *➕* icon under *String Database ➞ Sources*. Clicking the *➕* reveals a menu, from which we can select *Global Variables Source*.  
![Global Variables Source | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-add-global-variables-source.png.webp)  
Now, *within* the *Global Variables Source* is another *➕* icon. Let’s click that to add an entry. We can leave the default entry name, `global`, as-is. Let’s drag the global variables asset that we created above into the slot next to the name. That should have us all wired up.

### Using Global Variables in Translation Strings

Interpolating our global variables into our translation strings is straightforward. Let’s head over to *Window ➞ Asset Management ➞ Localization Tables* to add a new translation.  
![Global variables in Smart Strings | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-using-globalized-string-in-translation.png.webp)  
I’ve added a new table entry with a key of `character_gained_ability`. Note that, just as before, we have to check the *Smart* checkbox to use interpolation in our translation strings.  
To designate the placeholder where our global variable will swap in, we use the `{group-name.variable-name}` syntax. The group name will be whatever we called the group when we registered it as a source in our *Localization Settings* (`global` in our case).

### Updating Global Variables from Scripts

In order to see the reactivity of our global variable, we need to update it at runtime. We’ll need a script to do this.

using UnityEngine;

using UnityEngine.Localization.SmartFormat.Extensions;

using UnityEngine.Localization.SmartFormat.GlobalVariables;

using Random = UnityEngine.Random;

public class InterpolatedStringUpdater: MonoBehaviour

{

\[SerializeField\] private string\[\] \_characterNames;

private void Start()

{

// Get our GlobalVariablesSource

var source = LocalizationSettings

.StringDatabase

.SmartFormatter

.GetSourceExtension<GlobalVariablesSource>();

// Get the specific global variable

var characterName =

source\["global"\]\["character"\] as StringGlobalVariable;

var randomCharacterName = \_characterNames\[

Random.Range(0, \_characterNames.Length)

\];

// Update the global variable

characterName.Value = randomCharacterName;

}

}

using UnityEngine; using UnityEngine.Localization.SmartFormat.Extensions; using UnityEngine.Localization.SmartFormat.GlobalVariables; using Random = UnityEngine.Random; public class InterpolatedStringUpdater: MonoBehaviour { \[SerializeField\] private string\[\] \_characterNames; private void Start() { // Get our GlobalVariablesSource var source = LocalizationSettings.StringDatabase.SmartFormatter.GetSourceExtension<GlobalVariablesSource>(); // Get the specific global variable var characterName = source\["global"\]\["character"\] as StringGlobalVariable; var randomCharacterName = \_characterNames\[ Random.Range(0, \_characterNames.Length) \]; // Update the global variable characterName.Value = randomCharacterName; } }

```
using UnityEngine;
using UnityEngine.Localization.SmartFormat.Extensions;
using UnityEngine.Localization.SmartFormat.GlobalVariables;
using Random = UnityEngine.Random;
public class InterpolatedStringUpdater : MonoBehaviour
{
    [SerializeField] private string[] _characterNames;
    private void Start()
    {
        // Get our GlobalVariablesSource
        var source = LocalizationSettings
            .StringDatabase
            .SmartFormatter
            .GetSourceExtension<GlobalVariablesSource>();
        // Get the specific global variable
        var characterName =
            source["global"]["character"] as StringGlobalVariable;
        var randomCharacterName = _characterNames[
            Random.Range(0, _characterNames.Length)
        ];
        // Update the global variable
        characterName.Value = randomCharacterName;
    }
}
```

When our scene loads, our `InterpolatedStringUpdater` will find our `global.character` global variable and set it one of the random names we’ve specified in `_characterNames`. This update will trigger a refresh in any localized string that uses it.  
Now let’s hook up our updater to a game object in our scene.  
![Game object updater in scene | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-global-var-add-updater.png.webp)  
Finally, let’s update one of our Localized String Events associated with a TextMeshPro text label to use our new localized string.  
![Localized String Events with a TextMeshPro | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-global-var-connect-to-tmp.png.webp)  
With that in place, every time we run our game, our UI will show a randomized character name.

![UI with global variable | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-global-vars-randomized-name-fr.png.webp) *Who will it be? Marm, Awi, or Tanta?*

And just to drive home the reactivity of global variables, we created a little countdown updater.  
![UI with global variables countdown | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-global-vars-w-countdown-en.gif.webp)

> 🔗 *Resource »* Get [the code for the countdown updater](https://github.com/PhraseApp-Blog/unity-i18n-2021/blob/main/Assets/_Project/Scripts/GlobalValueUpdaters/PluralValueUpdater.cs) from our GitHub repo.

> ✋🏽 *Heads up »* Global variables are serializable and will persist when you update them, much like ScriptableObjects.

> 🔗 *Resource »* There is much more we can do with global variables. Get the skinny from [the official docs](https://docs.unity3d.com/Packages/com.unity.localization@0.10/manual/GlobalVariables.html).

## Accessing Localized Strings from Scripts

At some point, we’ll likely need to use translated values directly in our scripts. This isn’t too hard and can be done with the following recipe.

using System.Collections;

using UnityEngine;

using UnityEngine.Localization;

using UnityEngine.Localization.Tables;

public class LocalizedStringUser: MonoBehaviour

{

// 1. Get a reference to the localized string table

\[SerializeField\]

private LocalizedStringTable \_localizedStringTable;

private StringTable \_currentStringTable;

private IEnumerator Start()

{

// 2. Wait for the table to load asynchronously

var tableLoading = \_localizedStringTable.GetTable();

yield return tableLoading;

\_currentStringTable = tableLoading.Result;

// At this point \_currentStringTable can be used to

// access our strings

// 3. Retrieve the localized string

var str =

\_currentStringTable\["new\_ability\_discovered"\]

.LocalizedValue;

Debug.Log(str);

}

}

using System.Collections; using UnityEngine; using UnityEngine.Localization; using UnityEngine.Localization.Tables; public class LocalizedStringUser: MonoBehaviour { // 1. Get a reference to the localized string table \[SerializeField\] private LocalizedStringTable \_localizedStringTable; private StringTable \_currentStringTable; private IEnumerator Start() { // 2. Wait for the table to load asynchronously var tableLoading = \_localizedStringTable.GetTable(); yield return tableLoading; \_currentStringTable = tableLoading.Result; // At this point \_currentStringTable can be used to // access our strings // 3. Retrieve the localized string var str = \_currentStringTable\["new\_ability\_discovered"\].LocalizedValue; Debug.Log(str); } }

```
using System.Collections;
using UnityEngine;
using UnityEngine.Localization;
using UnityEngine.Localization.Tables;
public class LocalizedStringUser : MonoBehaviour
{
    // 1. Get a reference to the localized string table
    [SerializeField]
    private LocalizedStringTable _localizedStringTable;
    private StringTable _currentStringTable;
    private IEnumerator Start()
    {
        // 2. Wait for the table to load asynchronously
        var tableLoading = _localizedStringTable.GetTable();
        yield return tableLoading;
        _currentStringTable = tableLoading.Result;
        // At this point _currentStringTable can be used to
        // access our strings
        // 3. Retrieve the localized string
        var str =
            _currentStringTable["new_ability_discovered"]
                .LocalizedValue;
         Debug.Log(str);
    }
}
```

We need a reference to the string table housing our strings. By exposing the `LocalizedStringTable` field above in the Unity editor, we get a familiar UI to set the table.  
![Localized String Table field in Unity editor | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-use-localized-str-add-table.png.webp)  
In the *Inspector*, we can select the `UI` table in we created earlier. If we then access the `new_ability_discovered` string from it as we’re doing in the code above, our `Debug.Log(str)` will show:

Simple string: New ability discovered! // locale = en

Simple string: Nouvelle capacité découverte! // locale = fr

Simple string: اكتشفت قدرة جديدة! // locale = ar

Simple string: New ability discovered! // locale = en Simple string: Nouvelle capacité découverte! // locale = fr Simple string: اكتشفت قدرة جديدة! // locale = ar

```
Simple string: New ability discovered!       // locale = en
Simple string: Nouvelle capacité découverte! // locale = fr
Simple string: اكتشفت قدرة جديدة!            // locale = ar
```

> ✋🏽 *Heads up »* We’re using the Coroutine version of the `Start` Unity event method above. This is because loading a localized string table is an asynchronous operation, and we have to `yield` until it completes before we can use our table.

### Interpolating Values in Scripts

We can swap dynamic values into our localized strings in code almost as easily as we can with localized string events in the Unity editor. Let’s demonstrate using the “Thief stole X from you!” string we created earlier.

using System.Collections;

using UnityEngine;

using UnityEngine.Localization;

using UnityEngine.Localization.Settings;

using UnityEngine.Localization.Tables;

public class LocalizedStringUser: MonoBehaviour

{

\[SerializeField\]

private LocalizedStringTable \_localizedStringTable;

\[SerializedField\] private Values \_values;

private StringTable \_currentStringTable;

private IEnumerator Start()

{

var tableLoading = \_localizedStringTable.GetTable();

yield return tableLoading;

\_currentStringTable = tableLoading.Result;

var str =

\_currentStringTable\["thief\_stole"\].GetLocalizedString(

LocalizationSettings.SelectedLocale.Formatter,

\_values);

Debug.Log(str);

}

}

using System.Collections; using UnityEngine; using UnityEngine.Localization; using UnityEngine.Localization.Settings; using UnityEngine.Localization.Tables; public class LocalizedStringUser: MonoBehaviour { \[SerializeField\] private LocalizedStringTable \_localizedStringTable; \[SerializedField\] private Values \_values; private StringTable \_currentStringTable; private IEnumerator Start() { var tableLoading = \_localizedStringTable.GetTable(); yield return tableLoading; \_currentStringTable = tableLoading.Result; var str = \_currentStringTable\["thief\_stole"\].GetLocalizedString( LocalizationSettings.SelectedLocale.Formatter, \_values); Debug.Log(str); } }

```
using System.Collections;
using UnityEngine;
using UnityEngine.Localization;
using UnityEngine.Localization.Settings;
using UnityEngine.Localization.Tables;
public class LocalizedStringUser : MonoBehaviour
{
    [SerializeField]
    private LocalizedStringTable _localizedStringTable;
    [SerializedField] private Values _values;
    private StringTable _currentStringTable;
    private IEnumerator Start()
    {
        var tableLoading = _localizedStringTable.GetTable();
        yield return tableLoading;
        _currentStringTable = tableLoading.Result;
        var str =
            _currentStringTable["thief_stole"].GetLocalizedString(
                LocalizationSettings.SelectedLocale.Formatter,
                _values);
        Debug.Log(str);
    }
}
```

Just like we did when we introduced interpolation before, we need to wire up our `Values` object in the inspector. Once we do, we should get the following logs.

Interpolated string: A thief stole $1,014.99 from you! // locale = en

Interpolated string: Un voleur vous a volé 1 014,99 €! // locale = fr

Interpolated string: قد سرق لص منك ر.س. 1,014.99! // locale = ar

Interpolated string: A thief stole $1,014.99 from you! // locale = en Interpolated string: Un voleur vous a volé 1 014,99 €! // locale = fr Interpolated string: قد سرق لص منك ر.س. 1,014.99! // locale = ar

```
Interpolated string: A thief stole $1,014.99 from you! // locale = en
Interpolated string: Un voleur vous a volé 1 014,99 €! // locale = fr
Interpolated string: قد سرق لص منك ر.س.‏ 1,014.99 !     // locale = ar
```

Of course, you can interpolate more than just float values when using localized strings in code. In fact, you can use any format that works with [Smart Formats](https://docs.unity3d.com/Packages/com.unity.localization@0.10/manual/SmartStrings.html).  
Just for a spot of fun, we used localized strings in code to make a little Dialog scene.  
![Translated dialog scene | Phrase](https://phrase.com/wp-content/uploads/2021/03/unityi18n2021p2-dialog-fr.gif.webp)  
You can get the dialog system code from [our GitHub repo](https://github.com/PhraseApp-Blog/unity-i18n-2021). Find the scene in `Assets/_Project/Scenes`.

## Previewing & Building

We’ve already touched upon the locale game view menu dropdown that we can use to preview different translations in play mode. This can be quite handy when developing.  
![Drop down locale menu | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-debugging-locale-switcher.png.webp)

> 🗒 *Note »* You can turn the locale game view menu dropdown on or off in Unity preferences under *Localization*.

What about standalone builds? Well the simplest solution to preview translations in standalone builds is to force a locale from our *Locale Settings*.  
![Locale selector | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-forcing-locale.png.webp)  
Let’s set the *Locale Id* in the *Specific Locale Selector* and move the selector to the top of the list. This will ensure that our set locale will resolve as the active one at runtime.  
Because the localization package uses addressables, we have to build our addressables groups before we can get our updated translations in our standalone builds. To do this, we head over to *Window ➞ Asset Management ➞ Addressables ➞ Groups*. From there, we can click *Build ➞ New Build ➞ Default Build Script* to build our addressables groups.  
![Addressables groups | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-building-addressable-groups.png.webp)  
We can now build for our target platform to test our translations for production.  
![UI forced French translations | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-standalone-build-fr.png.webp)

*A standalone build with forced French translations*

> ✋🏽 *Heads up »* During my research I experienced a [known issue](https://forum.unity.com/threads/addressables-not-loading-in-build.925982/) with translations not appearing when I was using the addressables package v1.16.16. Reverting the package back to v1.16.15 seemed to resolve the issue.

## Fallback

Sometimes we will have missing translations in our projects. There a few ways to deal with this, and we can set our chosen strategy in *Localization Settings*.  
![Missing Translation State field | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-control-missing-translation-appearance.png.webp)  
The *Missing Translation State* field can be set to show a warning message instead of the translated string (default). This warning will appear in production as well. Another option is to *Print Warning*, which will show the warning in the console and render an empty string for the translation.  
We can also check the *Use Fallback* checkbox to use locale fallbacks for the whole project. This will cause a translation missing in say, French, to “fall back” to its English counterpart. If we go this route we need to make sure to set our fallback locales on each local we want to fall back. Selecting one of the locale assets in our project reveals its details in the *Inspector*. From there we can find the *Metadata* collection and add a *Fallback locale* to it.  
![Fallback locale | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-fallback.png.webp)  
Now when we have a missing French translation, its less-cool English cousin will be shown to the player instead.  
![UI with fallback locale | Phrase](https://phrase.com/wp-content/uploads/2021/02/unityi18n2021p1-missing-fr-translation-w-fallback.png.webp)

> 🗒 *Note »* We don’t have to set the *Fallback* option on a per-project level. We can choose to set it on individual *Localized String Event* s instead.

## GG WP

We hope you’ve enjoyed this guide to using the official Unity localization package to localize your Unity games. Kudos to the Unity team for constantly developing the engine and empowering developers to make awesome games. And we’ve only scratched the surface of what you can do with Unity’s first-party localization package. Check out [the official docs](https://docs.unity3d.com/Packages/com.unity.localization@0.10/manual/index.html) for more. And if you want us to dive deeper into any topic we covered here, or to cover any other Unity i18n topic, let us know in the comments below.

> 🔗 *Resource »* Get the project we’ve built here from [our GitHub repo](https://github.com/PhraseApp-Blog/unity-i18n-2021).

And if you’re looking for a professional localization platform for your growing team, check out [Phrase](https://phrase.com/). Built by developers for developers, Phrase features a powerful API, flexible CLI, GitHub/Bitbucket/GitLab sync, webhooks, machine translation, and a rich web-based translation console for your translation team. Check out all of [Phrase’s features](https://phrase.com/roles/developers/) to let Phrase do the heavy lifting in your localization process, keeping you focused on the creative code you love.