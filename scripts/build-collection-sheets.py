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

MODERN = [
    ("JAPANESE HI-FI", "hifi", "#171d1c", "#d7cfbf", "#222824", "#f2ecdc", "#72e2cb", "#ffb65c"),
    ("CONTROL ROOM", "control", "#071012", "#0c191b", "#102023", "#c9d7d6", "#63e6c2", "#ff5c4a"),
    ("AFTERHOURS", "afterhours", "#090811", "#12101b", "#1b1728", "#f7f4ff", "#b06cff", "#c5ff4a"),
    ("BENTO POP", "bento", "#f5f0ff", "#ffffff", "#ebe3ff", "#17131f", "#6b39ff", "#c8ff62"),
    ("SOFT TERMINAL", "terminal", "#dff7ee", "#f7fffb", "#173f35", "#14211d", "#116149", "#8c5bff"),
    ("CHROME CANDY", "candy", "#d8d0ff", "#ffffff", "#f8e9ff", "#17131e", "#742cff", "#ff71c4"),
    ("FIELD NOTES", "notes", "#f2eddf", "#fffdf5", "#eee7d6", "#272b2d", "#285b68", "#e6c94a"),
    ("STREET TYPE", "street", "#e9ff42", "#f7f4ff", "#151515", "#151515", "#6a34ff", "#151515"),
    ("RAINROOM", "rain", "#0d1419", "#18242c", "#2d414c", "#dce6e9", "#a9cbd5", "#7ca7b6"),
    ("PROTOTYPE ZERO", "prototype", "#e9e9e4", "#f7f7f3", "#deded8", "#191919", "#1670ff", "#191919"),
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
    if platform == "claude":
        # Claude home layout: compact rail, centered welcome, large composer and suggestion chips.
        d.rectangle((0, 0, 118, 286), fill=panel)
        d.line((118, 0, 118, 286), fill=line, width=2)
        d.text((16, 17), "C  CLAUDE", font=font(14, True), fill=accent)
        d.rounded_rectangle((13, 53, 104, 84), radius=7, fill=panel2, outline=line)
        d.text((26, 64), "+ New chat", font=font(8), fill=text)
        d.text((16, 108), "RECENTS", font=font(7, True), fill=muted)
        d.rounded_rectangle((12, 122, 106, 150), radius=6, fill=panel2)
        d.rectangle((12, 122, 15, 150), fill=accent)
        d.text((24, 132), "AI Skins", font=font(8), fill=text)
        d.text((16, 166), "Projects", font=font(8), fill=muted)
        d.text((142, 17), name, font=font(15, True), fill=accent)
        d.text((142, 49), "Good morning", font=font(18, True), fill=text)
        d.text((142, 75), "How can I help you today?", font=font(9), fill=muted)
        d.rounded_rectangle((141, 101, 593, 177), radius=13, fill=panel, outline=line)
        d.text((159, 120), "Ask Claude anything...", font=font(9), fill=muted)
        d.rounded_rectangle((551, 136, 581, 166), radius=8, fill=accent)
        d.text((561, 141), "↑", font=font(12, True), fill=bg)
        for index, label in enumerate(("Write", "Learn", "Create")):
            left = 142 + index * 113
            d.rounded_rectangle((left, 193, left + 98, 222), radius=13, fill=panel2, outline=line)
            d.text((left + 30, 203), label, font=font(8), fill=text)
        d.rounded_rectangle((142, 239, 593, 272), radius=8, fill=panel, outline=line)
        d.text((158, 250), "AI Skins project", font=font(8, True), fill=text)
        d.text((496, 250), "Active", font=font(8), fill=accent)
        return im

    d.rectangle((0, 0, 145, 286), fill=panel)
    d.line((145, 0, 145, 286), fill=line, width=2)
    d.text((18, 18), "◇  CHATGPT", font=font(15, True), fill=accent)
    d.rounded_rectangle((14, 55, 130, 88), radius=7, fill=panel2, outline=line)
    d.text((27, 66), "+ New task", font=font(9), fill=text)
    d.text((18, 119), "WORKSPACE", font=font(8, True), fill=muted)
    d.rounded_rectangle((13, 134, 132, 166), radius=6, fill=panel2)
    d.rectangle((13, 134, 16, 166), fill=accent)
    d.text((25, 145), "Skins", font=font(9), fill=text)
    d.text((170, 20), name, font=font(16, True), fill=accent)
    d.text((170, 50), "ai-skins / main", font=font(8), fill=muted)
    d.rounded_rectangle((258, 78, 586, 116), radius=9, fill=panel2, outline=line)
    d.text((276, 91), "Make the workspace feel designed.", font=font(9), fill=text)
    d.text((170, 146), "Implemented.", font=font(11, True), fill=accent)
    d.text((170, 168), "Theme tokens applied safely.", font=font(9), fill=text)
    d.rounded_rectangle((170, 195, 585, 258), radius=8, fill=panel, outline=line)
    d.text((186, 211), "--surface: var(--skin-panel);", font=font(8), fill=text)
    d.text((186, 233), f"--accent: {accent};", font=font(8), fill=accent)
    return im

def modern_tile(skin, platform="chatgpt"):
    name, layout, bg, panel, panel2, text, accent, accent2 = skin
    im = Image.new("RGB", (620, 286), bg)
    d = ImageDraw.Draw(im)
    claude = platform == "claude"
    rail = 112 if claude else 138
    title = "What are we making?" if claude else "Design session"

    if layout == "candy":
        glow = Image.new("RGBA", im.size, (0,0,0,0))
        gd = ImageDraw.Draw(glow)
        gd.ellipse((-90,-110,260,220), fill=accent2+"88")
        gd.ellipse((420,100,760,420), fill="#77e6ff88")
        im = Image.alpha_composite(im.convert("RGBA"), glow.filter(ImageFilter.GaussianBlur(42))).convert("RGB")
        d = ImageDraw.Draw(im)
    if layout in ("control", "prototype", "notes"):
        grid = accent + ("24" if layout != "prototype" else "20")
        overlay = Image.new("RGBA", im.size, (0,0,0,0)); od = ImageDraw.Draw(overlay)
        for x in range(0,620,22): od.line((x,0,x,286), fill=grid)
        for y in range(0,286,22): od.line((0,y,620,y), fill=grid)
        im = Image.alpha_composite(im.convert("RGBA"), overlay).convert("RGB"); d=ImageDraw.Draw(im)

    if layout == "hifi":
        d.rectangle((0,0,620,42),fill="#d7cfbf"); d.text((16,14),"AI-7700 / INTEGRATED WORKSTATION",font=font(10,True),fill="#171a18")
        d.rectangle((14,54,606,224),fill=panel,outline="#706a5e",width=2); d.rectangle((14,54,rail,224),fill="#222824")
        d.text((28,72),"SOURCE",font=font(9,True),fill=accent)
        for i,s in enumerate(("01 NEW","02 CHATS","03 PROJECTS")): d.text((28,102+i*27),s,font=font(8),fill=text)
        d.text((rail+24,74),title,font=font(15,True),fill=text)
        d.rectangle((rail+24,111,586,161),fill="#2c3532",outline="#59615a"); d.text((rail+39,129),"Precision without visual noise.",font=font(9),fill=text)
        d.rectangle((rail+24,178,586,211),fill="#111615",outline="#59615a"); d.text((rail+37,189),"ASK CLAUDE..." if claude else "INPUT SIGNAL...",font=font(8),fill=accent)
        d.rectangle((14,235,606,278),fill="#c9c0ad"); d.rectangle((29,244,158,270),fill="#151a18"); d.text((38,250),"INPUT  ▮▮▮▮▯",font=font(8),fill=accent); d.text((366,249),"DECORATIVE / NO TELEMETRY",font=font(7),fill="#635e54")
    elif layout == "control":
        d.rectangle((0,0,620,38),fill=panel2); d.text((14,13),"OPS GRID // SYSTEM NOMINAL",font=font(9,True),fill=accent); d.text((538,13),platform.upper(),font=font(8,True),fill=accent2)
        d.rectangle((0,38,rail,286),fill=panel); d.rectangle((514,38,620,286),fill=panel)
        for i,s in enumerate(("SESSION","PROJECTS","LOGS")): d.text((16,68+i*34),f"0{i+1} {s}",font=font(8),fill=text)
        d.text((rail+20,62),"ACTIVE CHANNEL",font=font(9,True),fill=accent2)
        for y,label in ((100,"REQUEST 014"),(162,"RESPONSE")):
            d.rectangle((rail+20,y,494,y+48),fill=panel,outline=accent); d.text((rail+32,y+9),label,font=font(8,True),fill=accent); d.text((rail+32,y+26),"Hierarchy stable. System clear.",font=font(8),fill=text)
        d.ellipse((532,64,600,132),outline=accent,width=2); d.text((529,151),"LINK 98%",font=font(8),fill=accent2); d.text((528,252),"FAKE STATUS",font=font(7),fill=text)
    elif layout == "afterhours":
        d.rectangle((0,0,rail,286),fill=panel); d.text((18,20),"AFTER HOURS",font=font(13,True),fill=accent2)
        for i,s in enumerate(("CHATS","MIXES","PROJECTS")): d.rounded_rectangle((14,58+i*39,rail-12,87+i*39),radius=14,fill=panel2); d.text((30,68+i*39),s,font=font(8),fill=text)
        d.text((rail+25,28),title,font=font(16,True),fill=text)
        d.rounded_rectangle((rail+25,68,590,126),radius=14,fill=panel2); d.rectangle((rail+25,68,rail+29,126),fill=accent); d.text((rail+42,86),"Give the interface more pulse.",font=font(9),fill=text)
        d.rounded_rectangle((rail+25,143,590,198),radius=14,fill=panel2); d.text((rail+42,162),"Sharper rhythm. Less chrome.",font=font(9),fill=text)
        d.rounded_rectangle((rail+25,222,590,260),radius=16,fill="#f5f1ff"); d.text((rail+42,235),"Drop a thought...",font=font(8),fill="#16121f")
        d.rectangle((rail+25,272,590,278),fill="#282235"); d.rectangle((rail+25,272,rail+190,278),fill=accent2)
    elif layout == "bento":
        d.rounded_rectangle((12,12,rail-12,274),radius=22,fill=accent); d.text((30,31),"+",font=font(19,True),fill="#ffffff")
        for i,s in enumerate(("CHATS","PROJECTS","SAVED")): d.text((28,85+i*39),s,font=font(8,True),fill="#ffffff")
        d.text((rail+22,24),title,font=font(16,True),fill=text); d.text((548,24),platform.upper(),font=font(8,True),fill=accent)
        d.rounded_rectangle((rail+22,62,368,157),radius=20,fill=accent2); d.text((rail+38,81),"YOU",font=font(8,True),fill=text); d.text((rail+38,105),"Make it modular",font=font(10,True),fill=text)
        d.rounded_rectangle((382,62,600,157),radius=20,fill=panel); d.text((398,82),platform.upper(),font=font(8,True),fill=accent); d.text((398,108),"Clear. Bright. Useful.",font=font(9),fill=text)
        d.rounded_rectangle((rail+22,174,600,258),radius=20,fill=panel); d.text((rail+40,194),"Message anything...",font=font(9),fill="#716a7e")
    elif layout == "terminal":
        d.rounded_rectangle((12,12,rail-12,274),radius=20,fill=panel2); d.text((28,28),"~/ai",font=font(14,True),fill="#dff7ee")
        for i,s in enumerate(("NEW","CHATS","PROJECTS","TOOLS")): d.text((28,76+i*34),s,font=font(8),fill="#dff7ee")
        d.rounded_rectangle((rail,12,606,274),radius=20,fill=panel); d.text((rail+24,33),"claude@workspace:~$" if claude else "chatgpt@workspace:~$",font=font(10,True),fill=accent)
        d.rounded_rectangle((rail+24,73,580,119),radius=13,fill="#e7f1ed"); d.text((rail+39,89),"$ refine the interface",font=font(9),fill=text)
        d.rounded_rectangle((rail+24,137,580,190),radius=13,fill="#d8c7ff"); d.text((rail+39,154),"Done. Soft structure, crisp type.",font=font(9),fill=text)
        d.rounded_rectangle((rail+24,216,580,252),radius=12,fill="#ffffff",outline="#9dc6b8"); d.text((rail+39,228),"type a message...",font=font(8),fill=text)
    elif layout == "candy":
        d.rounded_rectangle((14,14,rail-15,272),radius=26,fill="#ffffff99",outline="#ffffff"); d.text((44,24),"✦",font=font(19,True),fill=accent)
        for i,s in enumerate(("NEW","CHATS","PROJECTS","SAVED")): d.text((30,76+i*33),s,font=font(8,True),fill=text)
        d.text((rail+22,26),title,font=font(16,True),fill=text); d.text((542,26),platform.upper(),font=font(8,True),fill=accent)
        for y,label,fill in ((66,"YOU","#ffffffcc"),(137,platform.upper(),"#f8e9ffcc")):
            d.rounded_rectangle((rail+22,y,594,y+56),radius=22,fill=fill,outline="#ffffff"); d.text((rail+39,y+11),label,font=font(8,True),fill=accent); d.text((rail+39,y+29),"Glossy, clean and usable.",font=font(9),fill=text)
        d.rounded_rectangle((rail+22,225,594,264),radius=19,fill="#ffffffcc",outline="#ffffff"); d.text((rail+39,238),"Say something...",font=font(8),fill="#655873")
    elif layout == "notes":
        d.line((76,0,76,286),fill="#d76a5c",width=2); d.text((rail+22,30),title,font=font(17,True),fill=accent)
        for i,s in enumerate(("NEW CHAT","CHATS","PROJECTS")): d.rectangle((9,44+i*49,66,79+i*49),fill=(accent2 if i!=1 else "#ef9f91")); d.text((15,57+i*49),s,font=font(7,True),fill=text)
        for y,label in ((81,"Question"),(153,"Observation")):
            d.rectangle((rail+22,y,590,y+55),fill=panel,outline="#c3bca9"); d.text((rail+37,y+10),label,font=font(9,True),fill=accent); d.text((rail+37,y+29),"How should this workspace feel?",font=font(8),fill=text)
        d.rectangle((rail+22,231,590,266),fill=panel,outline="#aea690"); d.text((rail+37,243),"Write a note...",font=font(8),fill=text)
    elif layout == "street":
        d.rectangle((0,0,rail,286),fill=bg); d.text((14,18),"MAKE\nIT\nHIT",font=font(18,True),fill=text)
        for i,s in enumerate(("NEW CHAT","RECENTS","PROJECTS")): d.text((14,119+i*31),s,font=font(8,True),fill=text)
        d.text((rail+20,22),"IDEAS WITH VOLUME.",font=font(17,True),fill=text); d.text((547,25),platform.upper(),font=font(7,True),fill=accent)
        for y,label in ((68,"YOU"),(145,platform.upper())):
            d.rectangle((rail+20,y,584,y+58),fill=panel,outline=text,width=2); d.rectangle((rail+25,y+5,589,y+63),outline=text,width=2); d.text((rail+38,y+12),label,font=font(8,True),fill=accent); d.text((rail+38,y+32),"Big voice. Clear flow.",font=font(9),fill=text)
        d.rectangle((rail+20,233,590,270),fill=text); d.text((rail+38,246),"START SOMETHING...",font=font(8,True),fill=bg)
    elif layout == "rain":
        glow=Image.new("RGBA",im.size,(0,0,0,0)); gd=ImageDraw.Draw(glow); gd.ellipse((360,-160,760,230),fill=accent+"44"); im=Image.alpha_composite(im.convert("RGBA"),glow.filter(ImageFilter.GaussianBlur(55))).convert("RGB"); d=ImageDraw.Draw(im)
        d.rectangle((0,0,rail,286),fill=panel); d.text((18,20),platform.upper(),font=font(9,True),fill=accent)
        for i,s in enumerate(("New conversation","Projects","Library")): d.text((18,66+i*32),s,font=font(8),fill=text)
        d.text((rail+28,57),title,font=font(16,True),fill=text)
        d.rounded_rectangle((rail+28,100,584,174),radius=19,fill=panel2,outline=accent2); d.text((rail+49,126),"A quiet place to think.",font=font(10),fill=text)
        d.rounded_rectangle((rail+28,222,584,264),radius=19,fill=panel2,outline=accent2); d.text((rail+49,236),"Ask anything...",font=font(8),fill=accent)
    else:
        d.rectangle((0,0,620,27),fill=text); d.text((10,9),"BUILD 0.0.7 / COMPONENT MAP",font=font(7,True),fill="#ffffff")
        d.rectangle((16,45,rail-14,266),outline=accent); d.text((27,58),"NAV",font=font(8,True),fill=accent)
        for i,s in enumerate(("NEW_CHAT","PROJECTS","SETTINGS")): d.text((27,96+i*36),s,font=font(7),fill=text)
        d.text((rail+22,48),platform.upper()+"_SURFACE",font=font(12,True),fill=text)
        for y,copy in ((83,"Build a skin that exposes its system."),(153,"TOKENS_APPLIED = TRUE")):
            d.rectangle((rail+22,y,588,y+50),outline="#777777"); d.text((rail+37,y+18),copy,font=font(8),fill=text)
        d.rectangle((rail+22,229,588,267),outline=text,width=2); d.text((rail+37,242),"INPUT_COMPONENT / READY",font=font(8),fill=text)
    return im

def sheet(title, skins, filename, signature=False, platform="chatgpt"):
    canvas = Image.new("RGB", (W, H), "#0b0c0e")
    d = ImageDraw.Draw(canvas)
    d.text((70, 56), title, font=font(34, True), fill="#f4f5f7")
    for index, skin in enumerate(skins):
        x = 70 + (index % 2) * 660
        y = 160 + (index // 2) * 318
        preview = modern_tile(skin, platform) if title.startswith("MODERN") or "/ MODERN" in title else tile(skin, signature, platform)
        canvas.paste(preview, (x, y))
    canvas.save(OUT / filename, optimize=True)

sheet("STANDARD COLLECTION", STANDARD, "standard-collection.png")
sheet("SIGNATURE COLLECTION", SIGNATURE, "signature-collection.png", signature=True)
sheet("CLAUDE / STANDARD COLLECTION", STANDARD, "claude-standard-collection.png", platform="claude")
sheet("CLAUDE / SIGNATURE COLLECTION", SIGNATURE, "claude-signature-collection.png", signature=True, platform="claude")
sheet("MODERN COLLECTION", MODERN, "modern-collection.png")
sheet("CLAUDE / MODERN COLLECTION", MODERN, "claude-modern-collection.png", platform="claude")
print("collection sheets built")
