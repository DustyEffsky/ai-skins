const CODEX_SKINS = [
  {
    id: "classic",
    name: "Codex Classic",
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
  }
];

if (typeof globalThis !== "undefined") globalThis.CODEX_SKINS = CODEX_SKINS;
