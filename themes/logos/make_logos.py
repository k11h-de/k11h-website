"""Generate k11h logo proposals as hand-sized SVGs (geometry, not traced).
usage: python3 themes/logos/make_logos.py   -> writes logo-*.svg next to this file"""
from math import sin, cos, asin, radians
from pathlib import Path

C = 256                      # centre of a 512 viewBox
TEAL, RED, ORANGE, GREY = "#72aec0", "#cd5252", "#eaa258", "#706c7a"
OUT = Path(__file__).parent


def pt(r, deg):
    """polar -> svg coords; 0deg = top, clockwise"""
    a = radians(deg)
    return f"{C + r * sin(a):.1f} {C - r * cos(a):.1f}"


def svg(body, style=""):
    st = f"<style>{style}</style>" if style else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" '
            f'role="img" aria-label="k11h">{st}{body}</svg>\n')


# ---------------------------------------------------------------- A: rebuild
def logo_a():
    """Faithful rebuild: scalloped gear, four puzzle quadrants, centre hole."""
    R, hole, notch, n = 236, 84, 21, 16
    mask = (f'<mask id="g"><circle cx="{C}" cy="{C}" r="{R}" fill="#fff"/>'
            + "".join(f'<circle cx="{pt(R, i * 360 / n + 360 / n / 2).split()[0]}" '
                      f'cy="{pt(R, i * 360 / n + 360 / n / 2).split()[1]}" r="{notch}"/>' for i in range(n))
            + f'<circle cx="{C}" cy="{C}" r="{hole}"/></mask>')
    quads = [(GREY, 270), (RED, 0), (ORANGE, 90), (TEAL, 180)]  # colour, start angle
    wedges = "".join(
        f'<path fill="{col}" d="M{C} {C}L{pt(300, a)}A300 300 0 0 1 {pt(300, a + 90)}Z"/>' for col, a in quads)
    # each piece pushes one knob clockwise into its neighbour, across the shared edge
    knobs, rk, mid = "", 23, 158
    for col, a in quads:
        b = a + 90                                   # shared edge with the next piece
        x0, y0 = map(float, pt(mid, b).split())
        dx, dy = cos(radians(b)), sin(radians(b))    # unit vector perpendicular to the edge (clockwise)
        cx, cy = x0 + dx * 30, y0 + dy * 30
        neck = 11
        # neck: quad from the edge to the knob centre
        ex, ey = sin(radians(b)), -cos(radians(b))   # along the edge
        p = [(x0 - ex * neck - dx * 2, y0 - ey * neck - dy * 2), (x0 + ex * neck - dx * 2, y0 + ey * neck - dy * 2),
             (cx + ex * neck, cy + ey * neck), (cx - ex * neck, cy - ey * neck)]
        knobs += (f'<path fill="{col}" d="M' + "L".join(f"{x:.1f} {y:.1f}" for x, y in p) + 'Z"/>'
                  f'<circle fill="{col}" cx="{cx:.1f}" cy="{cy:.1f}" r="{rk}"/>')
    return svg(f'{mask}<g mask="url(#g)">{wedges}{knobs}</g>')


# ---------------------------------------------------------------- gear profile
def gear_segment(a, b, r_tip, r_root, r_in, teeth_per_seg, gap, tip_half, root_half):
    """One coloured segment of a toothed ring between angles a..b with a constant-width gap."""
    d = lambda r: asin(gap / 2 / r) * 180 / 3.141592653589793      # gap -> angle at radius r
    step = (b - a) / teeth_per_seg
    s = f"M{pt(r_root, a + d(r_root))}"
    for i in range(teeth_per_seg):
        t = a + step * (i + .5)                                          # tooth centre
        s += f"A{r_root} {r_root} 0 0 1 {pt(r_root, t - root_half)}"
        s += f"L{pt(r_tip, t - tip_half)}"
        s += f"A{r_tip} {r_tip} 0 0 1 {pt(r_tip, t + tip_half)}"
        s += f"L{pt(r_root, t + root_half)}"
    s += f"A{r_root} {r_root} 0 0 1 {pt(r_root, b - d(r_root))}"
    s += f"L{pt(r_in, b - d(r_in))}"
    s += f"A{r_in} {r_in} 0 0 0 {pt(r_in, a + d(r_in))}Z"
    return s


QUADS = [(GREY, 270), (RED, 0), (ORANGE, 90), (TEAL, 180)]


# ---------------------------------------------------------------- B: flat
def logo_b():
    """Reduced: no puzzle knobs, real trapezoid teeth, four segments split by clean gaps."""
    body = "".join(
        f'<path fill="{col}" d="{gear_segment(a, a + 90, 244, 204, 104, 3, 22, 6.5, 10)}"/>' for col, a in QUADS)
    return svg(body)


# ---------------------------------------------------------------- C: prompt
def logo_c():
    """Signet: slimmer gear ring, a terminal prompt >_ in the middle (adapts to dark mode)."""
    ring = "".join(
        f'<path fill="{col}" d="{gear_segment(a, a + 90, 248, 214, 150, 3, 20, 6.5, 10)}"/>' for col, a in QUADS)
    prompt = ('<path class="ink" fill="none" stroke-width="30" stroke-linecap="round" stroke-linejoin="round" '
              'd="M188 206L240 256L188 306M262 312H330"/>')
    style = ".ink{stroke:#2b2f36}@media (prefers-color-scheme:dark){.ink{stroke:#e8ebef}}"
    return svg(ring + prompt, style)


for name, fn in {"a-rebuild": logo_a, "b-flat": logo_b, "c-prompt": logo_c}.items():
    p = OUT / f"logo-{name}.svg"
    p.write_text(fn())
    print(f"{p.name}: {p.stat().st_size} bytes")
