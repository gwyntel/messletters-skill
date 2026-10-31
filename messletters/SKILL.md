---
name: messletters
description: Convert text into 121+ Unicode fancy text styles — math alphabets, scripts, symbols, decorative, encircled, runic, and more. Extracted from messletters.com. Includes wonkify (chaotic font mixing), a gradient text colorizer for Tumblr, and copy-safe delivery of fancy strings in chat.
version: 1.1.0
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

## Module

Bundled at `scripts/messletters.py` within this skill. The example below runs with the default global Hermes Agent installation. If installed elsewhere or on another host, replace that path with the actual skill directory reported by your agent's skill metadata/configuration; keep `scripts` as the final component. No host path is assumed outside the explicitly labeled Hermes example.

## Import

```python
from pathlib import Path
import sys

# Hermes Agent global install default; change this for your host/install scope.
skill_dir = Path.home() / ".hermes" / "skills" / "messletters"
sys.path.insert(0, str(skill_dir / "scripts"))
from messletters import convert, search_styles, list_styles, preview_styles, reverse_lookup, CATEGORIES, STYLES

print(convert("Hello World", "Math Sans-serif Bold"))
```

Agent tools differ. Use the host's Python/shell execution capability, or provide the style mapping/result directly when code execution is unavailable. This skill needs no Hermes-specific tool.

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

### Identifying an unknown fancy string
Run `reverse_lookup` on one character of the string to get candidate styles, then `convert` the plain word in each candidate and compare. Common confusions:

- **Math Serif Bold Italic** (`𝒔𝒆𝒆𝒅𝒃𝒐𝒙`) is a *serif* italic — elegant, reads as script to most eyes.
- **Math Script (Royal) Bold** (`𝓼𝓮𝓮𝓭𝓫𝓸𝔁`) is the true flowing script.
- **Math Monospace** (`𝚜𝚎𝚎𝚍𝚋𝚘𝚡`) is the typewriter slab.

Check the codepoint before guessing: 1D434–1D467 italic, 1D468–1D49B bold italic, 1D4D0–1D503 bold script, 1D670–1D6A3 monospace.

## Wonkify — Chaotic Font Mixing

Turn plain text into a glitchy font-stew by cycling through multiple messletters styles character-by-character, interspersing decorative Unicode markers, combining characters, and small caps. This is NOT uniform font conversion — it's deliberate aesthetic chaos.

**Core technique:** Cycle fonts per character (never repeat same style on adjacent chars), sprinkle Dwarf as "noise", add combining character accents (͟ strikethrough, ̲ underline), mix in small caps, wrap with decorative markers.

**Font roster for wonkification:** Math Script (Royal) Bold, Math Sans-serif Bold, Math Fraktur Bold, Math Serif Bold, Math Serif Italic, Math Sans-serif Italic, Math Serif Bold Italic, Math Fraktur Normal, Math Sans-serif Bold Italic, Math Monospace, Dwarf, Dwarf II.

**Examples:**
- `rockstar queen` → `✮ ◜ 𝓡ᵒ𝕮𝑘s𝐭ₐʳ ‎ ‎𝓠uᴱ𝔢𝒏`
- `guitar` → `𝓖uⁱt𝓪𝓻is𝑡`

Full reference: `references/wonkify-guide.md`

## EmojiCombos — Decorative Symbol Combinations

Curated encyclopedia of symbol combinations for decorating text, wonkifying names, and building Tumblr/RP display aesthetics. Combines prefix decorations, suffix endmarks, borders/wrappers, flourish separators, star/sparkle accents, cute kaomoji, glitch/void effects, and nature elements.

**House style: symbols over emoji.** When choosing decorative elements, reach for pure Unicode symbols († ♱ ⋆ ཐི ཋྀ ⛧ ࿔ ♡ ✧ ✮ ◜) rather than emoji characters. The target is gothic / alt / fairy-grunge — text that looks handmade and feral, not sticker-decorated. Emojis are acceptable sparingly, never as the dominant decoration.

**Integration pattern:** Use emojicombos for borders/flourishes/markers, messletters for font mixing within the text. Pipeline: messletters → emojicombos wrapping → text-colorizer for gradient.

`references/emojicombos.md` covers using [emojicombos.com](https://emojicombos.com/) as a live discovery tool — navigate to `emojicombos.com/<search-term>` and skim with your browser tool. Prefer symbol-forward searches (`divider-symbols`, `separator`, `alt-symbols`) over emoji-heavy ones. Keep your own static combos file as you collect favourites; the live site is the source, a local file is the shortcut.

## Text Colorizer — Gradient HTML for Tumblr

Generates Tumblr-compatible HTML with smooth color gradients across text. Each `<span>` gets an interpolated color. Supports 2-color, 3-color, rainbow, solid, and random modes.

**⚠ Tumblr post editor HTML quirks:** When editing HTML for Tumblr's **post editor** (not theme HTML), inline `style` on `<a>` tags gets STRIPPED on save — links revert to tumblr blue. The fix is wrapping `<a>` inside `<span style="color:...">`. Also: never restructure user-provided HTML without being asked. Full reference: `references/tumblr-html-quirks.md`

```bash
python3 scripts/colorize.py "YOUR TEXT" --start "#FF0000" --end "#0000FF"
python3 scripts/colorize.py "Hello world" --rainbow
```

Additional options: `--font`, `--size`, `--bold`, `--italic`, `--word` (word-by-word gradient).

Also supports recoloring existing gradient HTML and gradient labels for bios. See `references/colorizer-guide.md` for the full recoloring algorithm and card patterns.

## Combining Pipeline

The full wonkification pipeline chains all modes:
1. **messletters** — convert text to fancy Unicode fonts FIRST
2. **wonkify** — cycle multiple fonts per character for chaotic mixing
3. **text-colorizer** — apply gradient HTML colors to the result
4. **emojicombos** — add decorative prefixes/suffixes/borders around the final text

## Delivery in Chat

### Copiable Unicode strings → fenced code block

Any fancy-Unicode string the user is meant to **copy** (channel name, display name, bio line, tag) ships inside a plain triple-backtick fence, even when the string is a single word. Discord mobile gives the block a copy button and takes the whole string exactly; hand-selecting bare fancy text loses glyphs and picks up stray whitespace. Keep the fence to the string alone — font name, reasoning and alternatives go in the prose around it, never inside.

### HTML → pbcopy

When generating HTML (gradient text, bio cards, character templates), **pipe to `pbcopy` by default** — never dump raw HTML inline in chat. Discord cannot render HTML and copying from chat output is nearly impossible. Fall back to saving a file and telling the user the path.

```bash
python3 -c "..." | pbcopy
```

The only exception is when the user explicitly asks to see the HTML source in chat.

## Chat Platform Channel Names

On servers where the font is used to encode which section a channel belongs to, read the neighbourhood before converting anything.

1. **Read the live channel list first — never style blind.** Ask the platform API for the guild's channels (e.g. `GET /guilds/<guild_id>/channels` with a bot token). A local channel cache maintained by the agent is not that list: it only holds channels the agent has exchanged traffic in and omits media/forum channels entirely, so it will show a section's threads but not the channel they hang off.
2. **Match the font family already in that section.** Typical mapping:
   - persona / character channels → **Math Script (Royal) Bold**, flowing script
   - themed / scenario channels → **Math Monospace**, lowercase and hyphenated
   - notification channels → **bold caps + decoration**, e.g. `𝐍𝐎𝐓𝐈𝐅𝐒⏖notifs﹐`
   "Monospace like my other channels" means Math Monospace in the local lowercase-and-hyphen shape — not the persona script font, even when the persona channel is the one named after the agent.
3. **Shape:** lowercase, no spaces; multi-word names join with a hyphen to mirror how the platform renders ASCII channel names.
4. **Deliver** the raw string in a fenced code block and offer to create the channel. Creating or renaming server structure is the user's call — hand over the string, don't restructure the server unasked.

## Notes

- Non-ASCII characters (punctuation, spaces, emoji) pass through unchanged
- Some styles are **unicase** (upper=lower) — e.g., Japanese, Boxed Black, Carrier, Runes, Etruscan, Yi variants
- Digits don't map in all styles — they pass through as ASCII
- Strikethrough styles use combining characters — rendering depends on the platform/font
- `1337` is a leetspeak substitution cipher (a→4, e→3, i→1, o→0, s→5, t→7, z→2)
- CJK/Japanese styles map Latin characters to visually similar CJK characters — not a real transliteration
