---
title: "TextMesh Proのローカライズ対応"
type: concept
sources:
  - "raw/articles/Make TextMesh Pro Font Assets Responsive to Language Localization Switching.md"
  - "raw/articles/TextMesh Pro Localization.md"
  - "raw/articles/Localizing Unity Games As An Indie Dev.md"
related:
  - "[[unity-localization]]"
  - "[[game-localization]]"
created: 2026-04-06
updated: 2026-04-06
public: true
tags:
  - unity
  - localization
  - textmesh-pro
---

## 概要

TextMesh Pro（TMP）はUnityの標準テキスト描画コンポーネントだが、多言語対応にはフォントアセットの管理と切り替えの仕組みが必要になる。特に東アジア言語や中東言語では、専用のフォントアセットとフォールバック戦略が重要。

## フォントアセットの基本

- TMPはSDF（Signed Distance Field）シェーダーでフォントを描画
- フォントアセットはフォントファイルから文字をテクスチャアトラスにベイクして生成
- **Font Asset Creator**（Window > TextMeshPro > Font Asset Creator）で作成

## 文字セットのグループ化

言語をグループにまとめ、共有文字セットでフォントアセットを作成するのがベストプラクティス:

- **Latin (ASCII)**: 英語、スペイン語、ドイツ語、フランス語等
- **Cyrillic**: ロシア語、ギリシャ語等
- **East Asian**: 中国語、日本語等
- **Middle Eastern**: アラビア語、ペルシア語等

**注意**: 日本語と中国語では同じ漢字でもグリフの見た目が異なるため、別々のフォントを使用すべき。

## フォントアセット生成の最適化

- 全Unicodeレンジを生成すると巨大なテクスチャ（8Kでも23分以上）になる
- **使用文字のみをスキャン**してサブセットを生成すると1024x1024で半秒に短縮
- 数字と英字は動的に使われることが多いため、サブセットに含めておく

## フォールバック戦略

### 個別フォールバック
- TMPのFallback Font Assets設定で言語間のフォールバックチェーンを構成
- 例: Regional Font → International Font → Dynamic Fallback

### Dynamic Fallback
- Atlas Population Modeを**Dynamic**に設定したフォントアセット
- ソースフォントファイルから必要な文字を動的に追加
- 日本語の漢字など、使用頻度が限られる大規模文字セットに有効

### Global Fallback Font
- 複数言語の文字を同時表示する場面（言語選択画面等）で使用
- Edit > Project Settings > TextMesh Pro > Settingsで設定
- Staticフォールバックでビルドサイズとメモリを最小化

## 言語切り替え時のフォント切り替え

### 集中管理パターン（LanguageManager + LocalizationResponder）
- **LanguageManager**: 言語変更をC#イベントで通知する集中管理クラス。言語セットごとのフォントアセットスロットを持つ
- **LocalizationResponder**: 各TMPオブジェクトに付与。イベントを購読してフォントアセット・マテリアルプリセットを切り替え
- 個別オブジェクトでのオーバーライドも可能

### UI空間と3D空間の違い
- UI（Canvas）TMPと3D（World Space）TMPで別々のフォントアセット（またはマテリアル）が必要になる場合がある
- 同じマテリアルを共有するとデバイスによってはテキストが表示されない問題が報告されている

## Unity Localization Packageとの連携

- **Localize String Event**コンポーネントでTMPテキストの自動更新に対応
- RTLTMProコンポーネントにも同じLocalize String Eventが使える
- Smart Stringsで動的テキスト（複数形、数値フォーマット等）をサポート

## 関連ソース

- [[textmesh-pro-localization-guide]]
- [[unity-localization-package-guide]]
- [[unity-localization-indie-dev]]
