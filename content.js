(() => {
  const DEFAULTS = { enabled: true, skin: "classic", density: "comfortable", width: 92, intensity: 100 };
  const ROOT_MARKER = "data-codex-skins";

  function platform() {
    if (location.hostname === "claude.ai") return "claude";
    if (location.hostname === "chatgpt.com") return "chatgpt";
    return "unsupported";
  }

  function apply(settings) {
    const root = document.documentElement;
    const skin = CODEX_SKINS.find(item => item.id === settings.skin) || CODEX_SKINS[0];
    root.dataset.codexSkins = settings.enabled ? "on" : "off";
    root.dataset.codexPlatform = platform();
    root.dataset.codexSkin = skin.id;
    root.dataset.codexDensity = settings.density;
    for (const [key, value] of Object.entries(skin.vars)) root.style.setProperty(`--cs-${key}`, value);
    root.style.setProperty("--cs-accent2", skin.vars.accent2 || skin.vars.accent);
    root.style.setProperty("--cs-fx", skin.vars.fx || "none");
    root.style.setProperty("--cs-width", `${settings.width}rem`);
    root.style.setProperty("--cs-intensity", `${settings.intensity / 100}`);
    root.style.colorScheme = skin.dark ? "dark" : "light";
  }

  chrome.storage.local.get(DEFAULTS, apply);
  chrome.storage.onChanged.addListener((changes, area) => {
    if (area !== "local") return;
    chrome.storage.local.get(DEFAULTS, apply);
  });

  let scheduled = false;
  const observer = new MutationObserver(() => {
    if (scheduled || document.documentElement.hasAttribute(ROOT_MARKER)) return;
    scheduled = true;
    queueMicrotask(() => {
      scheduled = false;
      chrome.storage.local.get(DEFAULTS, apply);
    });
  });
  observer.observe(document.documentElement, { attributes: true, attributeFilter: [ROOT_MARKER] });

  chrome.runtime.onMessage.addListener((message, _sender, reply) => {
    if (message?.type !== "CODEX_SKINS_HEALTH") return;
    reply({ ok: true, active: document.documentElement.dataset.codexSkins === "on", skin: document.documentElement.dataset.codexSkin || null, platform: platform(), version: chrome.runtime.getManifest().version });
  });
})();
