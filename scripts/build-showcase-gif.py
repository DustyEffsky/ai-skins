from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "screenshots" / "all-20-skins-slow.gif"
W, H = 960, 540
OUTPUT_SIZE = (1440, 810)

SKINS = [
    ("STANDARD 01", "CHATGPT CLASSIC", "#0d0d0d", "#171717", "#212121", "#f4f4f4", "#a9a9a9", "#ffffff", "#343434"),
    ("STANDARD 02", "WINAMP INDUSTRIAL", "#0b0d0e", "#1b1f22", "#2a3034", "#d9e0d1", "#8c9789", "#92ff36", "#596068"),
    ("STANDARD 03", "AMBER TERMINAL", "#090603", "#100b05", "#191006", "#ffd27a", "#aa7732", "#ffb000", "#5c3c00"),
    ("STANDARD 04", "NEON GRID", "#09051a", "#130b2b", "#201044", "#f8edff", "#a99bbd", "#42e8ff", "#62378b"),
    ("STANDARD 05", "PAPER & INK", "#f2eadc", "#fbf6ec", "#e8decc", "#29241e", "#74695c", "#b54a32", "#cbbda7"),
    ("STANDARD 06", "BLUEPRINT", "#061d36", "#08284a", "#0c355e", "#e8f7ff", "#9bc2dc", "#ffffff", "#3e88b8"),
    ("STANDARD 07", "STUDIO LIGHT", "#f6f7f8", "#ffffff", "#eceef2", "#202124", "#6d7178", "#635bff", "#d8dbe2"),
    ("STANDARD 08", "GAME DEV DESK", "#0c1218", "#111c25", "#1d2b38", "#e8f0f5", "#8ea2af", "#ffca3a", "#314454"),
    ("STANDARD 09", "MIDNIGHT OLED", "#000000", "#050505", "#0a0a0a", "#eeeeee", "#777777", "#7dd3fc", "#232323"),
    ("STANDARD 10", "BAVARIAN WORKSHOP", "#17110d", "#241a13", "#38271a", "#f0e2c4", "#b6a280", "#d79b25", "#65472e"),
    ("SIGNATURE 01", "OBSIDIAN GLASS", "#050608", "#0d1117", "#181e27", "#f4f5f7", "#858b96", "#d8ff45", "#303540"),
    ("SIGNATURE 02", "LIQUID CHROME", "#090b10", "#171b24", "#252b38", "#f4f7ff", "#9ca7bb", "#dce8ff", "#515b70"),
    ("SIGNATURE 03", "SAKURA AFTER DARK", "#110912", "#1c1020", "#2b1730", "#ffeef8", "#b997ad", "#ff8fcf", "#633557"),
    ("SIGNATURE 04", "MONOLITH", "#050505", "#0b0b0b", "#151515", "#eeeeee", "#858585", "#ff3b30", "#323232"),
    ("SIGNATURE 05", "IVORY ATELIER", "#f5f0e6", "#fffaf1", "#ebe2d2", "#211e1a", "#776e63", "#9a6d23", "#c9bda9"),
    ("SIGNATURE 06", "ABYSSAL", "#02080d", "#06131a", "#0a2029", "#e1fbff", "#76a7ae", "#00e5ff", "#174653"),
    ("SIGNATURE 07", "EMBER FORGE", "#0e0907", "#1c100b", "#2b1710", "#fff0e5", "#b98d78", "#ff6b1a", "#66301c"),
    ("SIGNATURE 08", "HOLOGRAPHIC", "#f3f6fb", "#ffffff", "#e9eef7", "#1d2330", "#6e7688", "#6f4cff", "#c9d2e2"),
    ("SIGNATURE 09", "TOXIC EXECUTIVE", "#070907", "#10150d", "#1b2415", "#f2f8e9", "#8d9a81", "#c8ff00", "#34432c"),
    ("SIGNATURE 10", "CELESTIAL", "#070713", "#101024", "#1a1936", "#f2f2ff", "#9b9ab8", "#7c9dff", "#3f3d68"),
]

SEQUENCE = [
    "MIDNIGHT OLED", "CHATGPT CLASSIC", "MONOLITH", "OBSIDIAN GLASS",
    "WINAMP INDUSTRIAL", "TOXIC EXECUTIVE", "GAME DEV DESK", "BLUEPRINT",
    "ABYSSAL", "CELESTIAL", "NEON GRID", "SAKURA AFTER DARK",
    "EMBER FORGE", "BAVARIAN WORKSHOP", "AMBER TERMINAL", "PAPER & INK",
    "IVORY ATELIER", "STUDIO LIGHT", "HOLOGRAPHIC", "LIQUID CHROME",
]

def font(size, bold=False):
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)

def rr(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)

def app_panel(d, x, label, skin, claude=False):
    _, name, bg, panel, panel2, text, muted, accent, line = skin
    pw = 456
    d.rectangle((x, 72, x + pw, H), fill=bg)
    d.rectangle((x, 72, x + 116, H), fill=panel)
    d.line((x + 116, 72, x + 116, H), fill=line)
    brand = "C  CLAUDE" if claude else "◇  CHATGPT"
    d.text((x + 14, 92), brand, font=font(11, True), fill=accent)
    rr(d, (x + 12, 126, x + 104, 156), 6, panel2, line)
    d.text((x + 24, 136), "+  New chat", font=font(8), fill=text)
    d.text((x + 14, 184), "RECENTS", font=font(7, True), fill=muted)
    for i, item in enumerate(("AI Skins", "Project notes", "Interface ideas")):
        if i == 0:
            rr(d, (x + 10, 199, x + 107, 224), 5, panel2)
            d.rectangle((x + 10, 199, x + 13, 224), fill=accent)
        d.text((x + 20, 207 + i * 28), item, font=font(7), fill=text if i == 0 else muted)
    d.text((x + 14, 508), "●  Skin active", font=font(7), fill=accent)
    d.text((x + 136, 94), label, font=font(10, True), fill=text)
    d.text((x + 136, 116), name, font=font(13, True), fill=accent)
    rr(d, (x + 210, 155, x + 433, 198), 9, panel2, line)
    d.text((x + 225, 171), "Give this workspace a new identity.", font=font(8), fill=text)
    d.text((x + 138, 234), "Done.", font=font(10, True), fill=accent)
    d.text((x + 138, 256), "The interface now uses the same skin tokens", font=font(8), fill=text)
    d.text((x + 138, 273), "while preserving the app's familiar structure.", font=font(8), fill=text)
    rr(d, (x + 138, 306, x + 432, 393), 8, panel, line)
    d.rectangle((x + 139, 307, x + 431, 331), fill=panel2)
    d.text((x + 151, 315), "theme adapter", font=font(7), fill=muted)
    d.text((x + 151, 348), "--surface: var(--skin-panel);", font=font(7), fill=text)
    d.text((x + 151, 369), f"--accent: {accent};", font=font(7), fill=accent)
    rr(d, (x + 132, 441, x + 438, 493), 12, panel, line)
    d.text((x + 150, 461), "Reply to Claude..." if claude else "Message ChatGPT...", font=font(8), fill=muted)
    rr(d, (x + 402, 451, x + 428, 483), 8, accent)
    d.text((x + 411, 458), "↑", font=font(12, True), fill=bg)

def frame(skin, position):
    collection, name, bg, panel, panel2, text, muted, accent, line = skin
    im = Image.new("RGB", (W, H), bg)
    if collection.startswith("SIGNATURE"):
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(glow).ellipse((570, -220, 1080, 270), fill=accent + "32")
        im = Image.alpha_composite(im.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(75))).convert("RGB")
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 72), fill=panel)
    d.text((20, 14), "AI SKINS", font=font(16, True), fill=accent)
    d.text((20, 40), "CHATGPT + CODEX + CLAUDE", font=font(8, True), fill=muted)
    d.text((315, 22), name, font=font(18, True), fill=text)
    d.text((815, 25), f"{position:02d}/20", font=font(10, True), fill=accent)
    app_panel(d, 12, "CHATGPT / CODEX", skin)
    app_panel(d, 492, "CLAUDE", skin, claude=True)
    d.rectangle((478, 72, 482, H), fill=accent)
    return im

by_name = {skin[1]: skin for skin in SKINS}
keyframes = [frame(by_name[name], index + 1).resize(OUTPUT_SIZE, Image.Resampling.LANCZOS) for index, name in enumerate(SEQUENCE)]
palette_strip = Image.new("RGB", (240, 135 * len(keyframes)))
for index, image in enumerate(keyframes):
    palette_strip.paste(image.resize((240, 135), Image.Resampling.BILINEAR), (0, index * 135))
shared_palette = palette_strip.quantize(colors=160, method=Image.Quantize.MEDIANCUT)
frames, durations = [], []
for index, current in enumerate(keyframes):
    following = keyframes[(index + 1) % len(keyframes)]
    frames.append(current.quantize(palette=shared_palette, dither=Image.Dither.NONE))
    durations.append(1800)
    for step in range(1, 9):
        amount = step / 9
        eased = amount * amount * (3 - 2 * amount)
        frames.append(Image.blend(current, following, eased).quantize(palette=shared_palette, dither=Image.Dither.NONE))
        durations.append(90)

frames[0].save(OUTPUT, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True, disposal=1)
print(OUTPUT)
