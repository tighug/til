---
title: "10 Translation Prompts for ChatGPT and Claude That Actually Work"
source: "https://chatscontrol.com/blog/prompt-engineering-translation-chatgpt-claude-prompts"
author:
  - "[[Dmitry]]"
published: 2026-03-19
created: 2026-04-06
description: "10 tested translation prompts for ChatGPT and Claude - legal, medical, marketing translation with real examples and practical tips for professional translators."
tags:
  - "clippings"
---
Two translators pasted the same text into ChatGPT. The first one typed “translate to German.” The second spent a minute on the prompt - specified a role, context, a three-term glossary, and the target audience. The second one got a translation you couldn’t tell apart from a seasoned professional’s work. The first one got typical machine output that needed a complete rewrite. The difference wasn’t the model or the subscription plan. It was 50 words in the prompt.

Prompt engineering isn’t magic or hacking. It’s the ability to tell AI exactly what you want from it. And for translators, it’s a skill that directly affects your income: those who know how to work with ChatGPT and Claude properly do MTPE in 20 minutes instead of an hour.

Below are 10 specific prompts you can copy and use right now. Each one is designed for a specific situation, with an explanation of why it works.

## Why Your Prompt Matters

A study from the University of Hong Kong (ACM MMAsia 2024) confirmed what practicing translators have known for a while: prompt quality directly impacts translation quality. A simple “translate this” gives you Google Translate-level output. But add a role, context, and a couple of examples - and the same GPT-4o produces translations that compete with human work.

Key elements that improve results:

- **Role** - “you’re a legal translator with 10 years of experience” makes the model use appropriate terminology
- **Context** - document type, who the translation is for, which country it’ll be used in
- **Glossary** - specific terms that must be translated a certain way, no alternatives
- **Examples** (few-shot) - one or two sample translations in the desired style
- **Constraints** - what NOT to do (don’t simplify, don’t skip terms, don’t change numbers)

A head-to-head test on 200 sentences ([aitoolclash.com, 2026](https://aitoolclash.com/posts/chatgpt-vs-claude-for-translation-2026/)) showed Claude scoring 8.3/10 versus ChatGPT’s 7.9/10. Claude handles tone, idioms, and cultural context better. ChatGPT is stronger for technical documentation and supports more language pairs. But both models dramatically improve with the right prompt.

## 10 Translation Prompts

### 1\. The Basic Role-Based Prompt

The simplest upgrade from “translate this” - give the model a role.

```
You are a professional translator with 10+ years of experience translating
from [source language] to [target language]. Your translations are natural,
accurate, and read as if originally written in the target language.

Preserve the tone and style of the original. Do not add explanations
or commentary - output only the translation.

Text to translate:
[paste your text]
```

**Why it works:** the role activates a corresponding “mode” in the model. Instead of generic translation, it starts using professional vocabulary and natural target language constructions. The “read as if originally written” instruction reduces calques and literalness.

**When to use:** general texts, correspondence, articles, descriptions - anything that doesn’t need specialized knowledge.

### 2\. Legal Translation

Legal texts are a minefield where one wrong word changes the meaning of a contract. This prompt forces the model to be maximally precise.

```
You are a certified legal translator specializing in [source] to [target]
translation. Translate the following legal document accurately, preserving
all legal terminology and formal register.

Rules:
- If a legal term has no direct equivalent, keep the original in parentheses
  next to your translation
- Do not simplify or paraphrase legal formulations
- Preserve all references to laws, articles, and paragraphs exactly
- Maintain formal register throughout

Document type: [contract / court decision / power of attorney]
Jurisdiction: [Germany / USA / UK]

Text:
[paste your text]
```

**Why it works:** specifying jurisdiction is critical - legal terminology differs even between Germany and Austria, or between the US and the UK. The rule about keeping original terms in parentheses prevents the model from “inventing” equivalents that don’t exist. We covered the risks of machine translation for legal texts in detail in a [separate article](https://chatscontrol.com/en/blog/legal-documents-why-machine-translation-fails).

### 3\. Medical Translation

Medical texts demand absolute precision in dosages, diagnoses, and procedures.

```
You are a medical translator with expertise in [cardiology / oncology / general medicine].
Translate the following medical text from [source] to [target].

Rules:
- Use standard medical terminology accepted in [target country]
- For diagnoses, provide ICD-10/ICD-11 codes if mentioned in the original
- Preserve ALL numerical values, dosages, and measurements exactly as written
- Do not interpret or add medical information not present in the original
- For abbreviations, provide the target language equivalent with the original
  abbreviation in parentheses on first mention

Text:
[paste your text]
```

**Why it works:** the “do not interpret or add medical information” rule is protection against hallucinations. There have been documented cases where ChatGPT, when translating a medical report, added a specific drug dosage that wasn’t in the original. For a medical document, that’s a potentially dangerous error.

Marketing isn’t translated - it’s adapted. Here you need effect, not accuracy.

```
You are a creative copywriter and translator. Adapt the following marketing
text from [source] to [target language] for the [target country/region] market.

This is transcreation, not literal translation. The message, emotion,
and call-to-action must work for the target audience even if the wording
changes significantly.

Brand voice: [playful / professional / bold / warm]
Target audience: [young professionals 25-35 / parents / business owners]

Keep wordplay or humor if possible, or replace with an equivalent
that works in the target culture. Adapt cultural references.

Text:
[paste your text]
```

**Why it works:** the word “transcreation” in the prompt is key. It gives the model permission to deviate from the original for the sake of impact. Without it, even Claude will cling to the original’s structure and produce a “translation” rather than an “adaptation.”

### 5\. Translation with a Glossary

When a client provides terminology - you follow it, not make up your own alternatives.

```
You are a professional translator. Translate the following text from
[source] to [target], strictly following this terminology glossary.

These terms MUST be translated exactly as specified. Do not use synonyms
or alternative translations for these terms.

GLOSSARY:
- [source term 1] → [target term 1]
- [source term 2] → [target term 2]
- [source term 3] → [target term 3]

TEXT:
[paste your text]
```

**Why it works:** without a glossary, the model might translate the same term differently in different parts of a document. A glossary locks in terminology and provides consistency, which is critical for [legal documents](https://chatscontrol.com/en/blog/machine-translation-legal-documents-trust) and technical texts.

### 6\. Long Document Translation in Parts

Claude’s context window goes up to 200K tokens (~150,000 words), GPT-4o is 128K. But even with a large window, long documents work better when fed in a structured way.

```
You are a professional translator working on a long document from [source]
to [target]. I will provide the text in sequential parts. Maintain consistent
terminology and style throughout ALL parts.

Key terms to use consistently:
- [term 1] = [translation 1]
- [term 2] = [translation 2]
- [term 3] = [translation 3]

Style: [formal / informal / technical]
Target audience: [who will read this]
Document type: [annual report / user manual / legal contract]

This is part [1] of [5]. Translate:
[paste your text section]
```

**Why it works:** indicating the part number and total count helps the model maintain context. Key terms at the beginning of each part guarantee consistency. This is especially useful when working with [CAT tools](https://chatscontrol.com/en/blog/cat-tools-comparison-trados-memoq-smartcat-2026) where translation happens segment by segment.

### 7\. Back-Translation for Quality Verification

Back-translation is standard practice for medical and legal texts. AI does it instantly.

```
Perform these steps in order:

Step 1 - TRANSLATE: Translate the following text from [source] to [target].

Step 2 - BACK-TRANSLATE: Translate your result back to [source language].

Step 3 - COMPARE: List any differences in meaning between the original
and your back-translation. Note missed nuances, changed emphasis,
or potential errors.

Step 4 - CORRECT: If you found issues in Step 3, provide a corrected
translation.

Original text:
[paste your text]
```

**Why it works:** back-translation forces the model to find its own errors. If meaning changes during a round-trip translation - there’s a problem somewhere. It doesn’t replace human review, but it automatically filters out obvious mistakes.

### 8\. UI/Software Localization

Interface translation is a separate discipline with strict constraints on length and formatting.

```
You are a software localization specialist. Translate the following UI
strings from [English] to [target language].

Rules:
1. Keep translations concise - UI space is limited, aim for similar
   character length as the original
2. Keep all placeholders unchanged: {name}, %d, {{count}}, %s
3. Do not translate: brand names, product names, technical identifiers
4. Use informal/formal "you" form: [specify which]
5. Adapt date format to [target locale format, e.g., DD.MM.YYYY]
6. For ambiguous strings, add a translator comment in [brackets]

Output as a table: Original | Translation | Notes

Strings:
[paste your strings]
```

**Why it works:** the rules about placeholders and string length are what people usually forget. A broken placeholder = a production bug. An overly long translation = clipped text in the interface.

### 9\. Translation with Explanations and Alternatives

When you’re working on a complex text and want to see the model’s decision-making process.

```
Translate the following text from [source] to [target language].

After the translation, provide:
1. A list of terms where you chose between multiple translation options -
   explain why you chose each one
2. Any idioms or cultural references that required adaptation -
   explain what you changed and why
3. Sentences where the meaning could be ambiguous - explain your
   interpretation

Text:
[paste your text]
```

**Why it works:** this prompt turns AI from a black box into a transparent tool. You see the reasoning behind every decision and can agree or pick an alternative. Perfect for learning and for when you’re working in an unfamiliar domain.

### 10\. Multi-Step Translation: Draft to Final

Research shows that two-stage translation (first literal, then adaptation) gives better results than trying to do everything in one pass.

```
Translate the following text from [source] to [target language] in three steps:

Step 1 - LITERAL DRAFT: Translate as literally as possible, preserving
the original sentence structure.

Step 2 - NATURAL ADAPTATION: Rewrite Step 1 so it reads naturally
in [target language], as if originally written in that language.
Fix calques, adjust word order, replace unnatural constructions.

Step 3 - FINAL REVIEW: Compare Step 2 with the original. Ensure no
meaning was lost during adaptation. Provide the final translation.

Show all three steps so I can review the process.

Text:
[paste your text]
```

**Why it works:** breaking the process into steps prevents the model from cutting corners. Step one focuses on accuracy, step two on naturalness, step three on self-review. This mirrors the process professional translators use in [MTPE workflows](https://chatscontrol.com/en/blog/mtpe-post-editing-machine-translation-future).

## ChatGPT or Claude: Which Prompt Goes Where

Both models work well with prompts, but they have different strengths.

| Task | Better model | Why |
| --- | --- | --- |
| Literary / creative translation | Claude | Better tone preservation, idioms, cultural nuances. Only 8% literal idiom translations vs ChatGPT’s 34% |
| Technical documentation | ChatGPT | Better at preserving code formatting and technical terminology |
| Large document with glossary | Claude | Larger context window (200K+ tokens), better terminology consistency across a full document |
| Rare language pairs | ChatGPT | Supports more languages, including lower-resource ones |
| Marketing transcreation | Claude | Better at adapting humor and cultural references |
| High-volume API work | ChatGPT | Faster response times, simpler integration |

For a detailed comparison of AI models for translation, check our article on [Gemini vs GPT-4o](https://chatscontrol.com/en/blog/gemini-vs-gpt-4o-best-ai-translator-2026). And if you want to understand the difference between AI translation and classic NMT (DeepL, Google Translate), see [LLM vs NMT](https://chatscontrol.com/en/blog/llm-vs-nmt-neural-machine-translation-difference).

## Common Prompt Mistakes for Translation

**“Translate this”** - with zero context. The model doesn’t know if it’s a legal contract or an Instagram caption, so it translates “on average.”

**Overly long prompts** - three paragraphs of instructions confuse the model. Keep it structured: role, then context, then rules, then text.

**Missing language pair** - “translate to German” without specifying the source language. The model will guess, but why risk it?

**No domain context** - “translate contract” without specifying it’s an employment contract for Germany. An Arbeitsvertrag and a Werkvertrag are different documents with different terminology.

**Ignoring region** - German for Germany, Austria, and Switzerland differs significantly. “Führerschein” vs “Fahrausweis” vs “Lenkberechtigung” - same document, three different words.

## FAQ

### Should I write prompts in English or my native language?

English prompts tend to work more consistently because models are primarily trained on English data. But for pairs like DE→EN or FR→ES, you can write the prompt in either language with comparable results. What matters most is the prompt’s structure (role, context, rules), not the language it’s written in.

### How many terms can I add to a glossary in the prompt?

For ChatGPT, 10-30 terms is optimal. For Claude with its larger context window, you can go up to 100-200 without quality loss. If you have more terms, upload the full glossary as a file (both models support file uploads) and reference it in your prompt.

### Does a good prompt replace human review?

No. Even the best prompt doesn’t guarantee 100% accuracy. AI can hallucinate - add information that wasn’t in the original. For official documents, no prompt replaces a [sworn translator](https://chatscontrol.com/en/services/certified-translation). But the right prompt cuts post-editing time from an hour down to 15-20 minutes.

### Which prompt should I use for immigration documents?

Combine prompt #2 (legal) with prompt #5 (glossary). Specify the exact institution (Ausländerbehörde, USCIS, IRCC), document type, and jurisdiction. Add a glossary of 5-10 key terms for the specific procedure. This produces a result closest to what the official on the other end expects.

### Do these prompts work with free versions of ChatGPT and Claude?

Yes, all 10 prompts work with free versions too. But paid tiers (ChatGPT Plus, Claude Pro) deliver better quality thanks to access to the latest models (GPT-4o, Claude Opus/Sonnet) and larger context windows. If you do translation work regularly, the subscription pays for itself within the first week.