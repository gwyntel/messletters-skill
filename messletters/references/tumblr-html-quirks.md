# Tumblr Post Editor HTML Quirks

Hard-won lessons from editing HTML in Tumblr's post editor (not theme HTML — the actual post editor's HTML view `</>`).

## What Survives Tumblr's Post Editor

| Element | `style` attr works? | Notes |
|---|---|---|
| `<span>` | ✅ Yes | Most reliable carrier for inline color |
| `<small>` | ✅ Yes | Works fine with style |
| `<b>`, `<i>` | ✅ Yes | Works fine with style |
| `<strike>` | ✅ Yes | Strikethrough preserved |
| `<a>` (links) | ❌ **No — STRIPPED** | Tumblr strips `style` from `<a>` tags on save. The link reverts to tumblr blue. |
| `<font color>` | ⚠️ Unreliable | Deprecated HTML, sometimes works but not consistent across tumblr contexts |

## The Link Color Problem & Fix

**Problem:** Tumblr's post editor strips `style="color:..."` from `<a>` tags. Links revert to tumblr's default blue regardless of what you set.

**Wrong approaches (do NOT use):**
- `<a style="color: #939393" href="...">text</a>` — style gets stripped
- `<a href="..."><span style="color: #939393">text</span></a>` — close but fragile; the `<a>` wrapper can still override child span in some tumblr rendering contexts
- `<font color="#939393"><a href="...">text</a></font>` — deprecated, unreliable

**Reliable fix — wrap the `<a>` INSIDE a `<span style>`:**
```html
<span style="color: #939393"><a href="https://example.com">link text</a></span>
```
The span forces the color and the link inherits it. This survives tumblr's save cycle consistently.

## Style Format Notes

- `color:#939393` (no space after colon) tends to survive better than `color: #939393` (with space). Tumblr's parser is finicky.
- Match tumblr's own output format when possible: `<span style="color: #hex">` with lowercase hex.

## When User Provides Their Own HTML Structure

**Critical:** When the user provides HTML they've already structured and asks for a specific edit (e.g. "change these colors"), do NOT restructure the HTML. Make only the requested change within their existing tag structure. They may have tested it against tumblr's save cycle already.

Pattern from this session:
1. User provides working HTML
2. Asks for specific color swap (e.g. "make the lighter pinks #796d54")
3. Do simple find-and-replace on the hex values only
4. Do NOT refactor tags, consolidate spans, or "clean up" the structure
5. If using terminal `sed`, verify count of old → new color replacements to confirm the swap

## Batch Color Replacement

For multi-color swaps across large HTML blocks, use terminal `sed`:
```bash
cat input.html | sed 's/#9e6672/#796d54/g; s/#5f424c/#3e0000/g' > output.html
```
Then verify:
```bash
grep -c '#9e6672\|#5f424c' output.html  # should be 0
grep -c '#796d54' output.html            # new color count
grep -c '#3e0000' output.html            # new color count
```

This is faster and more reliable than manual editing for large muse lists with many repeated color values.

## Tumblr Theme HTML vs Post Editor HTML

These are different contexts with different rules:
- **Theme HTML editor** (Edit HTML in blog settings) — full HTML/CSS support, `style` attrs are reliable, `<style>` blocks work
- **Post editor HTML view** (the `</>` toggle) — aggressive style stripping, especially on `<a>` tags. `style` works on spans/small/b but NOT on links.
- **Post editor rich text** — strips everything, do not use for styled HTML

Always ask which context if unclear. The link-coloring problem only occurs in the post editor.
