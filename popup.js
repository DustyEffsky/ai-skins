const DEFAULTS = { enabled: true, skin: "classic", density: "comfortable", width: 92, intensity: 100 };
const $ = id => document.getElementById(id);
let state = { ...DEFAULTS };

function save(patch) {
  state = { ...state, ...patch };
  chrome.storage.local.set(patch);
  render();
}

function render() {
  $("enabled").checked = state.enabled;
  $("density").value = state.density;
  $("width").value = state.width;
  $("intensity").value = state.intensity;
  $("widthOut").textContent = `${state.width} rem`;
  $("intensityOut").textContent = `${state.intensity}%`;
  document.querySelectorAll(".skin").forEach(el => el.classList.toggle("active", el.dataset.skin === state.skin));
}

function buildSkins() {
  const groups = [
    ["standard", "Standard", CODEX_SKINS.filter(skin => !skin.collection)],
    ["signature", "Signature", CODEX_SKINS.filter(skin => skin.collection === "signature")],
    ["auteur", "Auteur", CODEX_SKINS.filter(skin => skin.collection === "auteur")]
  ];
  $("skins").innerHTML = groups.map(([, label, skins]) => `
    <h2 class="collection-title">${label}</h2>
    ${skins.map(skin => `
    <button class="skin" data-skin="${skin.id}" title="${skin.name}">
      <span class="swatches">${skin.swatches.map(color => `<i style="background:${color}"></i>`).join("")}</span>
      <span><strong>${skin.name}</strong><small>${skin.note}</small></span>
    </button>`).join("")}`).join("");
  document.querySelectorAll(".skin").forEach(el => el.addEventListener("click", () => save({skin: el.dataset.skin, enabled: true})));
}

buildSkins();
chrome.storage.local.get(DEFAULTS, stored => { state = stored; render(); });
$("enabled").addEventListener("change", e => save({enabled:e.target.checked}));
$("density").addEventListener("change", e => save({density:e.target.value}));
$("width").addEventListener("input", e => save({width:Number(e.target.value)}));
$("intensity").addEventListener("input", e => save({intensity:Number(e.target.value)}));
$("reset").addEventListener("click", () => { state={...DEFAULTS}; chrome.storage.local.set(state,render); });

chrome.tabs.query({active:true,currentWindow:true}, tabs => {
  const tab = tabs[0];
  const health = $("health");
  const setHealth = (kind, value) => { health.className = `health ${kind}`; health.querySelector("span").textContent = value; };
  const supported = tab?.url?.startsWith("https://chatgpt.com/") || tab?.url?.startsWith("https://claude.ai/");
  if (!supported) return setHealth("warn", "Open ChatGPT, Codex, or Claude to preview skins");
  chrome.tabs.sendMessage(tab.id, {type:"CODEX_SKINS_HEALTH"}, response => {
    if (chrome.runtime.lastError || !response?.ok) setHealth("warn", "Refresh this page after installation");
    else {
      const label = response.platform === "claude" ? "Claude" : "ChatGPT / Codex";
      setHealth("ok", `${label} connected · ${response.skin || "original"}`);
    }
  });
});
