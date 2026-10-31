#!/usr/bin/env python3
"""
Text Colorizer — Generate Tumblr-compatible gradient-colored HTML text.

Wraps each character in <span style='color:#XXXXXX;'>X</span> tags with
smooth color interpolation. Spaces are left bare between span groups.

Usage:
  python3 colorize.py "Hello world" --start "#FF0000" --end "#0000FF"
  python3 colorize.py "Hello world" --start red --end blue
  python3 colorize.py "Hello world" --rainbow
  python3 colorize.py "Hello world" --start "#FF0000" --end "#0000FF" --word
  python3 colorize.py "Hello world" --start "#FF0000" --end "#0000FF" --font Georgia --size 5 --bold --italic
"""

import argparse
import random
import re
import sys

# CSS3 named colors (subset — most commonly used for tumblr)
CSS_COLORS = {
    "aliceblue": "#F0F8FF", "antiquewhite": "#FAEBD7", "aqua": "#00FFFF",
    "aquamarine": "#7FFFD4", "azure": "#F0FFFF", "beige": "#F5F5DC",
    "bisque": "#FFE4C4", "black": "#000000", "blanchedalmond": "#FFEBCD",
    "blue": "#0000FF", "blueviolet": "#8A2BE2", "brown": "#A52A2A",
    "burlywood": "#DEB887", "cadetblue": "#5F9EA0", "chartreuse": "#7FFF00",
    "chocolate": "#D2691E", "coral": "#FF7F50", "cornflowerblue": "#6495ED",
    "cornsilk": "#FFF8DC", "crimson": "#DC143C", "cyan": "#00FFFF",
    "darkblue": "#00008B", "darkcyan": "#008B8B", "darkgoldenrod": "#B8860B",
    "darkgray": "#A9A9A9", "darkgreen": "#006400", "darkkhaki": "#BDB76B",
    "darkmagenta": "#8B008B", "darkolivegreen": "#556B2F", "darkorange": "#FF8C00",
    "darkorchid": "#9932CC", "darkred": "#8B0000", "darksalmon": "#E9967A",
    "darkseagreen": "#8FBC8F", "darkslateblue": "#483D8B", "darkslategray": "#2F4F4F",
    "darkturquoise": "#00CED1", "darkviolet": "#9400D3", "deeppink": "#FF1493",
    "deepskyblue": "#00BFFF", "dimgray": "#696969", "dodgerblue": "#1E90FF",
    "firebrick": "#B22222", "floralwhite": "#FFFAF0", "forestgreen": "#228B22",
    "fuchsia": "#FF00FF", "gainsboro": "#DCDCDC", "ghostwhite": "#F8F8FF",
    "gold": "#FFD700", "goldenrod": "#DAA520", "gray": "#808080",
    "green": "#008000", "greenyellow": "#ADFF2F", "honeydew": "#F0FFF0",
    "hotpink": "#FF69B4", "indianred": "#CD5C5C", "indigo": "#4B0082",
    "ivory": "#FFFFF0", "khaki": "#F0E68C", "lavender": "#E6E6FA",
    "lavenderblush": "#FFF0F5", "lawngreen": "#7CFC00", "lemonchiffon": "#FFFACD",
    "lightblue": "#ADD8E6", "lightcoral": "#F08080", "lightcyan": "#E0FFFF",
    "lightgoldenrodyellow": "#FAFAD2", "lightgray": "#D3D3D3", "lightgreen": "#90EE90",
    "lightpink": "#FFB6C1", "lightsalmon": "#FFA07A", "lightseagreen": "#20B2AA",
    "lightskyblue": "#87CEFA", "lightslategray": "#778899", "lightsteelblue": "#B0C4DE",
    "lightyellow": "#FFFFE0", "lime": "#00FF00", "limegreen": "#32CD32",
    "linen": "#FAF0E6", "magenta": "#FF00FF", "maroon": "#800000",
    "mediumaquamarine": "#66CDAA", "mediumblue": "#0000CD", "mediumorchid": "#BA55D3",
    "mediumpurple": "#9370DB", "mediumseagreen": "#3CB371", "mediumslateblue": "#7B68EE",
    "mediumspringgreen": "#00FA9A", "mediumturquoise": "#48D1CC", "mediumvioletred": "#C71585",
    "midnightblue": "#191970", "mintcream": "#F5FFFA", "mistyrose": "#FFE4E1",
    "moccasin": "#FFE4B5", "navajowhite": "#FFDEAD", "navy": "#000080",
    "oldlace": "#FDF5E6", "olive": "#808000", "olivedrab": "#6B8E23",
    "orange": "#FFA500", "orangered": "#FF4500", "orchid": "#DA70D6",
    "palegoldenrod": "#EEE8AA", "palegreen": "#98FB98", "paleturquoise": "#AFEEEE",
    "palevioletred": "#DB7093", "papayawhip": "#FFEFD5", "peachpuff": "#FFDAB9",
    "peru": "#CD853F", "pink": "#FFC0CB", "plum": "#DDA0DD",
    "powderblue": "#B0E0E6", "purple": "#800080", "rebeccapurple": "#663399",
    "red": "#FF0000", "rosybrown": "#BC8F8F", "royalblue": "#4169E1",
    "saddlebrown": "#8B4513", "salmon": "#FA8072", "sandybrown": "#F4A460",
    "seagreen": "#2E8B57", "seashell": "#FFF5EE", "sienna": "#A0522D",
    "silver": "#C0C0C0", "skyblue": "#87CEEB", "slateblue": "#6A5ACD",
    "slategray": "#708090", "snow": "#FFFAFA", "springgreen": "#00FF7F",
    "steelblue": "#4682B4", "tan": "#D2B48C", "teal": "#008080",
    "thistle": "#D8BFD8", "tomato": "#FF6347", "turquoise": "#40E0D0",
    "violet": "#EE82EE", "wheat": "#F5DEB3", "white": "#FFFFFF",
    "whitesmoke": "#F5F5F5", "yellow": "#FFFF00", "yellowgreen": "#9ACD32",
}


def parse_color(color_str):
    """Parse a color string (hex or named) into (r, g, b) tuple."""
    color_str = color_str.strip()
    
    # Named color
    lower = color_str.lower()
    if lower in CSS_COLORS:
        color_str = CSS_COLORS[lower]
    
    # Hex color
    if color_str.startswith("#"):
        hex_str = color_str[1:]
        if len(hex_str) == 3:
            hex_str = hex_str[0]*2 + hex_str[1]*2 + hex_str[2]*2
        if len(hex_str) != 6:
            raise ValueError(f"Invalid hex color: {color_str}")
        return (int(hex_str[0:2], 16), int(hex_str[2:4], 16), int(hex_str[4:6], 16))
    
    raise ValueError(f"Cannot parse color: {color_str}. Use hex (#FF0000) or named (red, blue, etc.)")


def rgb_to_hex(r, g, b):
    """Convert (r, g, b) to hex string like #FF0000."""
    return f"#{int(r):02X}{int(g):02X}{int(b):02X}"


def lerp_color(c1, c2, t):
    """Linearly interpolate between two (r, g, b) colors. t in [0, 1]."""
    return (
        c1[0] + (c2[0] - c1[0]) * t,
        c1[1] + (c2[1] - c1[1]) * t,
        c1[2] + (c2[2] - c1[2]) * t,
    )


def gradient_colors_2(n, start, end):
    """Generate n colors interpolating from start to end."""
    if n <= 0:
        return []
    if n == 1:
        return [rgb_to_hex(*start)]
    return [rgb_to_hex(*lerp_color(start, end, i / (n - 1))) for i in range(n)]


def gradient_colors_3(n, start, mid, end):
    """Generate n colors interpolating start → mid → end."""
    if n <= 0:
        return []
    if n == 1:
        return [rgb_to_hex(*start)]
    half = (n - 1) / 2.0
    colors = []
    for i in range(n):
        if i <= half:
            t = i / half if half > 0 else 0
            colors.append(rgb_to_hex(*lerp_color(start, mid, t)))
        else:
            t = (i - half) / ((n - 1) - half) if (n - 1) > half else 1
            colors.append(rgb_to_hex(*lerp_color(mid, end, t)))
    return colors


def rainbow_colors(n):
    """Generate n colors across the rainbow (red → violet)."""
    if n <= 0:
        return []
    rainbow_rgb = [
        (255, 0, 0),    # red
        (255, 127, 0),  # orange
        (255, 255, 0),  # yellow
        (0, 255, 0),    # green
        (0, 0, 255),    # blue
        (75, 0, 130),   # indigo
        (148, 0, 211),  # violet
    ]
    if n == 1:
        return [rgb_to_hex(*rainbow_rgb[0])]
    
    colors = []
    segments = len(rainbow_rgb) - 1
    for i in range(n):
        t = i / (n - 1) * segments
        seg = min(int(t), segments - 1)
        seg_t = t - seg
        colors.append(rgb_to_hex(*lerp_color(rainbow_rgb[seg], rainbow_rgb[seg + 1], seg_t)))
    return colors


def random_colors(n):
    """Generate n random colors."""
    return [rgb_to_hex(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(n)]


# Tumblr font size mapping (1-7 scale to px)
SIZE_MAP = {1: 10, 2: 13, 3: 16, 4: 18, 5: 24, 6: 32, 7: 48}


def colorize(text, colors):
    """Apply colors to text characters. Spaces are left bare."""
    parts = []
    color_idx = 0
    non_space_count = 0
    
    for ch in text:
        if ch == " ":
            parts.append(" ")
        else:
            c = colors[non_space_count % len(colors)] if non_space_count < len(colors) else colors[-1]
            parts.append(f"<span style='color:{c};'>{ch}</span>")
            non_space_count += 1
    
    return "".join(parts)


def colorize_words(text, colors):
    """Apply colors to whole words. Each word gets one color."""
    words = text.split(" ")
    parts = []
    for i, word in enumerate(words):
        c = colors[i % len(colors)] if i < len(colors) else colors[-1]
        if word:
            parts.append(f"<span style='color:{c};'>{word}</span>")
        if i < len(words) - 1:
            parts.append(" ")
    return "".join(parts)


def main():
    parser = argparse.ArgumentParser(description="Generate gradient-colored HTML text for Tumblr")
    parser.add_argument("text", help="Text to colorize")
    parser.add_argument("--start", default="#FF0000", help="Start color (hex or named)")
    parser.add_argument("--end", default="#0000FF", help="End color (hex or named)")
    parser.add_argument("--middle", default=None, help="Middle color for 3-color gradient (hex or named)")
    parser.add_argument("--rainbow", action="store_true", help="Use rainbow colors")
    parser.add_argument("--random", action="store_true", help="Use random colors per character/word")
    parser.add_argument("--solid", action="store_true", help="Use start color as solid (no gradient)")
    parser.add_argument("--word", action="store_true", help="Apply gradient word-by-word instead of char-by-char")
    parser.add_argument("--font", default=None, help="Font family (e.g. Georgia, Arial)")
    parser.add_argument("--size", type=int, default=None, choices=range(1, 8), help="Font size 1-7")
    parser.add_argument("--bold", action="store_true", help="Bold text")
    parser.add_argument("--italic", action="store_true", help="Italic text")
    
    args = parser.parse_args()
    
    # Parse colors
    start = parse_color(args.start)
    end = parse_color(args.end)
    mid = parse_color(args.middle) if args.middle else None
    
    # Count units for color generation
    if args.word:
        units = [w for w in args.text.split(" ") if w]  # non-empty words
    else:
        units = [c for c in args.text if c != " "]  # non-space chars
    
    n = len(units)
    
    # Generate color palette
    if args.rainbow:
        colors = rainbow_colors(n)
    elif args.random:
        colors = random_colors(n)
    elif args.solid:
        colors = [rgb_to_hex(*start)] * n
    elif mid is not None:
        colors = gradient_colors_3(n, start, mid, end)
    else:
        colors = gradient_colors_2(n, start, end)
    
    # Apply colors
    if args.word:
        result = colorize_words(args.text, colors)
    else:
        result = colorize(args.text, colors)
    
    # Wrap with formatting
    if args.bold:
        result = f"<b>{result}</b>"
    if args.italic:
        result = f"<i>{result}</i>"
    
    # Outer wrapper for font/size
    style_parts = []
    if args.font:
        style_parts.append(f"font-family:{args.font}")
    if args.size:
        px = SIZE_MAP.get(args.size, 16)
        style_parts.append(f"font-size:{px}px")
    
    if style_parts:
        result = f'<span style="{"; ".join(style_parts)};">{result}</span>'
    
    print(result)


if __name__ == "__main__":
    main()
