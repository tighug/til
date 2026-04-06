---
title: "Make TextMesh Pro Font Assets Responsive to Language Localization Switching"
source: "https://crazyminnowstudio.com/posts/making-textmesh-pro-font-assets-responsive-for-localization/"
author:
published:
created: 2026-04-06
description: "Easily implement localization language switching for TextMesh Pro font-assets in Unity."
tags:
  - "clippings"
---
#### TextMesh Pro is Awesome! Localization is Awesome!

\[UPDATE 2017-11-09: the UnityPackage file (version 1.0.1) has been released to correct a typo bug in the LocalizationResponder.cs script.\]

This asset set will demonstrate one method for making TextMesh Pro components responsive to language changes in your app/game. In other words, some languages use characters that are not present in all fonts -- this requires the use of different font assets. It's easy to switch between font assets in TextMesh Pro and you can even programmatically switch and apply material presets to different font assets.

**NOTE:** There are several localization packages available, M2H's Localization Package is the one we're using here, but you should be able to easily modify the code/implementation to your localization package of choice. It should likewise be just as simple to modify the scripts to work with normal Unity Text components if required/desired.

This implementation uses a helper script/componet (we're calling a localization responder) which is placed on objects using TextMesh Pro with localization. The localizaton responder works in conjuction with a centralized manager (in this instance, the LanguageManager class). Language changes are signaled via a C# event which the localization responder is subscribed to. We're going to be handling language changes in the LanguageManager class, but they could be implemented anywhere. The LanguageManager also maintains public slots for defining a centralized selection of language sets (languages that require different character sets and subsequently different font assets). In this example, we'll be using 3 language sets: Russian (cyrillic), Korean, and a general latin/germanic character set (supporting EN, ES, FR, DE, etc.). The method described would work with any number of language character sets needed.

If you like/appreciate this article and the scripts, please share it with others. Also, take a look at our [real-time, lip-synchronization asset SALSA Lip-Sync](https://crazyminnowstudio.com/unity-assetstore-salsa-suite).

In addition to centralize management of font assets in the LanguageManager class, the LocalizationResponder helper script also contains slots for font assets to override the LanguageManager centralization if desired -- it is convenient to have a general set of font assets for the whole project, while affording the ability to individually select different fonts for specific display requirements.

##### General features of the localization responder and centralized manager:

- *C# event firing when the language is changed* -- use this to drive any sort of reaction to the event. The event system can be used to notify any portion of your codebase of a language change. In this instance, the LocalizationResponder "hears" the change and subsequently re-maps the language selected to the appropriate font asset, material preset, and localization label (as desired).
- [![](https://crazyminnowstudio.com/site/assets/files/1506/languagemanagereditor.250x0-is.png)](https://crazyminnowstudio.com/site/assets/files/1506/languagemanagereditor.png) *Centralized font asset management for different language classes* (handled in the WorldManager class). In this implementation, the centralized font-asset slots must be populated or you will get an error at runtime. You will need to modify the responder if you do not desire this behavior.
- [![](https://crazyminnowstudio.com/site/assets/files/1506/localizationrespondereditor.250x0-is.png)](https://crazyminnowstudio.com/site/assets/files/1506/localizationrespondereditor.png) *Local font asset overrides for specific display requirements.* The override slots should remain null if you do not wish to override the centralized font-asset selections.
- *Re-mappable TexhMesh Pro font material assets.* You may include a font-material-preset if you desire. It is \*not\* required that the preset be created with the font-asset being used. The font-material's font-atlas is remapped to the font-asset selected and should work fine for similar font types. This allows you to re-use the same font-material for multiple font-assets if desired. Of course, you are also free to create and use as many font presets as you desire. Drop the appropriate material-preset into this slot.
- *Localization meta tag/label entry.* There may be occassions where you don't want the text to be localized/changed. If this is the case, simply leave this slot blank. Otherwise, the (M2H) localization system will convert the text to the appropriate language text when the language change event fires.

[![](https://crazyminnowstudio.com/site/assets/files/1506/unityeditorscreenshot.250x0-is.png)](https://crazyminnowstudio.com/site/assets/files/1506/unityeditorscreenshot.png) [![](https://crazyminnowstudio.com/site/assets/files/1506/russianselected.126x0-is.png) ![](https://crazyminnowstudio.com/site/assets/files/1506/russianselected.126x0-is.png)](https://crazyminnowstudio.com/site/assets/files/1506/russianselected.png)

##### Usage - Getting Started:

1. Ensure you have already imported TextMesh Pro into your project.
2. Ensure you have imported M2H Localization (or whichever localization package you are using). NOTE: if not using M2H, you'll need to modify both scripts to work with your localization package.
3. Download the files below and import them into your project. The two included scripts will import into your Assets root, move them wherever you like.
4. Add the LanguageManager.cs script to a game manager object (this will be your centralized manager object for language changes).
	1. Configure the language slots with your preferred (centralized) TextMesh Pro font-assets.
		2. If you need more language sets, add them to the LanguageManager and LocalizationResponder scripts. See the video for more information.
5. Add the LocalizationResponder.cs to any object(s) with TextMesh Pro that you would like to respond to localization changes.
	1. Configure the responder as necessary. If you do not want to override the centralized font-assets, leave the slots null on this component. If you don't have any font-material-presets to change, leave this blank as well. See the video for more information.
		2. If you've added more language set slots to the LanguageManager, you'll need to edit the LocalizationResponder script to process the additional sets in the switch statement.
		3. If you're using M2H's Localization Package (or have edited both of these scripts to work with your preferred localization package), you can also add your localization label to this TextMesh-based object.
6. That should be it for the configuration of the LanguageManager and LocalizationResponder. Implement some language changing capabilities in your scene (i.e. buttons, etc.) and make sure they call LanguageManager.SetLanguage(string).
7. If you're totally lost, make sure you watch the video -- it should clarify the process.

##### Watch the Video:

For those of you that like to watch (you know who you are!), here's a quick video tutorial covering all of the TextMesh Pro and localization configuration in a scene.

---

![](https://www.youtube.com/watch?v=5YEADopvGXU)

---

##### Support:

Nope. This stuff is all free for your use/consumption -- you're on your own.;)

##### Download the files (license for use):

There are two scripts in this implementation, provided as-is in a.unitypackage file.  
**NOTE: You are free to modify the files for your personal or commercial use. You may not sell or re-sell these scripts, or their derivatives, in any form other than their implementation as a system into your Unity project game/application.**  
Of course, we always appreciate your attributions, tweets, shares, likes, follows, or link-backs to this page or the Crazy Minnow Studio homepage. If you have any questions concerning licensing, please email us at our AssetSupport address.  

**NOTE:** *While every attempt has been made to ensure the safe content and operation of these files, they are provided as-is, without warranty or guarantee of any kind. By downloading and using these files you are accepting any and all risks associated and release Crazy Minnow Studio, LLC of any and all liability.*

  
[Download Files](https://crazyminnowstudio.com/pkgDL.php?file=responsivelocalization_1_0_1.unitypackage)