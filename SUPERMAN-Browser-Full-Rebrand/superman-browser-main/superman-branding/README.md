# SUPERMAN BROWSER — InvisiProxy LTS Edition

This is a **cosmetic fork/rebrand of InvisiProxy LTS**, not a new engine. It takes the official upstream repository and updates its **visible names, headings, favicon, home-page logos, navigation icon style, browser metadata, and website colors**. It deliberately leaves Scramjet/Wisp/transports/service workers and routing names unchanged, so that changing a brand doesn't break proxy compatibility.

## 1. In GitHub Codespaces

Upload this entire folder into your Codespace. Then open a terminal inside the folder:

```bash
bash setup.sh
```

That clones `https://github.com/InvisiProxy/InvisiProxyLTS` into `SUPERMAN-BROWSER/` and applies the branding. If you already cloned InvisiProxy, you can instead do:

```bash
python3 brand_superman.py /path/to/your/InvisiProxyLTS
```

**Node.js 26.x is required by current InvisiProxy.** Then:

```bash
cd SUPERMAN-BROWSER
pnpm run fresh-install
pnpm start
```

The official InvisiProxy LTS documentation lists these Codespaces startup commands. If your checkout requires a different package manager command, follow the repo README. The branding tool has been tested on a fixture, not against a full live clone.

## 2. Link it to the existing SUPERMAN (Zite) chat

In GitHub Codespaces → **Ports**, identify the port reported by `pnpm start` (InvisiProxy's default is **8080**). Set the forwarded port to **Public** if you wish other members to access it, copy its HTTPS URL, then go to your existing **SUPERMAN → Proxy → I'm Hosting** and share that URL.

Other members can now click **Join Shared Proxy** and see SUPERMAN-branded InvisiProxy.

**Important:** A publicly forwarded InvisiProxy port can be opened by *anyone who knows the link*. Zite membership hides the link in the app but does **not** authenticate visitors at the Codespaces proxy. For a genuinely private proxy, add separate server-side authentication; do not rely on a hidden URL. Only share with people you trust. Respect network/service rules.

## What changes

- Site headings, titles, visible copy, and translated branding text: **SUPERMAN BROWSER**.
- InvisiProxy-owned brand logos, hero graphic, favicon, homescreen icons → custom SUPERMAN S-emblem.
- Browser and install metadata updated.
- Original-styled navigation icons replaced with a custom unified icon family and purple/cyan accents.
- Google, TikTok, Discord, Chess.com and other **third-party logos remain recognizable**.
- Includes runtime fallback for any dynamically generated original brand labels in the UI.

## What does not change

- Proxy engine internals, service worker paths, Wisp, Scramjet, networking protocols, URLs, package identities.
- The original repository's **LICENSE, Credits and copyright notices**. Attribution is preserved as legally required. The tool adds `SUPERMAN-UPSTREAM-NOTICE.md`.

**Version note:** This script fetches upstream's latest `master` on first install; the exact merged commit and TikTok compatibility depend on what is in `master` when you run it. For a pinned, tested version, start from the known working commit before applying the branding. Current upstream notes warn that `master` may have experimental work.

### Source license

The upstream project is published under AGPL-3.0. If you make this modified version available over a network, **make the complete corresponding modified source available to users**, including the overlay script and icons (for example by publishing your own fork). Retain upstream notices, credits and license.
