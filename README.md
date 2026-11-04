# SUPERMAN Browser

SUPERMAN Browser is a self-hosted browser-proxy project with custom branding,
icons, a new look and a separate GitHub repository. It uses the open-source
InvisiProxy LTS proxy engine and retains upstream licenses and copyright notices.

## Start in GitHub Codespaces

Use the latest compatible Node.js version (upstream currently recommends Node 26.x).
Then run:

```bash
pnpm run fresh-install
pnpm start
```

From Codespaces **Ports**, copy the forwarded app URL to **SUPERMAN → Proxy → I'm Hosting**.

## License, source and attribution

This is a modified version of InvisiProxy LTS (GNU AGPLv3).
See [LICENSE](LICENSE), [source attribution](SUPERMAN-UPSTREAM-NOTICE.md), and
[original upstream README](UPSTREAM-README.md). Modified branding scripts and
assets are in [superman-branding/](superman-branding/).

The application does not guarantee that every third-party website works via proxy.
A public Codespaces port is accessible by anyone with its URL; add separate
proxy authentication if access should be limited to signed-in members.
