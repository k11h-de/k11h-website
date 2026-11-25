# k11h theme

Own Pelican theme, replaces the Flex submodule. No external requests (no web fonts, no icon CDN), one small JS file, no cookies.

## skins and colour scheme

| | default | switch |
|---|---|---|
| skin | `sidebar`: sticky side card, logo gradient, blog as card grid | terminal-icon button → `terminal`: prompt bar, monospace chrome, blog as `ls -lt` list |
| colour | follows the OS (`prefers-color-scheme`) | colour button (half circle / sun / moon) cycles auto → dark → light |

Both choices are stored in `localStorage` (`k11h-skin`, `k11h-theme`). `static/js/skin.js` runs in `<head>` and writes the right stylesheet links before first paint, so there is no flash. Without JS the sidebar skin loads via `<noscript>` and the buttons stay hidden.

Both skins share one markup (`templates/`); everything visual lives in `static/css/skin-<name>.css`. Colour tokens are defined three times per skin: default, `:root[data-theme=…]` (manual switch) and `@media (prefers-color-scheme)` scoped to `:root:not([data-theme=…])` (auto).

## files

```
themes/
  k11h/templates/          base, index, article, page, tags, archives, partials
  k11h/templates/partial/logo.html   inline copy of content/images/logo.svg (ink colour from CSS)
  k11h/templates/partial/icons.html  icon(): social icons (Font Awesome Free 5.13, CC BY 4.0), ui(): switch icons (own)
  k11h/static/css/         skin-sidebar.css, skin-terminal.css, pygments-<skin>.css (generated)
  k11h/static/js/skin.js   skin + colour switch
  logos/make_logos.py      generates the logo (variant C is in use) + the two discarded variants
  gen-pygments.py          regenerates pygments-<skin>.css
  serve.sh                 local dev server: themes/serve.sh [port]
```

Regenerate syntax colours:

```bash
python themes/gen-pygments.py sidebar  xcode one-dark    light
python themes/gen-pygments.py terminal xcode github-dark dark
```

If the logo changes, update `content/images/logo.svg` and copy its `<path>`s into `partial/logo.html` (keep `class="ink"` on the prompt stroke).

## notes

- Pelican >= 4.12 no longer assigns folder categories when `CATEGORY_SAVE_AS = ''`. The templates fall back to the folder name, so old and new Pelican both work.
- The skill bars in `vita.md` carry inline colours (`#00e641` …): fine on dark, a bit faint on light backgrounds.
