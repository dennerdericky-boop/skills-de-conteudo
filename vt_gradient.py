#!/usr/bin/env python3
"""VANTAGE TIMES - degrade editorial + carimbo VT na cor certa (1080x1350)."""
import argparse, base64, io
from PIL import Image, ImageEnhance, ImageOps, ImageStat

PRESETS = {
    "petrol":   {"color": (9, 47, 53),    "sat": 0.35, "contrast": 1.15, "bright": 0.92, "tint": 0.18, "max": 0.97, "fundo": "escuro"},
    "ink":      {"color": (17, 17, 17),   "sat": 0.0,  "contrast": 1.25, "bright": 0.90, "tint": 0.00, "max": 0.97, "fundo": "escuro"},
    "lavender": {"color": (216, 210, 232), "sat": 0.0, "contrast": 1.05, "bright": 1.05, "tint": 0.30, "max": 1.00, "fundo": "claro"},
    "paper":    {"color": (242, 240, 233), "sat": 0.0, "contrast": 1.00, "bright": 1.05, "tint": 0.20, "max": 1.00, "fundo": "claro"},
}
CATEGORIA = {
    "mercados": "petrol", "mercado": "petrol", "acoes": "petrol", "economia": "petrol", "analise": "petrol",
    "comercio": "petrol", "institucional": "petrol", "negocios": "petrol", "breaking": "petrol",
    "politica": "ink", "crise": "ink", "investigacao": "ink",
    "geopolitica": "lavender", "citacao": "paper",
}

# Carimbo VT oficial: canal R = forma do V, canal G = forma do T
VT_MASK = """
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
"""
V_CLARO = (255, 255, 255)   # V branco  -> VT_stamp_dark-background (fundo escuro)
V_ESCURO = (7, 17, 26)      # V escuro  -> VT_stamp_cream-background (fundo claro)
T_LIME = (178, 235, 8)      # T sempre em Signal Lime

def carimbo(versao, largura):
    m = Image.open(io.BytesIO(base64.b64decode("".join(VT_MASK.split())))).convert("RGB")
    r, g, _ = m.split()
    vcor = V_CLARO if versao == "dark-background" else V_ESCURO
    out = Image.new("RGBA", m.size, (0, 0, 0, 0))
    v = Image.new("RGBA", m.size, vcor + (255,)); v.putalpha(r)
    t = Image.new("RGBA", m.size, T_LIME + (255,)); t.putalpha(g)
    out = Image.alpha_composite(Image.alpha_composite(out, v), t)
    h = round(m.height * largura / m.width)
    return out.resize((largura, h), Image.LANCZOS)

def escolher_versao(img, caixa):
    """Regra: fundo escuro -> V branco; fundo claro -> V escuro. Mede o fundo real sob o carimbo."""
    lum = ImageStat.Stat(img.crop(caixa).convert("L")).mean[0] / 255
    return ("cream-background" if lum > 0.55 else "dark-background"), lum

def ramp(n, start, end, max_alpha):
    out = []
    for i in range(n):
        t = i / (n - 1)
        if t <= start:
            a = 0.0
        elif t >= end:
            a = max_alpha
        else:
            x = (t - start) / (end - start)
            a = max_alpha * x * x * (3 - 2 * x)
        out.append(int(a * 255))
    return out

def mask(w, h, direction, start, end, max_alpha):
    if direction in ("bottom", "top"):
        vals = ramp(h, start, end, max_alpha)
        if direction == "top":
            vals = vals[::-1]
        m = Image.new("L", (1, h)); m.putdata(vals)
    else:
        vals = ramp(w, start, end, max_alpha)
        if direction == "left":
            vals = vals[::-1]
        m = Image.new("L", (w, 1)); m.putdata(vals)
    return m.resize((w, h))

def render(src, dst, preset, direction="bottom", start=0.35, end=0.82, focus_y=0.4,
           stamp="auto", stamp_w=110, margem=64, w=1080, h=1350, lado="esquerda"):
    p = PRESETS[preset]
    if src:
        img = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        img = ImageOps.fit(img, (w, h), Image.LANCZOS, centering=(0.5, focus_y))
        img = ImageEnhance.Color(img).enhance(p["sat"])
        img = ImageEnhance.Contrast(img).enhance(p["contrast"])
        img = ImageEnhance.Brightness(img).enhance(p["bright"])
        color = Image.new("RGB", (w, h), p["color"])
        if p["tint"]:
            img = Image.blend(img, color, p["tint"])
        img = Image.composite(color, img, mask(w, h, direction, start, end, p["max"]))
        img = Image.composite(color, img, mask(w, h, "top", 0.80, 1.0, 0.45))
    else:  # slide sem foto: fundo chapado da categoria
        img = Image.new("RGB", (w, h), p["color"])
    versao = None
    if stamp != "off":
        s = carimbo("dark-background", stamp_w)
        x = margem if lado == "esquerda" else w - margem - s.width
        y = margem
        caixa = (x - 10, y - 10, x + s.width + 10, y + s.height + 10)
        if stamp == "auto":
            versao, lum = escolher_versao(img, caixa)
        else:
            versao = stamp
        s = carimbo(versao, stamp_w)
        base = img.convert("RGBA"); base.alpha_composite(s, (x, y)); img = base.convert("RGB")
    img.save(dst, quality=92)
    return dst, versao

if __name__ == "__main__":
    a = argparse.ArgumentParser()
    a.add_argument("src", help="foto, ou - para slide sem foto"); a.add_argument("dst")
    a.add_argument("--categoria", default="economia")
    a.add_argument("--preset", choices=PRESETS)
    a.add_argument("--direcao", default="bottom", choices=["bottom", "top", "left", "right"])
    a.add_argument("--inicio", type=float, default=0.35)
    a.add_argument("--fim", type=float, default=0.82)
    a.add_argument("--foco", type=float, default=0.4)
    a.add_argument("--carimbo", default="auto", choices=["auto", "dark-background", "cream-background", "off"])
    a.add_argument("--carimbo-largura", type=int, default=110)
    a.add_argument("--carimbo-lado", default="esquerda", choices=["esquerda", "direita"],
                   help="canto superior do carimbo VT (regra da marca: esquerda)")
    x = a.parse_args()
    preset = x.preset or CATEGORIA.get(x.categoria.lower(), "petrol")
    dst, versao = render(None if x.src == "-" else x.src, x.dst, preset, x.direcao, x.inicio, x.fim,
                         x.foco, x.carimbo, x.carimbo_largura, lado=x.carimbo_lado)
    print(dst, "| carimbo:", versao and "VT_stamp_" + versao)
