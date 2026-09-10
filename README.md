# AI Skins

A Winamp-inspired skin system for ChatGPT, Codex, and Claude. Switch between 30 visual identities, including ten layout-led Modern skins that reshape spacing, navigation, message surfaces, typography, texture, and controls without changing how the underlying apps work.

> Unofficial community project. Not affiliated with or endorsed by OpenAI or Anthropic. ChatGPT, Codex, and Claude are trademarks of their respective owners.

![Slow split-screen preview cycling through all 30 AI Skins on ChatGPT and Claude](screenshots/all-30-skins-slow.gif)

![All ten Standard skins arranged two abreast](screenshots/standard-collection.png)

![All ten Signature skins arranged two abreast](screenshots/signature-collection.png)

![All ten Modern skins arranged two abreast](screenshots/modern-collection.png)

![All ten Standard skins shown on Claude](screenshots/claude-standard-collection.png)

![All ten Signature skins shown on Claude](screenshots/claude-signature-collection.png)

![All ten Modern skins shown on Claude](screenshots/claude-modern-collection.png)

## What it does

- Applies palettes, typography, surfaces, borders, spacing, navigation treatments, glow, and optional texture effects.
- Includes **10 Standard skins**, **10 Signature skins**, and **10 Modern skins**.
- Adds Compact, Comfortable and Airy interface-density options.
- Adjusts the maximum workspace width for focused or ultrawide layouts.
- Stores every preference locally and makes no network requests.
- Provides a master switch that immediately restores the original interface.
- Uses conservative semantic styling so individual enhancements fail safely when a supported interface changes.

## Install locally

1. Unzip the package.
2. Open `chrome://extensions` in Chrome or `edge://extensions` in Edge.
3. Enable **Developer mode**.
4. Choose **Load unpacked** and select the `ai-skins` folder.
5. Open or refresh `https://chatgpt.com` or `https://claude.ai`, then click the extension icon.

## Included skins: Standard

1. ChatGPT Classic
2. Winamp Industrial
3. Amber Terminal
4. Neon Grid
5. Paper & Ink
6. Blueprint
7. Studio Light
8. Game Dev Desk
9. Midnight OLED
10. Bavarian Workshop

## Included skins: Signature

1. Obsidian Glass
2. Liquid Chrome
3. Sakura After Dark
4. Monolith
5. Ivory Atelier
6. Abyssal
7. Ember Forge
8. Holographic
9. Toxic Executive
10. Celestial

Each skin can be combined with Compact, Comfortable, or Airy density, a custom workspace width, and adjustable texture intensity.

## Included skins: Modern

1. Japanese Hi-Fi
2. Control Room
3. Afterhours
4. Bento Pop
5. Soft Terminal
6. Chrome Candy
7. Field Notes
8. Street Type
9. Rainroom
10. Prototype Zero

The Modern collection goes beyond recoloring. Each skin has isolated layout rules and its own type, geometry, navigation, message, and input treatment. Japanese Hi-Fi includes an animated signal display that is purely decorative. It is labeled **Decorative loop / no telemetry**, reads no conversation data, and stops animating when reduced motion is enabled.

## Safety and limitations

- The extension runs only on `chatgpt.com` and `claude.ai` and stores preferences locally.
- It requests no browsing-history, network, or account permissions.
- Interface updates can change internal layout selectors. Separate platform adapters rely primarily on semantic CSS variables to reduce breakage and isolate failures.
- Turn the master switch off to immediately restore the original appearance.
- The popup reports whether the extension is connected to the current ChatGPT, Codex, or Claude tab.
- Screenshots and GIFs are representative mockups, not claims of pixel-identical rendering across every account, experiment, or interface revision.

## Compatibility policy

The base palette layer uses shared CSS variables. ChatGPT and Claude compatibility rules are isolated by platform. Modern layout adjustments are isolated by skin, use broad semantic selectors, and fail independently. Generated class names are deliberately avoided. If a platform changes, the palette layer should continue working even when an optional structural enhancement no longer matches. Compatibility reports are welcome through the included GitHub issue template.

## Development

Edit `skins.js` to add themes. Skin-specific structural rules live in clearly separated blocks in `content.css`. Reload the extension from the browser extensions page after changing files.
