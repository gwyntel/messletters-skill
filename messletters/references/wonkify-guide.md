# Wonkify — Chaotic Unicode Font Mixing (Full Reference)

## What It Is

Wonkification turns plain text into a glitchy font-stew by cycling through multiple messletters styles character-by-character, interspersing decorative Unicode markers, combining characters, and small caps. This is NOT uniform font conversion — it's deliberate aesthetic chaos.

The target aesthetic is Tumblr/RP display names, playlist titles, bio labels — places where the text needs to feel handmade and feral, not cleanly typeset.

## Font Roster

These are the styles that mix well for wonkification. They're chosen for visual contrast — serif vs sans, script vs fraktur, upright vs italic — so adjacent characters feel distinctly different.

- **Math Sans-serif Bold** — clean geometric bold (𝗮𝗯𝗰)
- **Math Serif Bold** — classic serif bold (𝐚𝐛𝐛)
- **Math Serif Italic** — elegant italic (𝑎𝑏𝑐)
- **Math Serif Bold Italic** — bold+italic (𝒂𝒃𝒄)
- **Math Script (Royal) Bold** — calligraphic bold (𝓪𝓫𝓬)
- **Math Sans-serif Italic** — slanted geometric (𝘢𝘣𝘤)
- **Math Sans-serif Bold Italic** — bold slanted geometric (𝙖𝙗𝙘)
- **Math Fraktur Bold** — gothic bold (𝖆𝖇𝖈)
- **Math Fraktur Normal** — gothic regular (𝔞𝔟𝔠)
- **Math Monospace** — fixed-width (𝚊𝚋𝚌)
- **Dwarf** — decorative small (custom messletters style)
- **Dwarf II** — decorative small variant

## Core Technique

1. **Cycle fonts per character**, never repeating the same style on adjacent characters. The rotation should feel random but not actually be random — pick 3-5 styles and cycle through them with slight variation.

2. **Sprinkle Dwarf/Dwarf II as "noise"** — swap a character or two into Dwarf for visual texture breaks. Not every word, just enough to make it feel unglued.

3. **Add combining character accents** for glitch:
   - `͟` (combining double low line / strikethrough) — placed after a char: `ᴱ͟`
   - `̲` (combining low line / underline) — `E̲`
   - `̷` (combining short stroke overlay) — `E̷`
   - Stack multiple: `ᴱ̷̲͟`

4. **Mix in small caps** for variety — superscript-sized characters like `ᵐʸ`, `ˢᵒᴺ`, `ᴱ͟`. These work great for short function words ("my", "the", "so") where full fancy-font feels too heavy.

5. **Wrap with decorative markers** from the emojicombos reference:
   - Prefix: `⋆.`, `✮ ◜`, `˗ˏˋ`, `✧`, `✮`
   - Suffix: `.ᐟ`, `˚⋆`, `ˎˊ˗`, `⋆˚`, `♡˚`
   - Borders: `˗ˏˋ ... ˎˊ˗`, `꒰ა ♡ ໒꒱`

6. **Add hearts and sparkles** as garnish (not structural): `♡`, `♥`, `✧`, `⋆`, `✮`

## Style Mixing Rules of Thumb

- **Contrast is the goal.** Serif Italic next to Sans-serif Bold next to Fraktur — the jarring jumps are the point.
- **Don't wonkify every single character.** Natural-looking wonkification has "rest" characters — maybe 1 in 5 stays as a superscript/small cap while neighbors go full font.
- **Short text = simpler mix.** A two-word title like "my karma" only needs 2-3 font styles cycled, plus a decorative wrapper. Don't overcomplicate short strings.
- **Longer text = more chaos room.** Full sentences or display names can layer combining chars, dwarf noise, brackets, and emojicombos borders.

## Programmatic Wonkification (messletters.py)

For batch or systematic wonkification, use the messletters Python module:

```python
import sys, os
skill_scripts = os.path.expanduser('~/.hermes/skills/messletters/scripts')
sys.path.insert(0, skill_scripts)
from messletters import convert, search_styles

# Convert the full string to a single style as a base
base = convert("my karma", "Math Script (Royal) Bold")
# → 𝓶𝔂 𝓴𝓪𝓻𝓶𝓪

# Then manually remix individual characters with other styles
# (no automated wonkify function yet — the technique is intentionally hand-crafted)
```

Note: There is no `wonkify()` function in messletters.py. Wonkification is inherently a creative, hand-crafted process. The module provides the building blocks (style conversion, style search); the mixing is done by feel.

## Examples

**Short title: "my karma <3"**
- `⋆ ᵐʸ 𝘬𝒶𝕣ᵐᵃ ♡˚` — small caps for "my", mixed serif italic + fraktur bold + serif bold for "karma", heart+degree suffix
- `✧ ᵐᵎ 𝓴𝒜𝘳𝵐𝙖 <3 ⋆˚` — superscript mix for "my", script bold + serif italic + fraktur for "karma", sparkle wrapper
- `˗ˏˋ ᵐʸ 𝘬𝒶𝕣𝵐𝒶 ♡ ˎˊ˗` — clean border wrapper, small caps + serif italic + fraktur + serif bold cycle
- `✮ ᵐʸ 𝘬𝙖𝕣ₘ𝒶 ♡⋆` — minimal prefix/suffix, sans-serif italic + fraktur + subscript + serif bold

**Display name: "rockstar queen"**
- `✮ ◜ 𝓡ᵒ𝕮𝑘s𝐭ₐʳ ‎ ‎𝓠uᴱ𝔢𝒏`

**Display name: "guitarist"**
- `𝓖uⁱt𝓪𝓻is𝑡`

**Full bio label:**
- `𝐎𝒽,⠀[ 𝘛̲𝘏̲𝘈̲𝘕̲𝘒̲ ̲𝘎̲𝘖̲𝘋̲ ]⠀I 𝓢ᴼᴸᴅ MY 𝓢OUL⠀—    𝟺⠀Ꮐᴸ͟ᴵ͟ᵀ͟ᵀ͟ᴇ͟ᴿ͟,⠀Ꭰ𝚁𝚄𝙶𝚂⠀[ 𖬺 ]⠀𝐑𝐎𝐂𝐊 𖬺 𝑹𝑶̲𝑳̲𝑳̲ .ᐟ`

## Pipeline Integration

The full wonkification pipeline chains all messletters modes:

1. **messletters** — convert text to fancy Unicode fonts FIRST
2. **wonkify** — cycle multiple fonts per character for chaotic mixing
3. **text-colorizer** — apply gradient HTML colors to the result (for Tumblr bios/posts)
4. **emojicombos** — add decorative prefixes/suffixes/borders around the final text

See also:
- Emoji combos: `references/emojicombos.md` (live search) plus your own saved combos file
- Colorizer reference: `references/colorizer-guide.md`
