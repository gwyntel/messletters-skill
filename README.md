[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/gwyntel/messletters-skill)
# messletters

Convert text into 121+ Unicode fancy text styles — math alphabets, scripts, symbols, decorative, encircled, runic, and more. Zero dependencies. Single file.

Extracted from [messletters.com](https://www.messletters.com/en/).

## Install

Prerequisite: Node.js 22.20 or later.

This repository keeps the skill in `messletters/SKILL.md`; select that skill by name when installing with the Vercel `skills` CLI:

```bash
npx skills add gwyntel/messletters-skill --skill messletters --agent hermes-agent -g -y
```

The install is global for the selected agent. The CLI discovers the nested skill directory; do not move `SKILL.md` to the repository root.

## Use

Once installed, ask your agent to convert text using a named style (for example, “convert Hello to Math Sans-serif Bold”) or import the bundled Python module as shown below. Python usage requires the skill's `scripts` directory on `sys.path`; locate it through your host agent's skill metadata/configuration (for a global Hermes install, this is typically `~/.hermes/skills/messletters/scripts`; other agents' locations vary). No Hermes-specific tool is required; without Python/shell execution, an agent can still use the mapping instructions and provide the result directly.

## Update

Update a skill installed from the GitHub repository with:

```bash
npx skills update messletters
```

If the CLI reports that no matching installation is tracked, run the install command above again to install/update the selected skill from its canonical source. Local-path installs may not be tracked for source-based updates.

For CLI options, see [Vercel skills](https://github.com/vercel-labs/skills).

---

**Hermes-native installer (alternative):** `hermes skills install gwyntel/messletters/messletters`. This is separate from the Vercel CLI and may use a different install location.

---

## Quick Start: Python

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
