#!/usr/bin/env python3
"""
Genererer de 6 item-sprites (16x16) til Dansk Delight.

Alle sprites er tegnet fra bunden som pixel-art i kode (ASCII-kort + små
tegnefunktioner). Der er ikke kopieret billeder fra nettet, så der ikke er
nogen ophavsretlige problemer - du kan frit redigere farverne herunder.

Kør:  python3 tools/make_textures.py        (kræver: pip install pillow)
"""
import os
from PIL import Image

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "src", "main",
                   "resources", "assets", "danskdelight", "textures", "item")

K = "#2a1a0e"  # fælles outline-farve


def hexc(h):
    h = h.lstrip("#")
    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)


class Canvas:
    def __init__(self):
        self.px = [[None] * 16 for _ in range(16)]

    def put(self, x, y, c):
        if 0 <= x < 16 and 0 <= y < 16 and c:
            self.px[y][x] = c

    def ascii(self, rows, pal, min_row=0, max_row=15):
        assert len(rows) == 16
        for y, row in enumerate(rows):
            assert len(row) == 16, f"række {y}: {len(row)}"
            if y < min_row or y > max_row:
                continue
            for x, ch in enumerate(row):
                if ch != ".":
                    self.put(x, y, pal[ch])

    def ellipse(self, cx, cy, rx, ry, fill, outline=None, hi=None, lo=None):
        """Udfyldt ellipse. outline=None -> kun skygge/highlight (ingen sort kant)."""
        def inside(x, y):
            return ((x - cx) / rx) ** 2 + ((y - cy) / ry) ** 2 <= 1.0
        for y in range(16):
            for x in range(16):
                if not inside(x, y):
                    continue
                edge = not all(inside(x + dx, y + dy)
                               for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)))
                if edge and outline:
                    self.put(x, y, outline)
                    continue
                c = fill
                if hi and (x - cx) + (y - cy) < -(rx + ry) * 0.35:
                    c = hi
                if lo and (not inside(x + 1, y) or not inside(x, y + 1)):
                    c = lo
                self.put(x, y, c)

    def slice_(self, x0, y0, w, h, c):
        """Skive flæskesteg: sprød svær øverst, fedtkant, lyst kød."""
        for y in range(h):
            for x in range(w):
                if x in (0, w - 1) and y in (0, h - 1):
                    continue
                if y == 0 or y == h - 1 or x == 0 or x == w - 1:
                    self.put(x0 + x, y0 + y, c["k"])
                elif y <= 2:                       # svær
                    self.put(x0 + x, y0 + y, [c["Y"], c["G"], c["O"], c["G"]][(x + y * 2) % 4])
                elif y == 3:                       # fedt
                    self.put(x0 + x, y0 + y, c["F"])
                else:                              # kød
                    spec = (x * 3 + y * 5) % 7 == 0
                    col = c["Q"] if spec else c["P"]
                    if x == w - 2:
                        col = c["M"]
                    self.put(x0 + x, y0 + y, col)

    def save(self, name):
        img = Image.new("RGBA", (16, 16), (0, 0, 0, 0))
        for y in range(16):
            for x in range(16):
                if self.px[y][x]:
                    img.putpixel((x, y), hexc(self.px[y][x]))
        os.makedirs(OUT, exist_ok=True)
        img.save(os.path.join(OUT, name + ".png"))
        print("skrev", name + ".png")


# ------------------------------------------------------------ fælles skål
BOWL_PAL = {"k": K, "B": "#b88450", "b": "#8a5c32", "v": "#62401f"}

# Kun selve skålens krop (rækker 9-13); indholdet tegnes ovenpå/inden i.
BOWL_BODY = [
    "................",
    "................",
    "................",
    "................",
    "................",
    "................",
    "................",
    "................",
    "................",
    "..kbBBBBBBBBbk..",
    "..kbbbbbbbbbbk..",
    "...kvbbbbbbvk...",
    "....kvvvvvvk....",
    ".....kkkkkk.....",
    "................",
    "................",
]

# Skål set ovenfra med sovs/ris i (rækker 4-9) + krop
BOWL_FULL = [
    "................",
    "................",
    "................",
    "....kkkkkkkk....",
    "..kkBBBBBBBBkk..",
    ".kBBSSSSSSSSBBk.",
    ".kBSSSSSSSSSSBk.",
    ".kBSSSSSSSSSSBk.",
    ".kbBSSSSSSSSBbk.",
    "..kbBBBBBBBBbk..",
    "..kbbbbbbbbbbk..",
    "...kvbbbbbbvk...",
    "....kvvvvvvk....",
    ".....kkkkkk.....",
    "................",
    "................",
]


def sauce_bowl(name, base, light, shade):
    """Skål set ovenfra med sovs i."""
    rows = [r for r in BOWL_FULL]
    rows[6] = ".kBLLSSSSSSSSBk."      # glans øverst til venstre
    rows[7] = ".kBLSSSSSSSsSBk."
    rows[8] = ".kbBSSSSSSsSBbk."
    cv = Canvas()
    cv.ascii(rows, dict(BOWL_PAL, S=base, L=light, s=shade))
    cv.save(name)


# ------------------------------------------------------------------ kulør
def kulor():
    pal = {
        "k": K, "g": "#b9d6e0", "G": "#7ea3b2", "h": "#f1fafc",
        "d": "#4d2812", "D": "#2c1408", "m": "#74401c",
        "c": "#c9a068", "C": "#8f6c3a", "l": "#efe0b8", "L": "#a07a45",
    }
    rows = [
        "................",
        ".....kkkkkk.....",
        ".....kccCck.....",
        ".....kccCck.....",
        "......khGk......",
        "......khGk......",
        ".....kghddGk....",
        "....kghmdddGk...",
        "...kghmddddDGk..",
        "...kgdllllldGk..",
        "...kgdlLLLldGk..",
        "...kgdllllldGk..",
        "...kgmddddddGk..",
        "...kgmdddddDGk..",
        "....kGdddDDGk...",
        ".....kkkkkkk....",
    ]
    cv = Canvas()
    cv.ascii(rows, pal)
    cv.save("kulor")


# ------------------------------------------------------------ flæskesteg
SVAER = {
    "k": "#3b2210", "Y": "#f6d97a", "G": "#dca845", "O": "#a96a22",
    "F": "#f7e8c6", "P": "#ecc9a6", "Q": "#caa07c", "M": "#b9763d",
    "N": "#85502a",
}


def flaeskesteg():
    """Steg i 3/4-visning: ternet, sprød svær øverst, skåret forside, brun skorpe i siden."""
    cv = Canvas()
    kind = {}
    for y in range(8, 14):                       # forside (skåret flade)
        for x in range(1, 10):
            kind[(x, y)] = "front"
    for y in range(3, 8):                        # overside (svær)
        for x in range(1 + (8 - y), 10 + (8 - y)):
            kind[(x, y)] = "top"
    for x, (y0, y1) in {10: (8, 12), 11: (7, 11), 12: (6, 10), 13: (5, 9), 14: (4, 8)}.items():
        for y in range(y0, y1 + 1):              # højre side (skorpe)
            kind[(x, y)] = "side"
    for (x, y), k in kind.items():
        if k == "top":
            lattice = (x + y) % 3 == 0 or (x - y) % 3 == 0
            if lattice:
                col = SVAER["O"]
            elif (x * 5 + y * 3) % 6 == 0:
                col = SVAER["Y"]
            else:
                col = SVAER["G"]
        elif k == "front":
            if y == 8:
                col = SVAER["F"]                     # fedtkant under sværen
            elif y == 13:
                col = SVAER["M"]
            else:
                col = SVAER["Q"] if (y % 2 == 0 and (x + y) % 3 == 0) else SVAER["P"]
        else:
            col = SVAER["N"] if (x + y) % 3 == 0 else SVAER["M"]
        cv.put(x, y, col)
    pts = set(kind)
    for (x, y) in pts:                           # sort outline rundt om figuren
        if any((x + dx, y + dy) not in pts for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))):
            cv.put(x, y, SVAER["k"])
    # kant mellem forside og side så de adskilles
    for y in range(9, 13):
        cv.put(9, y, SVAER["M"])
    # laurbærblad og nellike oven på sværen
    for (x, y) in [(7, 5), (8, 5), (9, 4)]:
        cv.put(x, y, "#5e8c3a")
    cv.put(8, 4, "#3f6428"); cv.put(6, 5, "#3f6428"); cv.put(10, 4, "#3f6428")
    cv.save("flaeskesteg")


# --------------------------------------------------------- flæskefråder
def slice2(cv, x0, y0, w, h):
    """Skive set oppefra: sprød svær i kanten, lyst kød, skygge forneden."""
    for y in range(h):
        for x in range(w):
            if x in (0, w - 1) and y in (0, h - 1):
                continue
            if y == 0:
                col = [SVAER["Y"], SVAER["G"], SVAER["O"], SVAER["G"]][x % 4]
            elif y == h - 1:
                col = SVAER["M"]
            else:
                col = SVAER["Q"] if (x * 2 + y * 3) % 7 == 0 else SVAER["P"]
            cv.put(x0 + x, y0 + y, col)


def flaeskefrader():
    """Tallerken oppefra: flæskesteg, brunede kartofler, kål og brun sovs."""
    cv = Canvas()
    cv.ellipse(7.5, 7.5, 7.1, 7.1, "#eef2f4", outline=K, hi="#ffffff", lo="#c3ced6")
    cv.ellipse(7.5, 7.5, 5.2, 5.2, "#dfe7ec", lo="#c3ced6")
    # kål (nederst til venstre)
    cv.ellipse(5.0, 11.0, 2.8, 1.8, "#7cb342", hi="#b2de78", lo="#4a7d2b")
    # kartofler (til højre)
    cv.ellipse(11.6, 5.6, 2.2, 2.2, "#d79a42", hi="#f6cf7a", lo="#a86d28")
    cv.ellipse(11.2, 9.4, 2.2, 2.2, "#d79a42", hi="#f6cf7a", lo="#a86d28")
    # to skiver flæskesteg
    slice2(cv, 3, 3, 7, 4)
    slice2(cv, 4, 6, 7, 4)
    # brun sovs hældt over
    for (x, y) in [(4, 9), (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9),
                   (5, 10), (6, 10), (7, 10), (8, 10), (9, 10),
                   (6, 11), (7, 11), (8, 8), (9, 8), (5, 8)]:
        cv.put(x, y, "#5a2f14")
    for (x, y) in [(5, 9), (8, 10), (7, 11), (9, 8)]:
        cv.put(x, y, "#86502a")
    for (x, y) in [(6, 10), (9, 10)]:
        cv.put(x, y, "#3a1c0a")
    cv.save("flaeskefrader")


# ---------------------------------------------------- kylling bernaise
def kylling_bernaise():
    cv = Canvas()
    pal = dict(BOWL_PAL, S="#f7f4e8", L="#ffffff", s="#d3cdb2")
    rows = [r for r in BOWL_FULL]
    rows[6] = ".kBLSSSSSSSsSBk."
    rows[7] = ".kBSSSsSSSSSSBk."
    rows[8] = ".kbBSSSSSsSSBbk."
    cv.ascii(rows, pal)
    # ris-bunke der stikker op over skålen
    cv.ellipse(8, 5.6, 5.8, 3.0, "#f7f4e8", hi="#ffffff", lo="#d3cdb2")
    for (x, y) in [(4, 5), (6, 7), (10, 7), (11, 5), (8, 7)]:
        cv.put(x, y, "#d3cdb2")
    # kyllingefilet
    cv.ellipse(8, 4.2, 4.8, 2.4, "#d9923a", hi="#f2bd62", lo="#a2601f")
    for (x, y) in [(5, 4), (6, 5), (8, 3), (9, 4), (10, 5)]:
        cv.put(x, y, "#9a5c1e")
    # bernaise-sauce hældt ovenpå
    for (x, y) in [(6, 2), (7, 2), (8, 2), (7, 3), (8, 3), (9, 3), (8, 4), (9, 4), (10, 4), (9, 5), (8, 6),
                   (7, 4), (11, 4), (10, 5), (7, 5)]:
        cv.put(x, y, "#f2cf3d")
    for (x, y) in [(7, 2), (8, 3), (9, 4), (7, 4)]:
        cv.put(x, y, "#fff08a")
    for (x, y) in [(9, 5), (8, 6), (10, 5)]:
        cv.put(x, y, "#d4a91c")
    cv.save("kylling_bernaise")


def main():
    kulor()
    sauce_bowl("brun_sovs", "#5a2f14", "#8a5530", "#43200c")
    sauce_bowl("bernaise", "#f0d56a", "#fff2a8", "#d9b94a")
    flaeskesteg()
    flaeskefrader()
    kylling_bernaise()


if __name__ == "__main__":
    main()
