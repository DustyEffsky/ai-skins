from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "screenshots"
W, H = 1400, 1800

STANDARD = [
    ("CHATGPT CLASSIC", "#0d0d0d", "#171717", "#212121", "#f4f4f4", "#a9a9a9", "#ffffff", "#343434"),
    ("WINAMP INDUSTRIAL", "#0b0d0e", "#1b1f22", "#2a3034", "#d9e0d1", "#8c9789", "#92ff36", "#596068"),
    ("AMBER TERMINAL", "#090603", "#100b05", "#191006", "#ffd27a", "#aa7732", "#ffb000", "#5c3c00"),
    ("NEON GRID", "#09051a", "#130b2b", "#201044", "#f8edff", "#a99bbd", "#42e8ff", "#62378b"),
    ("PAPER & INK", "#f2eadc", "#fbf6ec", "#e8decc", "#29241e", "#74695c", "#b54a32", "#cbbda7"),
    ("BLUEPRINT", "#061d36", "#08284a", "#0c355e", "#e8f7ff", "#9bc2dc", "#ffffff", "#3e88b8"),
    ("STUDIO LIGHT", "#f6f7f8", "#ffffff", "#eceef2", "#202124", "#6d7178", "#635bff", "#d8dbe2"),
    ("GAME DEV DESK", "#0c1218", "#111c25", "#1d2b38", "#e8f0f5", "#8ea2af", "#ffca3a", "#314454"),
    ("MIDNIGHT OLED", "#000000", "#050505", "#0a0a0a", "#eeeeee", "#777777", "#7dd3fc", "#232323"),
    ("BAVARIAN WORKSHOP", "#17110d", "#241a13", "#38271a", "#f0e2c4", "#b6a280", "#d79b25", "#65472e"),
]

SIGNATURE = [
    ("OBSIDIAN GLASS", "#050608", "#0d1117", "#181e27", "#f4f5f7", "#858b96", "#d8ff45", "#303540"),
    ("LIQUID CHROME", "#090b10", "#171b24", "#252b38", "#f4f7ff", "#9ca7bb", "#dce8ff", "#515b70"),
    ("SAKURA AFTER DARK", "#110912", "#1c1020", "#2b1730", "#ffeef8", "#b997ad", "#ff8fcf", "#633557"),
    ("MONOLITH", "#050505", "#0b0b0b", "#151515", "#eeeeee", "#858585", "#ff3b30", "#323232"),
    ("IVORY ATELIER", "#f5f0e6", "#fffaf1", "#ebe2d2", "#211e1a", "#776e63", "#9a6d23", "#c9bda9"),
    ("ABYSSAL", "#02080d", "#06131a", "#0a2029", "#e1fbff", "#76a7ae", "#00e5ff", "#174653"),
    ("EMBER FORGE", "#0e0907", "#1c100b", "#2b1710", "#fff0e5", "#b98d78", "#ff6b1a", "#66301c"),
    ("HOLOGRAPHIC", "#f3f6fb", "#ffffff", "#e9eef7", "#1d2330", "#6e7688", "#6f4cff", "#c9d2e2"),
    ("TOXIC EXECUTIVE", "#070907", "#10150d", "#1b2415", "#f2f8e9", "#8d9a81", "#c8ff00", "#34432c"),
    ("CELESTIAL", "#070713", "#101024", "#1a1936", "#f2f2ff", "#9b9ab8", "#7c9dff", "#3f3d68"),
]

def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

def tile(skin, signature=False, platform="chatgpt"):
    name, bg, panel, panel2, text, muted, accent, line = skin
    im = Image.new("RGB", (620, 286), bg)
    if signature:
        glow = Image.new("RGBA", im.size, (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse((370, -150, 730, 210), fill=accent + "35")
        im = Image.alpha_composite(im.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(55))).convert("RGB")
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, 145, 286), fill=panel)
    d.line((145, 0, 145, 286), fill=line, width=2)
    brand = "C  CLAUDE" if platform == "claude" else "◇  CHATGPT"
    d.text((18, 18), brand, font=font(15, True), fill=accent)
    d.rounded_rectangle((14, 55, 130, 88), radius=7, fill=panel2, outline=line)
    d.text((27, 66), "+ New task", font=font(9), fill=text)
    d.text((18, 119), "WORKSPACE", font=font(8, True), fill=muted)
    d.rounded_rectangle((13, 134, 132, 166), radius=6, fill=panel2)
    d.rectangle((13, 134, 16, 166), fill=accent)
    d.text((25, 145), "Skins", font=font(9), fill=text)
    d.text((170, 20), name, font=font(16, True), fill=accent)
    context = "claude.ai / conversation" if platform == "claude" else "ai-skins / main"
    d.text((170, 50), context, font=font(8), fill=muted)
    d.rounded_rectangle((258, 78, 586, 116), radius=9, fill=panel2, outline=line)
    d.text((276, 91), "Make the workspace feel designed.", font=font(9), fill=text)
    d.text((170, 146), "Done." if platform == "claude" else "Implemented.", font=font(11, True), fill=accent)
    d.text((170, 168), "Theme tokens applied safely.", font=font(9), fill=text)
    d.rounded_rectangle((170, 195, 585, 258), radius=8, fill=panel, outline=line)
    d.text((186, 211), "--surface: var(--skin-panel);", font=font(8), fill=text)
    d.text((186, 233), f"--accent: {accent};", font=font(8), fill=accent)
    return im

def sheet(title, skins, filename, signature=False, platform="chatgpt"):
    canvas = Image.new("RGB", (W, H), "#0b0c0e")
    d = ImageDraw.Draw(canvas)
    d.text((70, 56), title, font=font(34, True), fill="#f4f5f7")
    for index, skin in enumerate(skins):
        x = 70 + (index % 2) * 660
        y = 160 + (index // 2) * 318
        canvas.paste(tile(skin, signature, platform), (x, y))
    canvas.save(OUT / filename, optimize=True)

sheet("STANDARD COLLECTION", STANDARD, "standard-collection.png")
sheet("SIGNATURE COLLECTION", SIGNATURE, "signature-collection.png", signature=True)
sheet("CLAUDE / STANDARD COLLECTION", STANDARD, "claude-standard-collection.png", platform="claude")
sheet("CLAUDE / SIGNATURE COLLECTION", SIGNATURE, "claude-signature-collection.png", signature=True, platform="claude")
print("collection sheets built")
