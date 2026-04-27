import re

with open('jy5W-fQfL4.html', 'r', encoding='utf-8') as f:
    content = f.read()

mobile_lang_html = """  <div style="display:flex; gap:1rem; margin-top:2rem;">
    <button class="lang-btn active" style="font-size:1rem;" onclick="setLang('it'); toggleMenu()">IT</button>
    <button class="lang-btn" style="font-size:1rem;" onclick="setLang('en'); toggleMenu()">EN</button>
    <button class="lang-btn" style="font-size:1rem;" onclick="setLang('de'); toggleMenu()">DE</button>
    <button class="lang-btn" style="font-size:1rem;" onclick="setLang('fr'); toggleMenu()">FR</button>
  </div>
</div>"""

content = content.replace('<a href="#booking" onclick="toggleMenu()" data-i18n="nav.book">Prenota Ora</a>\n</div>', '<a href="#booking" onclick="toggleMenu()" data-i18n="nav.book">Prenota Ora</a>\n' + mobile_lang_html)

with open('jy5W-fQfL4.html', 'w', encoding='utf-8') as f:
    f.write(content)
