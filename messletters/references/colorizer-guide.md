# Text Colorizer - Gradient HTML for Tumblr (Full Reference)

## What It Is

Generates Tumblr-compatible HTML with smooth color gradients across text. Each character (or word) gets wrapped in a `<span>` with an interpolated color. The result can be pasted directly into Tumblr's HTML editor.

Script: `scripts/colorize.py`

## CLI Usage

```bash
# 2-color gradient (char-by-char)
python3 scripts/colorize.py "Hello world" --start "#FF0000" --end "#0000FF"

# Named colors work too
python3 scripts/colorize.py "Hello" --start red --end blue

# Rainbow mode
python3 scripts/colorize.py "Hello world" --rainbow

# 3-color gradient
python3 scripts/colorize.py "Hello" --start "#FF0000" --middle "#00FF00" --end "#0000FF"

# Word-by-word gradient (each word gets one color instead of each char)
python3 scripts/colorize.py "Hello world" --start "#FF0000" --end "#0000FF" --word

# Solid color (no gradient)
python3 scripts/colorize.py "Hello" --start "#FF0000" --solid

# Random colors per character
python3 scripts/colorize.py "Hello" --random

# With formatting
python3 scripts/colorize.py "Hello" --start red --end blue --font Georgia --size 5 --bold --italic
```

## Options

- `--start COLOR` - gradient start color (hex `#FF0000` or named `red`)
- `--end COLOR` - gradient end color
- `--middle COLOR` - optional middle color for 3-stop gradients
- `--rainbow` - rainbow palette (ignores start/end)
- `--random` - random color per unit
- `--solid` - single color, no gradient
- `--word` - apply gradient word-by-word instead of char-by-char
- `--font FAMILY` - wrap in font-family (e.g. `Georgia`, `Arial`)
- `--size 1-7` - Tumblr font size scale (1=10px, 2=13px, 3=16px, 4=18px, 5=24px, 6=32px, 7=48px)
- `--bold` - wrap in `<b>`
- `--italic` - wrap in `<i>`

## Programmatic Usage (via execute_code)

```python
import sys, os
skill_scripts = os.path.expanduser('~/.hermes/skills/messletters/scripts')
sys.path.insert(0, skill_scripts)
from colorize import colorize, gradient_colors_2, parse_color

# Build colors programmatically
start = parse_color("#6E6B38")  # olive
end = parse_color("#961818")    # burgundy
text = "your text here"
colors = gradient_colors_2(len([c for c in text if c != ' ']), start, end)
result = colorize(text, colors)
print(result)
```

## Recoloring Existing Gradient HTML

To recolor an existing Tumblr bio/post that already has gradient spans:

1. Extract the text content (strip all `<span>` tags, keep inner text)
2. Re-run colorize with the new palette
3. The output replaces the old HTML entirely

There is no in-place recolor - it is always extract then regenerate.

## Saved Palettes

Projects usually accumulate their own palettes — one per character, blog or brand. When the user says "use X's colors" or "make it X's gradient," look the pair up in whatever palette note you keep for that project and use the start/end hex as the gradient endpoints. Never guess the hexes; if the palette is unrecorded, ask for the exact values.

## Gradient Bio Card Pattern

A common Tumblr bio layout:

```
[emojicombos prefix] WONKIFIED NAME [emojicombos suffix]
gradient subtitle / descriptor text
```

The name layer gets wonkified (messletters + wonkify technique), the subtitle gets gradient HTML (this colorizer), and emojicombos wraps the whole thing.

Pipeline: messletters -> wonkify -> text-colorizer -> emojicombos

## Character Bio Card Template Pattern

A structured multi-section character bio with decorative Unicode capitals, gradient headers, and color-coded structural elements. Common on Tumblr RP blogs.

### Structure

Each line: `[dash] [fancy cap][gradient rest-of-header] [brackets] [bold-first-letter content]`

```html
<b><span style="color: #82464e">&mdash;</span></b>&nbsp;
<span style="color: #68828b"><b>&#119821;</b></span>
<small><b><span style="color: #68828b">A</span><span style="color: #7e939b">M</span><span style="color: #a9b6bb">E</span></b></small>
<b><small>[</small></b> ... <b><small>]</small></b>
<b>f</b>irstname   <b><i>m</i></b><i>iddle</i>  <strike>lastname</strike>
```

### Key Rules

1. **Fancy cap + gradient: skip first letter.** When a decorative Unicode capital (𝐍, 𝐌, 𝐆, etc.) represents the first letter, the gradient spans start from the SECOND letter. Otherwise you get 𝐍NAME instead of 𝐍AME. The fancy char IS the first letter — don't duplicate it.

2. **Split headers = continuous gradient.** For multi-word headers like "DATE OF BIRTH" where each word gets its own decorative cap, the gradient runs continuously across the full label string (all letters in one interpolation), but skips the first letter of each word that has a decorative char.

3. **Header letter accuracy.** The decorative Unicode capital MUST match the actual first letter. Common mismatches to watch for: using 𝐏 for MORAL (should be 𝐌), 𝐁 for ALIGNMENT (should be 𝐀), 𝐅 for OCCUPATION (should be 𝐎). Always verify.

### Per-Label Independent Gradients

In some templates, each stat label (NAME, MEANING, DOB, etc.) gets its OWN gradient running from start→end independently. Each label restarts the interpolation from the start color. This is different from the continuous-gradient pattern above.

**When to use:** When the template has multiple short labels on separate lines, each one a few characters long. A continuous gradient across "NAME MEANING NICKNAMES DOB" would barely move the color per letter. Independent gradients give each label a full start→end sweep.

**Implementation:** For each label, generate `gradient_colors_2(len(label), start, end)` and wrap each letter in its own span. Bold the whole label with `<b>` if the template uses bold labels.

Example (multi-label template):
```html
<!-- Each label restarts from #544537 → #977f5d independently -->
<b><span style="color: #544537">N</span><span style="color: #594a3b">A</span><span style="color: #5e503f">M</span><span style="color: #635643">E</span></b>
<b><span style="color: #544537">M</span><span style="color: #594a3b">E</span><span style="color: #5e503f">A</span><span style="color: #635643">N</span><span style="color: #685b47">I</span><span style="color: #6d604b">N</span><span style="color: #72654f">G</span></b>
```

**Split-header note:** For multi-word labels like "PLACE OF BIRTH," the gradient runs across ALL letters continuously (P-L-A-C-E-O-F-B-I-R-T-H as one string), still starting fresh from the start color.

### Structural Colors vs Gradient Colors

Dashes (—, ▬), brackets ([ ... ]), arrows (➥, ›), and `...` separators are structural elements, NOT part of the gradient. Give them their own accent color:

- `▬` block markers: use a secondary structural color (e.g. `#b3aea6` warm gray)
- `—` em dashes and `➥` arrows: use the primary accent color (e.g. `#75624f`)
- `| | |` section separators: use the structural color
- `[ ... ]` bracket spacers: use the accent color

The decorative Unicode capital (𝐍, 𝐌, 𝐆) that opens each label is also accent-colored, NOT gradient. The gradient starts from the second character.

4. **Bold-first-letter content.** The fill-in content uses a pattern where the first letter of each word is bold (`<b>f</b>irstname`), sometimes with italic alternation for emphasis.

5. **Unicode reference.** The decorative caps are Mathematical Bold Italic (codepoints 119808–119833 = 𝐀–𝐙). Python: `chr(119808) = 𝐀`, `chr(119809) = 𝐁`, etc. For 𝐍 use `&#119821;` in HTML.

### Pipeline

For a full character template:
1. Define the gradient palette (start/end hex)
2. Define the structural accent color (dashes, brackets)
3. Generate gradient spans for each header (skip first letter, or first letter of each word for split headers)
4. Assemble with decorative caps, brackets, and placeholder content
5. Pipe to `pbcopy` or save to file — never dump in chat

## Notes

- Spaces are left bare (not wrapped in spans) - this prevents Tumblr from collapsing them
- Non-ASCII characters (punctuation, emoji, already-wonkified Unicode) pass through the span wrapping but do not consume gradient stops - only visible characters advance the gradient position
- The script handles CSS named colors (140+ entries), 3-digit hex shorthand, and 6-digit hex
- Tumblr font size uses a 1-7 scale that maps to pixel values; size 3 (16px) is the default on most themes
