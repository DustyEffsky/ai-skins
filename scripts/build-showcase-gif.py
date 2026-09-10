from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "screenshots" / "all-skins.gif"
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

def frame(skin, position):
    collection, name, bg, panel, panel2, text, muted, accent, line = skin
    im = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(im)
    # Soft signature light without changing the actual palette.
    if collection.startswith("SIGNATURE"):
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse((620, -180, 1100, 300), fill=accent + "38")
        im = Image.alpha_composite(im.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(70))).convert("RGB")
        d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 42), fill=panel)
    d.text((20, 13), "CHATGPT + CODEX SKINS", font=font(13, True), fill=accent)
    counter = f"{position:02d}/20  {collection}"
    d.text((W - 205, 14), counter, font=font(10, True), fill=muted)
    # Sidebar.
    d.rectangle((0, 42, 188, H), fill=panel)
    d.line((188, 42, 188, H), fill=line)
    d.text((20, 67), "◇  CODEX", font=font(15, True), fill=accent)
    rr(d, (16, 103, 172, 139), 7, panel2, line)
    d.text((29, 115), "+  New task", font=font(10), fill=text)
    d.text((20, 174), "WORKSPACE", font=font(9, True), fill=muted)
    rr(d, (15, 190, 173, 224), 6, panel2)
    d.rectangle((15, 190, 18, 224), fill=accent)
    d.text((29, 201), "ChatGPT Skins", font=font(10), fill=text)
    for i, label in enumerate(("Leafstream", "AUNOZ", "Controller support")):
        d.text((29, 247 + i * 31), label, font=font(10), fill=muted)
    d.text((20, 506), "●  Extension connected", font=font(9), fill=accent)
    # Header and conversation.
    d.line((188, 86, W, 86), fill=line)
    d.text((216, 59), "codex-skins / main", font=font(10), fill=text)
    d.ellipse((W - 32, 62, W - 24, 70), fill=accent)
    rr(d, (448, 121, 906, 174), 11, panel2, line)
    d.text((471, 140), "Make this interface feel genuinely designed.", font=font(12), fill=text)
    d.text((226, 215), "Implemented.", font=font(13, True), fill=accent)
    d.text((226, 243), "The palette, surfaces, typography and atmosphere now", font=font(11), fill=text)
    d.text((226, 263), "change together while the workspace remains familiar.", font=font(11), fill=text)
    rr(d, (226, 298, 904, 415), 10, panel, line)
    d.rectangle((227, 299, 903, 328), fill=panel2)
    d.text((244, 308), "content.css", font=font(9), fill=muted)
    d.text((246, 348), ':root[data-codex-skins="on"] {', font=font(10), fill=accent)
    d.text((265, 370), "--main-surface-primary: var(--cs-bg);", font=font(10), fill=text)
    d.text((265, 392), "--text-primary: var(--cs-text);", font=font(10), fill=text)
    rr(d, (220, 458, 913, 511), 13, panel, line)
    d.text((242, 478), "Ask Codex to refine this skin...", font=font(10), fill=muted)
    rr(d, (864, 469, 900, 501), 9, accent)
    d.text((877, 475), "↑", font=font(15, True), fill=bg)
    # Large skin identity.
    d.text((211, 102), name, font=font(17, True), fill=accent)
    return im.quantize(colors=96, method=Image.Quantize.MEDIANCUT)

by_name = {skin[1]: skin for skin in SKINS}
keyframes = [
    frame(by_name[name], index + 1).convert("RGB").resize(OUTPUT_SIZE, Image.Resampling.LANCZOS)
    for index, name in enumerate(SEQUENCE)
]
palette_strip = Image.new("RGB", (240, 135 * len(keyframes)))
for index, image in enumerate(keyframes):
    palette_strip.paste(image.resize((240, 135), Image.Resampling.BILINEAR), (0, index * 135))
shared_palette = palette_strip.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
frames = []
durations = []

for index, current in enumerate(keyframes):
    following = keyframes[(index + 1) % len(keyframes)]
    frames.append(current.quantize(palette=shared_palette, dither=Image.Dither.NONE))
    durations.append(900)
    for step in range(1, 9):
        amount = step / 9
        eased = amount * amount * (3 - 2 * amount)
        blend = Image.blend(current, following, eased)
        frames.append(blend.quantize(palette=shared_palette, dither=Image.Dither.NONE))
        durations.append(80)

frames[0].save(OUTPUT, save_all=True, append_images=frames[1:], duration=durations, loop=0, optimize=True, disposal=1)
print(OUTPUT)
