# Contributing

ChatGPT + Codex Skins is intentionally conservative: a broken enhancement should disappear, never make ChatGPT unusable.

## Skin contributions

- Add palette data to `skins.js`.
- Prefer shared CSS custom properties over page-specific selectors.
- Keep text contrast readable in conversation and code views.
- Avoid remote fonts, scripts, analytics, and network requests.

## Compatibility fixes

- Do not target generated or obfuscated class names.
- Prefer semantic elements, ARIA roles, stable data attributes, and shared CSS variables.
- Keep every rule under the master root attribute so the switch is a true kill switch.
- Test the original appearance after switching the extension off.

## Useful bug reports

Include browser/version, extension version, affected skin, page type, screenshot, and the shortest reproduction sequence. Never include private conversation content.
