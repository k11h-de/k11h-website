/* k11h skin + colour-scheme switch.
   Runs synchronously in <head>: picks the stylesheet before first paint (no flash),
   then wires the two buttons once the DOM is there. No cookies, only localStorage. */
(function () {
  var d = document.documentElement;
  var me = document.currentScript;
  var base = me.getAttribute('data-css');
  var SKINS = ['sidebar', 'terminal'];
  var THEMES = ['auto', 'dark', 'light'];
  var LABEL = { auto: 'Farbschema: automatisch', dark: 'Farbschema: dunkel', light: 'Farbschema: hell' };

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function put(k, v) { try { v ? localStorage.setItem(k, v) : localStorage.removeItem(k); } catch (e) {} }

  var skin = SKINS.indexOf(get('k11h-skin')) > 0 ? get('k11h-skin') : 'sidebar';
  var theme = THEMES.indexOf(get('k11h-theme')) > 0 ? get('k11h-theme') : 'auto';
  d.setAttribute('data-skin', skin);
  if (theme !== 'auto') d.setAttribute('data-theme', theme);

  document.write(
    '<link id="skin-css" rel="stylesheet" href="' + base + 'skin-' + skin + '.css">' +
    '<link id="skin-pyg" rel="stylesheet" href="' + base + 'pygments-' + skin + '.css">'
  );

  function setSkin(s) {
    skin = s;
    d.setAttribute('data-skin', s);
    document.getElementById('skin-css').href = base + 'skin-' + s + '.css';
    document.getElementById('skin-pyg').href = base + 'pygments-' + s + '.css';
    put('k11h-skin', s === 'sidebar' ? null : s);
  }
  function setTheme(t) {
    theme = t;
    if (t === 'auto') d.removeAttribute('data-theme'); else d.setAttribute('data-theme', t);
    put('k11h-theme', t === 'auto' ? null : t);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var tools = document.querySelector('.side__tools');
    if (!tools) return;
    var tb = tools.querySelector('[data-action=theme]');
    var sb = tools.querySelector('[data-action=skin]');
    function paint() {
      tb.setAttribute('data-state', theme);
      tb.setAttribute('aria-label', LABEL[theme]);
      tb.title = LABEL[theme];
      sb.setAttribute('aria-pressed', skin === 'terminal' ? 'true' : 'false');
    }
    tb.addEventListener('click', function () { setTheme(THEMES[(THEMES.indexOf(theme) + 1) % THEMES.length]); paint(); });
    sb.addEventListener('click', function () { setSkin(skin === 'terminal' ? 'sidebar' : 'terminal'); paint(); });
    paint();
    tools.hidden = false;
  });
})();
