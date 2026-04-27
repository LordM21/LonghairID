import re

with open('jy5W-fQfL4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace old rgb values
content = content.replace('rgba(10,8,6,', 'rgba(59,42,39,')
content = content.replace('rgba(201,169,110,', 'rgba(255,182,193,')

# 2. Add scrollbar styling
scrollbar_css = """
/* Custom scrollbar */
::-webkit-scrollbar { width: 10px; }
::-webkit-scrollbar-track { background: var(--off-black); }
::-webkit-scrollbar-thumb { background: var(--gold-dark); border-radius: 5px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }
"""
content = content.replace('/* Custom cursor */', scrollbar_css + '\n/* Custom cursor */')

# 3. Move language bar inside nav and fix css
lang_bar_html = """<!-- Language Bar -->
<div class="lang-bar" id="lang-bar">
  <button class="lang-btn active" onclick="setLang('it')">IT</button>
  <span class="lang-sep">·</span>
  <button class="lang-btn" onclick="setLang('en')">EN</button>
  <span class="lang-sep">·</span>
  <button class="lang-btn" onclick="setLang('de')">DE</button>
  <span class="lang-sep">·</span>
  <button class="lang-btn" onclick="setLang('fr')">FR</button>
</div>"""

content = content.replace(lang_bar_html, '')

new_nav_html = """<nav id="main-nav">
  <a href="#" class="nav-logo">LongHairID<span>Percorsi d'Identità</span></a>
  <div class="nav-links">
    <a href="#philosophy" data-i18n="nav.philosophy">Filosofia</a>
    <a href="#services" data-i18n="nav.services">Servizi</a>
    <a href="#fhair" data-i18n="nav.method">Metodo</a>
    <a href="#treatments" data-i18n="nav.treatments">Trattamenti</a>
    <a href="#" onclick="openPriceModal()" data-i18n="nav.prices">Listino</a>
    <a href="#booking" class="nav-cta" data-i18n="nav.book">Prenota</a>
    <div class="lang-bar" id="lang-bar" style="position:static; padding:0; margin-left:1rem;">
      <button class="lang-btn active" onclick="setLang('it')">IT</button>
      <span class="lang-sep">·</span>
      <button class="lang-btn" onclick="setLang('en')">EN</button>
      <span class="lang-sep">·</span>
      <button class="lang-btn" onclick="setLang('de')">DE</button>
      <span class="lang-sep">·</span>
      <button class="lang-btn" onclick="setLang('fr')">FR</button>
    </div>
  </div>
  <div class="nav-menu-toggle" id="menu-toggle" onclick="toggleMenu()">
    <span></span><span></span><span></span>
  </div>
</nav>"""

# Replace old nav
old_nav_html_start = '<nav id="main-nav">'
old_nav_html_end = '</nav>'
start_idx = content.find(old_nav_html_start)
end_idx = content.find(old_nav_html_end, start_idx) + len(old_nav_html_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_nav_html + content[end_idx:]

with open('jy5W-fQfL4.html', 'w', encoding='utf-8') as f:
    f.write(content)
