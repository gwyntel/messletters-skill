---
name: messletters
description: Convert text into 121+ Unicode fancy text styles — math alphabets, scripts, symbols, decorative, encircled, runic, and more. Extracted from messletters.com.
version: 1.0.0
author: gwyntel
license: MutuaL-1.2
metadata:
  hermes:
    tags: [unicode, fancy-text, text-transform, messletters, creative, typography]
    related_skills: [xhb-111, refract]
---

# Messletters — Unicode Fancy Text Converter

Converts ASCII text into 121 Unicode "fancy text" styles using pre-extracted character mappings from [messletters.com](https://www.messletters.com/en/).

Zero dependencies. Single Python file. Works anywhere.

**Install:** `hermes skills install gwyntel/messletters/messletters`

## Module

Bundled at `scripts/messletters.py` within this skill.

## Import

```python
import sys, os
skill_scripts = os.path.expanduser('~/.hermes/skills/messletters/scripts')
sys.path.insert(0, skill_scripts)
from messletters import convert, search_styles, list_styles, preview_styles, reverse_lookup, CATEGORIES, STYLES
```

## API

### `convert(text: str, style: str) -> str`
Convert text to a named style. Non-ASCII chars (spaces, punctuation, emoji) pass through unchanged. Returns original text if style name not found.

```python
convert("Hello World", "Math Sans-serif Bold")
# → 𝗛𝗲𝗹𝗹𝗼 𝗪𝗼𝗿𝗹𝗱

convert("Claire", "Circled")
# → ⓒⓛⓐⓘⓡⓔ

convert("Love you 3000", "Math Fraktur Bold")
# → 𝕃𝖔𝖛𝖊 𝖞𝖔𝖚 𝟯𝟬𝟬𝟬
```

### `list_styles() -> list[str]`
All 121 style names, alphabetically sorted.

### `search_styles(query: str) -> list[str]`
Case-insensitive substring search on style names.

### `preview_styles(text: str = "Hello World") -> list[tuple[str, str]]`
Apply all styles to text. Returns list of `(style_name, converted_text)` tuples.

### `reverse_lookup(char: str) -> list[tuple[str, str]]`
Find which styles map a single ASCII character and what they produce.

### `CATEGORIES`
Dict of `category_name -> list[style_names]` for browsing by type.

### `STYLES`
Raw data dict: `style_name -> (lower_cps_tuple, upper_cps_tuple, digit_cps_tuple)`.

## Categories

### mathematical (17)
Math Script Customized (Royal), Math Monospace, Math Sans-serif Bold, Math Serif Italic, Math Serif Bold, Math Sans-serif, Math Script (Royal) Bold, Math Sans-serif Italic, Math Sans-serif Bold Italic, Math Fraktur Bold - Edit, Math Fraktur Normal, Math Serif Bold Italic, Math Script (Royal), Math Fraktur Bold, Math Serif Italic Greek, Math Serif Italic v2, Math Fraktur Normal - Edit

### enclosed (6)
Circled, Circled Black, Boxed, Boxed Black, Parenthesized, Fullwidth

### script_cursive (14)
Lilia, Yas Script, Script a, Handwrite, Writing, Serene, Cute v1, Cute v2, Cute v3, FancyCurly, Curly, AwCute, Ribbon, Swipe

### gothic_runes (5)
Runes, Gothic, Celtic, Black Panther, Etruscan

### asian_scripts (14)
Japanese, CJK, Yi One, Yi Two, Yi Three, Yi Four, Yi Five, Yi Six, Yi Seven, Yi Eight, Malayalam, Ge'ez Script - Ethiopian, Ge'ez Script - Amharic, Cherokee Mystique

### decorative (18)
Messletters, Fasion, Swirly, Wiggly, Dotted, BigOne, Strange, Newspaper Cutout Standard, Newspaper Cutout Uppercase, Newspaper Cutout Mixed Case, Dwarf, Dwarf II, Phonetic, Phonetic Rounded, Phonetic Light, Lower Upper Bold, Awesome

### leetspeak (1)
1337

### regional_scripts (23)
Greek, Greek v2, Russian, Russian v3, Ukrainian, Armenian, Georgian I, Georgian II, Tai Le, Tai Le v2, Tai Le v2 ft. Canadian Curly, Coptic Standard, Coptic Fancy, Turkish, Turkic, Vietnamese, Scammer, African Unicase 1982, Africa, Pan Nigerian, Mtavruli-Asomtavruli, Mtavruli-Nuskhuri, English Phonotypic

### effects (3)
Strikethrough, Strikethrough II, Flip

### fancy_mixed (20)
Classic, Smooth, Smooth v2, Palaeotype, Messletters 2005, Carrier, CarrierII, DraKo, Attila, Hazy, Hyves, Love, Stupid, Maniac, Twisted, Cranky, Slammer, Hodgepodge (fmr Tamil), Cryptic Fusion, Heroic Harmony

## Sample Output

Input: `Claire`

- **Math Sans-serif Bold:** 𝗖𝗹𝗮𝗶𝗿𝗲
- **Fullwidth:** Ｃｌａｉｒｅ
- **Circled:** ⓒⓛⓐⓘⓡⓔ
- **Circled Black:** 🅒🅛🅐🅘🅡🅔
- **Math Fraktur Bold:** 𝕮𝖑𝖆𝖎𝖗𝖊
- **Math Script (Royal):** 𝒞𝓁𝒶𝒾𝓇𝑒
- **Math Monospace:** 𝙲𝚕𝚊𝚒𝚛𝚎
- **Parenthesized:** ⒞⒧⒜⒤⒭⒠

## Usage Patterns

### Convert with execute_code
```python
import sys, os
skill_scripts = os.path.expanduser('~/.hermes/skills/messletters/scripts')
sys.path.insert(0, skill_scripts)
from messletters import convert
result = convert("Hello World", "Fullwidth")
print(result)  # Ｈｅｌｌｏ Ｗｏｒｌｄ
```

### User asks "what styles are available?"
Show categories and sample outputs. Group by category — don't list all 121 raw.

## Notes

- Non-ASCII characters (punctuation, spaces, emoji) pass through unchanged
- Some styles are **unicase** (upper=lower) — e.g., Japanese, Boxed Black, Carrier, Runes, Etruscan, Yi variants
- Digits don't map in all styles — they pass through as ASCII
- Strikethrough styles use combining characters — rendering depends on the platform/font
- `1337` is a leetspeak substitution cipher (a→4, e→3, i→1, o→0, s→5, t→7, z→2)
- CJK/Japanese styles map Latin characters to visually similar CJK characters — not a real transliteration
