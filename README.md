[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/gwyntel/messletters-skill)
# messletters

Convert text into 121+ Unicode fancy text styles — math alphabets, scripts, symbols, decorative, encircled, runic, and more. Zero dependencies. Single file.

Extracted from [messletters.com](https://www.messletters.com/en/).

## Install

Install globally for Hermes Agent (or another supported agent):

```bash
npx skills add gwyntel/messletters-skill --skill messletters --agent hermes-agent -g -y
```

For other supported agents, replace `hermes-agent` with the target agent name. Browse installers with `npx skills add gwyntel/messletters-skill --list`.

Hermes-native installation is separate from the Vercel skills CLI; use the repository's `messletters/SKILL.md` content with Hermes' skill installation workflow if you do not use the Vercel CLI.

## Quick Start

```python
from messletters import convert, search_styles

# Convert text to a fancy style
convert("Hello World", "Math Sans-serif Bold")
# → 𝗛𝗲𝗹𝗹𝗼 𝗪𝗼𝗿𝗹𝗱

convert("Claire", "Circled")
# → ⓒⓛⓐⓘⓡⓔ

convert("Love you 3000", "Math Fraktur Bold")
# → 𝕃𝖔𝖛𝖊 𝖞𝖔𝖚 𝟯𝟬𝟬𝟬

# Search for styles
search_styles("fraktur")
# → ['Math Fraktur Bold', 'Math Fraktur Bold - Edit', 'Math Fraktur Normal', 'Math Fraktur Normal - Edit']
```

## Update

For a reliable update from this GitHub repository, install the latest version again:

```bash
npx skills add gwyntel/messletters-skill --skill messletters --agent hermes-agent -g -y
```

The Vercel CLI's `skills update` command updates sources recorded in its install registry; installs from a local repository path may not be tracked. If you installed from a local clone, rerun `npx skills add /path/to/messletters-skill --skill messletters --agent hermes-agent -g -y` after pulling the repository. For other agent paths, use the same installer with the appropriate `--agent` target.

## API

- **`convert(text, style)`** → converted string
- **`list_styles()`** → all 121 style names
- **`search_styles(query)`** → case-insensitive substring search
- **`preview_styles(text)`** → all styles applied to text
- **`reverse_lookup(char)`** → which styles produce a character
- **`CATEGORIES`** → dict of category → style names
- **`STYLES`** → raw codepoint data

## Categories

- **mathematical** (17) — Math Script, Monospace, Sans-serif Bold, Fraktur, Serif variants
- **enclosed** (6) — Circled, Boxed, Parenthesized, Fullwidth
- **script_cursive** (14) — Lilia, Yas Script, Cute v1/v2/v3, Curly, Ribbon
- **gothic_runes** (5) — Runes, Gothic, Celtic, Black Panther, Etruscan
- **asian_scripts** (14) — Japanese, CJK, Yi variants, Malayalam, Cherokee Mystique
- **decorative** (18) — Messletters, Swirly, Wiggly, Dotted, Phonetic
- **leetspeak** (1) — 1337
- **regional_scripts** (23) — Greek, Russian, Armenian, Turkish, Vietnamese
- **effects** (3) — Strikethrough, Flip
- **fancy_mixed** (20) — Classic, Smooth, Palaeotype, DraKo, Love, Twisted

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

## License

MutuaL-1.2 © 2026 GwynTel
