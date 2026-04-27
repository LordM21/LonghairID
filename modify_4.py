import re

with open('jy5W-fQfL4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Fix Image in FHAIR section
content = content.replace('src="https://leadpages.com/PLACEHOLDER_FHAIR"', 'src="images/fhair_cutting.png"')

# 2. Add Google Maps
map_html = """<!-- Location Map -->
<section style="height: 450px; width: 100%; border-top: 1px solid rgba(255,182,193,.1);">
  <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2799.308709355708!2d11.0205844!3d45.4433604!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x477f5f44a8060c23%3A0xc3f6cb42e472ebf8!2sVia%20Montorio%2C%2064%2C%2037131%20Verona%20VR!5e0!3m2!1sen!2sit!4v1700000000000!5m2!1sen!2sit" width="100%" height="100%" style="border:0; filter: grayscale(100%) invert(90%) hue-rotate(180deg) contrast(1.2);" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
</section>

<!-- Info Bar -->"""
content = content.replace('<!-- Info Bar -->', map_html)

# 3. Restructure Price Modal (Payment Stuff)
old_price_start = '<div class="price-title" data-i18n="price.title">Listino Prezzi</div>'
old_price_end = 'Prenota la tua consulenza gratuita per un preventivo personalizzato.</p>'

new_price_html = """<div class="price-title" style="text-align:center; margin-bottom: 0.5rem;" data-i18n="price.title">I Nostri Percorsi</div>
    <p style="text-align:center; color:var(--text-muted); font-size: 0.85rem; margin-bottom: 2.5rem;">Oltre 2,000+ clienti soddisfatte. Scegli il percorso adatto alla tua identità.</p>
    
    <div class="pricing-tiers" style="display:flex; gap:1.5rem; margin-bottom: 2rem; flex-wrap: wrap; justify-content: center;">
      <!-- Tier 1: Decoy / Basic -->
      <div class="tier-card" style="flex: 1; min-width: 250px; padding: 2rem; border: 1px solid rgba(255,182,193,.2); border-radius: 12px; text-align: center; background: var(--off-black);">
        <h3 style="font-family: var(--heading); font-size: 1.5rem; color: var(--text);">Essenziale</h3>
        <p style="font-size: 0.75rem; color: var(--text-muted); margin: 1rem 0;">Per chi cerca un aggiornamento veloce e curato.</p>
        <div style="font-family: var(--heading); font-size: 2.5rem; color: var(--gold); margin: 1.5rem 0;">€89<span style="font-size:1.2rem">.99</span></div>
        <ul style="list-style:none; padding:0; text-align:left; font-size: 0.85rem; color: var(--text-muted); line-height: 2;">
          <li>✓ Taglio FHAIR™ (medi)</li>
          <li>✓ Piega &amp; Styling</li>
          <li style="opacity:0.5">✕ Consulenza Identitaria</li>
          <li style="opacity:0.5">✕ Trattamento Colore</li>
        </ul>
      </div>

      <!-- Tier 2: Most Popular (Center Stage) -->
      <div class="tier-card popular" style="flex: 1; min-width: 250px; padding: 2rem; border: 2px solid var(--gold); border-radius: 12px; text-align: center; background: rgba(255,182,193,.05); position: relative; z-index: 2;">
        <div style="position:absolute; top:-12px; left:50%; transform:translateX(-50%); background:var(--gold); color:var(--black); font-size:0.65rem; padding:0.2rem 1rem; border-radius:20px; font-weight:bold; letter-spacing:0.1em; text-transform:uppercase;">Più Richiesto</div>
        <h3 style="font-family: var(--heading); font-size: 1.8rem; color: var(--text);">Signature</h3>
        <p style="font-size: 0.75rem; color: var(--text-muted); margin: 1rem 0;">L'esperienza LongHairID completa per ridefinire la tua identità.</p>
        <div style="font-family: var(--heading); font-size: 3rem; color: var(--gold); margin: 1.5rem 0;">€149<span style="font-size:1.5rem">.99</span></div>
        <ul style="list-style:none; padding:0; text-align:left; font-size: 0.85rem; color: var(--text-muted); line-height: 2;">
          <li>✓ Taglio FHAIR™ (lunghi)</li>
          <li>✓ Consulenza Ascolto-Armo-Cromia</li>
          <li>✓ Piega &amp; Styling Avanzato</li>
          <li>✓ Trattamento Ristrutturante</li>
        </ul>
        <a href="#booking" onclick="closePriceModal()" style="display:block; margin-top:1.5rem; background:var(--gold); color:var(--black); padding:0.8rem; text-decoration:none; text-transform:uppercase; font-size:0.75rem; letter-spacing:0.1em; font-weight:bold;">Prenota Ora</a>
      </div>

      <!-- Tier 3: Elite / Prestige -->
      <div class="tier-card" style="flex: 1; min-width: 250px; padding: 2rem; border: 1px solid rgba(255,182,193,.2); border-radius: 12px; text-align: center; background: var(--off-black);">
        <h3 style="font-family: var(--heading); font-size: 1.5rem; color: var(--text);">Elite</h3>
        <p style="font-size: 0.75rem; color: var(--text-muted); margin: 1rem 0;">La trasformazione cromatica e strutturale definitiva.</p>
        <div style="font-family: var(--heading); font-size: 2.5rem; color: var(--gold); margin: 1.5rem 0;">€299<span style="font-size:1.2rem">.00</span></div>
        <ul style="list-style:none; padding:0; text-align:left; font-size: 0.85rem; color: var(--text-muted); line-height: 2;">
          <li>✓ Tutto nel pacchetto Signature</li>
          <li>✓ Tiger Eye Coloring o Balayage</li>
          <li>✓ Velvet Smoothing</li>
          <li>✓ Priority Booking</li>
        </ul>
        <p style="color:#ffb6c1; font-size:0.75rem; margin-top:1.5rem; font-weight:bold; padding:0.5rem; background:rgba(255,182,193,0.1); border-radius:4px;">⏳ Solo 3 posti rimasti per questa settimana!</p>
      </div>
    </div>
    <style>
      @media(min-width: 900px){
        .tier-card.popular { transform: scale(1.05); }
      }
    </style>"""

start_idx = content.find(old_price_start)
end_idx = content.find(old_price_end, start_idx) + len(old_price_end)

if start_idx != -1 and end_idx != -1:
    content = content[:start_idx] + new_price_html + content[end_idx:]

with open('jy5W-fQfL4.html', 'w', encoding='utf-8') as f:
    f.write(content)
