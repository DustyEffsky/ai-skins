const CODEX_SKINS = [
  {
    id: "classic",
    name: "ChatGPT Classic",
    note: "The original, tightened up",
    swatches: ["#0d0d0d", "#212121", "#ffffff"],
    dark: true,
    vars: { bg:"#0d0d0d", panel:"#171717", panel2:"#212121", text:"#f4f4f4", muted:"#a9a9a9", accent:"#ffffff", line:"#343434", glow:"transparent", radius:"12px", font:"Inter, ui-sans-serif, system-ui" }
  },
  {
    id: "winamp",
    name: "Winamp Industrial",
    note: "Brushed metal and toxic green",
    swatches: ["#17191b", "#92ff36", "#596068"],
    dark: true,
    vars: { bg:"#0b0d0e", panel:"#1b1f22", panel2:"#2a3034", text:"#d9e0d1", muted:"#8c9789", accent:"#92ff36", line:"#596068", glow:"rgba(146,255,54,.28)", radius:"2px", font:"Tahoma, Verdana, sans-serif" }
  },
  {
    id: "amber",
    name: "Amber Terminal",
    note: "A warm monochrome CRT",
    swatches: ["#090603", "#ffb000", "#5c3c00"],
    dark: true,
    vars: { bg:"#090603", panel:"#100b05", panel2:"#191006", text:"#ffd27a", muted:"#aa7732", accent:"#ffb000", line:"#5c3c00", glow:"rgba(255,176,0,.3)", radius:"0px", font:"Consolas, 'Courier New', monospace" }
  },
  {
    id: "neon",
    name: "Neon Grid",
    note: "Arcade-night synthwave",
    swatches: ["#09051a", "#ff3fcf", "#42e8ff"],
    dark: true,
    vars: { bg:"#09051a", panel:"#130b2b", panel2:"#201044", text:"#f8edff", muted:"#a99bbd", accent:"#42e8ff", line:"#62378b", glow:"rgba(255,63,207,.32)", radius:"8px", font:"Trebuchet MS, ui-sans-serif, sans-serif" }
  },
  {
    id: "paper",
    name: "Paper & Ink",
    note: "Quiet editorial workspace",
    swatches: ["#f2eadc", "#29241e", "#b54a32"],
    dark: false,
    vars: { bg:"#f2eadc", panel:"#fbf6ec", panel2:"#e8decc", text:"#29241e", muted:"#74695c", accent:"#b54a32", line:"#cbbda7", glow:"transparent", radius:"5px", font:"Georgia, 'Times New Roman', serif" }
  },
  {
    id: "blueprint",
    name: "Blueprint",
    note: "Technical drawing table",
    swatches: ["#08284a", "#d7efff", "#3e88b8"],
    dark: true,
    vars: { bg:"#061d36", panel:"#08284a", panel2:"#0c355e", text:"#e8f7ff", muted:"#9bc2dc", accent:"#ffffff", line:"#3e88b8", glow:"rgba(137,211,255,.2)", radius:"3px", font:"Arial Narrow, Roboto Condensed, sans-serif" }
  },
  {
    id: "studio",
    name: "Studio Light",
    note: "Clean, calm, and spacious",
    swatches: ["#f6f7f8", "#ffffff", "#635bff"],
    dark: false,
    vars: { bg:"#f6f7f8", panel:"#ffffff", panel2:"#eceef2", text:"#202124", muted:"#6d7178", accent:"#635bff", line:"#d8dbe2", glow:"rgba(99,91,255,.16)", radius:"16px", font:"Inter, ui-sans-serif, system-ui" }
  },
  {
    id: "gamedev",
    name: "Game Dev Desk",
    note: "Wide canvas, compact chrome",
    swatches: ["#111820", "#1d2b38", "#ffca3a"],
    dark: true,
    vars: { bg:"#0c1218", panel:"#111c25", panel2:"#1d2b38", text:"#e8f0f5", muted:"#8ea2af", accent:"#ffca3a", line:"#314454", glow:"rgba(255,202,58,.18)", radius:"6px", font:"Barlow Condensed, Inter, sans-serif" }
  },
  {
    id: "oled",
    name: "Midnight OLED",
    note: "True black, minimal distraction",
    swatches: ["#000000", "#0a0a0a", "#7dd3fc"],
    dark: true,
    vars: { bg:"#000000", panel:"#050505", panel2:"#0a0a0a", text:"#eeeeee", muted:"#777777", accent:"#7dd3fc", line:"#232323", glow:"rgba(125,211,252,.14)", radius:"10px", font:"Inter, ui-sans-serif, system-ui" }
  },
  {
    id: "workshop",
    name: "Bavarian Workshop",
    note: "Timber, mustard, and warm plaster",
    swatches: ["#241a13", "#f0d7a6", "#d79b25"],
    dark: true,
    vars: { bg:"#17110d", panel:"#241a13", panel2:"#38271a", text:"#f0e2c4", muted:"#b6a280", accent:"#d79b25", line:"#65472e", glow:"rgba(215,155,37,.22)", radius:"4px", font:"Barlow Condensed, Trebuchet MS, sans-serif" }
  },
  {
    id:"obsidian", collection:"signature", name:"Obsidian Glass", note:"Smoked luxury glass", swatches:["#050608","#1b2028","#d8ff45"], dark:true,
    vars:{bg:"#050608",panel:"rgba(13,17,23,.91)",panel2:"rgba(24,30,39,.9)",text:"#f4f5f7",muted:"#858b96",accent:"#d8ff45",accent2:"#62e6ff",line:"#303540",glow:"rgba(216,255,69,.22)",radius:"14px",font:"Inter, system-ui",fx:"radial-gradient(circle at 72% 12%,rgba(98,230,255,.14),transparent 32%),radial-gradient(circle at 30% 90%,rgba(216,255,69,.08),transparent 35%)"}
  },
  {
    id:"chrome", collection:"signature", name:"Liquid Chrome", note:"Future hardware", swatches:["#090b10","#dce8ff","#8d62ff"], dark:true,
    vars:{bg:"#090b10",panel:"rgba(23,27,36,.92)",panel2:"#252b38",text:"#f4f7ff",muted:"#9ca7bb",accent:"#dce8ff",accent2:"#8d62ff",line:"#515b70",glow:"rgba(197,220,255,.24)",radius:"9px",font:"Inter, system-ui",fx:"linear-gradient(125deg,transparent 30%,rgba(220,232,255,.12) 46%,transparent 62%)"}
  },
  {
    id:"sakura", collection:"signature", name:"Sakura After Dark", note:"Soft neon Japan", swatches:["#130a16","#ff8fcf","#9c7cff"], dark:true,
    vars:{bg:"#110912",panel:"rgba(28,16,32,.92)",panel2:"#2b1730",text:"#ffeef8",muted:"#b997ad",accent:"#ff8fcf",accent2:"#9c7cff",line:"#633557",glow:"rgba(255,143,207,.25)",radius:"18px",font:"Inter, system-ui",fx:"radial-gradient(circle at 85% 20%,rgba(255,143,207,.22),transparent 32%),radial-gradient(circle at 15% 80%,rgba(156,124,255,.16),transparent 35%)"}
  },
  {
    id:"monolith", collection:"signature", name:"Monolith", note:"Architectural black", swatches:["#050505","#ebebeb","#ff3b30"], dark:true,
    vars:{bg:"#050505",panel:"#0b0b0b",panel2:"#151515",text:"#eeeeee",muted:"#858585",accent:"#ff3b30",accent2:"#eeeeee",line:"#323232",glow:"transparent",radius:"0px",font:"Helvetica Neue, Arial, sans-serif",fx:"linear-gradient(90deg,transparent 49.8%,rgba(255,255,255,.025) 50%,transparent 50.2%)"}
  },
  {
    id:"ivory", collection:"signature", name:"Ivory Atelier", note:"Fashion editorial", swatches:["#f5f0e6","#1e1c1a","#b58a3b"], dark:false,
    vars:{bg:"#f5f0e6",panel:"rgba(255,250,241,.94)",panel2:"#ebe2d2",text:"#211e1a",muted:"#776e63",accent:"#9a6d23",accent2:"#5e7385",line:"#c9bda9",glow:"transparent",radius:"3px",font:"Georgia, serif",fx:"linear-gradient(115deg,rgba(154,109,35,.055),transparent 42%)"}
  },
  {
    id:"abyss", collection:"signature", name:"Abyssal", note:"Deep ocean light", swatches:["#020b12","#00e5ff","#007a8c"], dark:true,
    vars:{bg:"#02080d",panel:"rgba(6,19,26,.92)",panel2:"#0a2029",text:"#e1fbff",muted:"#76a7ae",accent:"#00e5ff",accent2:"#49ffd2",line:"#174653",glow:"rgba(0,229,255,.22)",radius:"16px",font:"Inter, system-ui",fx:"radial-gradient(ellipse at 50% 0%,rgba(0,229,255,.18),transparent 45%)"}
  },
  {
    id:"ember", collection:"signature", name:"Ember Forge", note:"Heat and carbon", swatches:["#0e0907","#ff6b1a","#ffd166"], dark:true,
    vars:{bg:"#0e0907",panel:"#1c100b",panel2:"#2b1710",text:"#fff0e5",muted:"#b98d78",accent:"#ff6b1a",accent2:"#ffd166",line:"#66301c",glow:"rgba(255,107,26,.24)",radius:"5px",font:"Arial Narrow, sans-serif",fx:"radial-gradient(circle at 70% 105%,rgba(255,107,26,.28),transparent 38%)"}
  },
  {
    id:"holo", collection:"signature", name:"Holographic", note:"Iridescent clean", swatches:["#f4f7ff","#69d9ff","#ca76ff"], dark:false,
    vars:{bg:"#f3f6fb",panel:"rgba(255,255,255,.91)",panel2:"#e9eef7",text:"#1d2330",muted:"#6e7688",accent:"#6f4cff",accent2:"#00a8c8",line:"#c9d2e2",glow:"rgba(111,76,255,.16)",radius:"20px",font:"Inter, system-ui",fx:"linear-gradient(125deg,rgba(105,217,255,.13),rgba(202,118,255,.1),rgba(255,214,117,.1),transparent 70%)"}
  },
  {
    id:"toxic", collection:"signature", name:"Toxic Executive", note:"Luxury acid", swatches:["#090b08","#c8ff00","#385500"], dark:true,
    vars:{bg:"#070907",panel:"rgba(16,21,13,.93)",panel2:"#1b2415",text:"#f2f8e9",muted:"#8d9a81",accent:"#c8ff00",accent2:"#83aaff",line:"#34432c",glow:"rgba(200,255,0,.21)",radius:"11px",font:"Inter, system-ui",fx:"radial-gradient(circle at 85% 15%,rgba(200,255,0,.16),transparent 30%)"}
  },
  {
    id:"celestial", collection:"signature", name:"Celestial", note:"Cosmic restraint", swatches:["#080817","#7c9dff","#e78bff"], dark:true,
    vars:{bg:"#070713",panel:"rgba(16,16,36,.92)",panel2:"#1a1936",text:"#f2f2ff",muted:"#9b9ab8",accent:"#7c9dff",accent2:"#e78bff",line:"#3f3d68",glow:"rgba(124,157,255,.23)",radius:"17px",font:"Inter, system-ui",fx:"radial-gradient(circle at 72% 10%,rgba(231,139,255,.16),transparent 31%),radial-gradient(circle at 20% 85%,rgba(124,157,255,.13),transparent 35%)"}
  },
  {
    id:"control-room", collection:"auteur", name:"Control Room", note:"Mission-critical density", swatches:["#080b0d","#b8c5c9","#ff4d3d"], dark:true,
    vars:{bg:"#080b0d",panel:"#101518",panel2:"#182024",text:"#d8e1e3",muted:"#77868b",accent:"#ff4d3d",accent2:"#62d6a6",line:"#344148",glow:"rgba(255,77,61,.18)",radius:"2px",font:"Arial Narrow, Roboto Condensed, sans-serif",fx:"repeating-linear-gradient(90deg,transparent 0 79px,rgba(184,197,201,.025) 80px)"}
  },
  {
    id:"directors-cut", collection:"auteur", name:"Director's Cut", note:"A cinematic editing suite", swatches:["#090909","#242424","#d9382b"], dark:true,
    vars:{bg:"#090909",panel:"#111111",panel2:"#202020",text:"#e9e4dc",muted:"#817d77",accent:"#d9382b",accent2:"#d6b06a",line:"#383532",glow:"rgba(217,56,43,.16)",radius:"1px",font:"Helvetica Neue, Arial, sans-serif",fx:"linear-gradient(180deg,rgba(255,255,255,.018),transparent 28%)"}
  },
  {
    id:"archive", collection:"auteur", name:"The Archive", note:"Catalogued research papers", swatches:["#e8e0cf","#2c2924","#8b2e27"], dark:false,
    vars:{bg:"#e8e0cf",panel:"#f4eddf",panel2:"#ddd2bd",text:"#2c2924",muted:"#756d60",accent:"#8b2e27",accent2:"#315f68",line:"#b9ad98",glow:"transparent",radius:"0px",font:"Georgia, Times New Roman, serif",fx:"repeating-linear-gradient(0deg,transparent 0 31px,rgba(74,66,54,.045) 32px)"}
  },
  {
    id:"braun", collection:"auteur", name:"Braun Workshop", note:"German industrial clarity", swatches:["#d7d2c8","#343432","#e85d04"], dark:false,
    vars:{bg:"#d7d2c8",panel:"#e8e4dc",panel2:"#c7c1b6",text:"#272725",muted:"#6f6b64",accent:"#e85d04",accent2:"#397a78",line:"#aaa49a",glow:"transparent",radius:"4px",font:"Helvetica Neue, Arial, sans-serif",fx:"linear-gradient(90deg,rgba(255,255,255,.12),transparent 35%)"}
  },
  {
    id:"hotel-noir", collection:"auteur", name:"Hotel Noir", note:"Walnut, brass and burgundy", swatches:["#130d0d","#3a171b","#c5a15a"], dark:true,
    vars:{bg:"#130d0d",panel:"#211315",panel2:"#351b1f",text:"#eadfcf",muted:"#9f8c7d",accent:"#c5a15a",accent2:"#7e2631",line:"#594039",glow:"rgba(197,161,90,.16)",radius:"7px",font:"Georgia, Times New Roman, serif",fx:"radial-gradient(circle at 85% 5%,rgba(126,38,49,.2),transparent 34%)"}
  },
  {
    id:"field-notes", collection:"auteur", name:"Field Notes", note:"A designer's working notebook", swatches:["#e8e3d4","#fffdf5","#e6c62f"], dark:false,
    vars:{bg:"#e8e3d4",panel:"#f6f1e4",panel2:"#dfd8c6",text:"#262b2d",muted:"#687075",accent:"#d04c3f",accent2:"#e6c62f",line:"#b9b29f",glow:"transparent",radius:"2px",font:"Trebuchet MS, ui-sans-serif, sans-serif",fx:"linear-gradient(rgba(61,105,122,.09) 1px,transparent 1px),linear-gradient(90deg,rgba(61,105,122,.09) 1px,transparent 1px)"}
  },
  {
    id:"japanese-hifi", collection:"auteur", name:"Japanese Hi-Fi", note:"Seventies precision audio", swatches:["#c7bda8","#292b29","#63d7c5"], dark:true,
    vars:{bg:"#181a19",panel:"#252825",panel2:"#343833",text:"#eee8db",muted:"#999384",accent:"#63d7c5",accent2:"#e7a93d",line:"#686454",glow:"rgba(99,215,197,.17)",radius:"3px",font:"Arial, Helvetica, sans-serif",fx:"repeating-linear-gradient(0deg,rgba(255,255,255,.018) 0 1px,transparent 1px 3px)"}
  },
  {
    id:"editorial-red", collection:"auteur", name:"Editorial Red", note:"Severe Swiss typography", swatches:["#f2f0eb","#141414","#e1251b"], dark:false,
    vars:{bg:"#f2f0eb",panel:"#ffffff",panel2:"#e8e5de",text:"#141414",muted:"#686868",accent:"#e1251b",accent2:"#141414",line:"#bcb8b0",glow:"transparent",radius:"0px",font:"Helvetica Neue, Arial, sans-serif",fx:"linear-gradient(90deg,transparent 0 12%,rgba(225,37,27,.035) 12% 12.2%,transparent 12.2%)"}
  },
  {
    id:"rainroom", collection:"auteur", name:"Rainroom", note:"Quiet glass in a storm", swatches:["#10171d","#293944","#8eb8c7"], dark:true,
    vars:{bg:"#10171d",panel:"rgba(25,35,43,.9)",panel2:"rgba(42,57,67,.86)",text:"#dbe4e7",muted:"#8b9ba2",accent:"#8eb8c7",accent2:"#b8a6d9",line:"#435660",glow:"rgba(142,184,199,.14)",radius:"18px",font:"Inter, ui-sans-serif, system-ui",fx:"linear-gradient(115deg,rgba(174,205,214,.07),transparent 30%),radial-gradient(circle at 80% 10%,rgba(108,136,163,.16),transparent 35%)"}
  },
  {
    id:"prototype-zero", collection:"auteur", name:"Prototype Zero", note:"The internal build escaped", swatches:["#e9e9e4","#1b1b1b","#006cff"], dark:false,
    vars:{bg:"#e9e9e4",panel:"#f7f7f3",panel2:"#deded8",text:"#1b1b1b",muted:"#66665f",accent:"#006cff",accent2:"#ff2d55",line:"#92928c",glow:"transparent",radius:"0px",font:"Consolas, SFMono-Regular, monospace",fx:"linear-gradient(rgba(0,108,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(0,108,255,.07) 1px,transparent 1px)"}
  }
];

if (typeof globalThis !== "undefined") globalThis.CODEX_SKINS = CODEX_SKINS;
