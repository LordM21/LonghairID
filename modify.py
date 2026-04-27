import re

with open('jy5W-fQfL4.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Colors
content = content.replace(
""":root {
  --gold: #C9A96E;
  --gold-light: #E8D5B0;
  --gold-dark: #8B6B3D;
  --black: #0A0806;
  --off-black: #121010;
  --dark: #1A1612;
  --mid: #2C2420;
  --surface: #1E1A16;
  --text: #F2EDE6;
  --text-muted: #8C7E72;
  --text-dim: #5C504A;""",
""":root {
  --gold: #FFB6C1;
  --gold-light: #FFD1DC;
  --gold-dark: #D87093;
  --black: #3B2A27;
  --off-black: #4A3531;
  --dark: #5A403C;
  --mid: #6C4E49;
  --surface: #4A3531;
  --text: #FFF0F5;
  --text-muted: #E6C8C8;
  --text-dim: #BFA0A0;"""
)

# 2. Hero and Pad sizes
content = content.replace('clamp(4rem,10vw,9rem)', 'clamp(2.5rem,6vw,5rem)')
content = content.replace('padding:8rem 4rem', 'padding:5rem 2rem')
content = content.replace('clamp(2.5rem,5vw,4.5rem)', 'clamp(1.8rem,4vw,3.5rem)')

# 3. Flexboxes
content = content.replace(
    '.services-grid{max-width:1400px;margin:0 auto;display:grid;grid-template-columns:repeat(4,1fr);gap:1.5px;background:rgba(201,169,110,.1)}',
    '.services-grid{max-width:1400px;margin:0 auto;display:flex;flex-wrap:wrap;justify-content:center;gap:1.5rem;background:transparent}'
)
content = content.replace(
    '.service-card{background:var(--black);padding:3rem 2rem;position:relative;overflow:hidden;transition:all .5s cubic-bezier(.16,1,.3,1);cursor:pointer}',
    '.service-card{flex:1 1 250px;max-width:320px;border-radius:12px;background:var(--off-black);padding:3rem 2rem;position:relative;overflow:hidden;transition:all .5s cubic-bezier(.16,1,.3,1);cursor:pointer}'
)
content = content.replace(
    '.treatments-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:2rem}',
    '.treatments-grid{display:flex;flex-wrap:wrap;justify-content:center;gap:2rem}'
)
content = content.replace(
    '.treatment-card{position:relative;overflow:hidden;aspect-ratio:3/4;background:var(--dark);cursor:pointer}',
    '.treatment-card{flex:1 1 300px;max-width:400px;border-radius:12px;position:relative;overflow:hidden;aspect-ratio:3/4;background:var(--dark);cursor:pointer}'
)

# 4. Empty styles
content = content.replace(' style=""', '')

# 5. Images and treatments
treatments_orig = """      <div class="treatment-card reveal">
        <img src="https://leadpages.com/PLACEHOLDER_TIGER" alt="Tiger Eye coloring capelli lunghi Verona">
        <div class="treatment-card-overlay"></div>
        <div class="treatment-card-content">
          <div class="treatment-tag" data-i18n="treat.t1.tag">Colorazione esclusiva</div>
          <h3 class="treatment-name">Tiger Eye</h3>
          <p class="treatment-desc" data-i18n="treat.t1.desc">Riflessi ambrati, dorati e bruniti che si intrecciano come le venature di un occhio di tigre. Profondità e luminosità senza pari.</p>
        </div>
      </div>
      <div class="treatment-card reveal">
        <img src="https://leadpages.com/PLACEHOLDER_BEACH" alt="BeachWave trattamento texture capelli lunghi">
        <div class="treatment-card-overlay"></div>
        <div class="treatment-card-content">
          <div class="treatment-tag" data-i18n="treat.t2.tag">Texture naturale</div>
          <h3 class="treatment-name">BeachWave</h3>
          <p class="treatment-desc" data-i18n="treat.t2.desc">Il movimento del mare catturato nei tuoi capelli. Onde morbide e definite che durano nel tempo con cura minima.</p>
        </div>
      </div>
      <div class="treatment-card reveal">
        <img src="https://leadpages.com/PLACEHOLDER_VELVET" alt="Velvet smoothing trattamento lisciante capelli lunghi">
        <div class="treatment-card-overlay"></div>
        <div class="treatment-card-content">
          <div class="treatment-tag" data-i18n="treat.t3.tag">Liscio vellutato</div>
          <h3 class="treatment-name">Velvet</h3>
          <p class="treatment-desc" data-i18n="treat.t3.desc">La texture del velluto nei tuoi capelli: liscio, setoso, con una lucentezza che toglie il fiato. Il lusso quotidiano.</p>
        </div>
      </div>"""

treatments_new = """      <div class="treatment-card reveal">
        <img src="images/pink_hair.png" alt="Wavy Pink Hair">
        <div class="treatment-card-overlay"></div>
        <div class="treatment-card-content">
          <div class="treatment-tag">Colore e Onde</div>
          <h3 class="treatment-name">Wavy Pink</h3>
          <p class="treatment-desc">Una colorazione audace unita a onde morbide che valorizzano il movimento e l'identità.</p>
        </div>
      </div>
      <div class="treatment-card reveal">
        <img src="images/brown_hair.png" alt="Straight Brown Hair">
        <div class="treatment-card-overlay"></div>
        <div class="treatment-card-content">
          <div class="treatment-tag">Liscio Naturale</div>
          <h3 class="treatment-name">Straight Brown</h3>
          <p class="treatment-desc">Liscio perfetto e setoso che esalta la lunghezza e la naturale brillantezza del colore castano.</p>
        </div>
      </div>
      <div class="treatment-card reveal">
        <img src="images/curly_hair.png" alt="Long Curly Hair">
        <div class="treatment-card-overlay"></div>
        <div class="treatment-card-content">
          <div class="treatment-tag">Volume e Ricci</div>
          <h3 class="treatment-name">Curly Volume</h3>
          <p class="treatment-desc">Ricci definiti e corposi che incorniciano il volto e celebrano la tua texture naturale.</p>
        </div>
      </div>"""
content = content.replace(treatments_orig, treatments_new)

# 6. WebGL Shader background
shader_orig = """    vec3 gold=vec3(.78,.66,.43);
    vec3 col=gold*strand;
    gl_FragColor=vec4(col,.4*strand);"""

shader_new = """    vec3 pink=vec3(1.0, 0.71, 0.76); // Light pink
    vec3 col=pink*strand * 1.5;
    gl_FragColor=vec4(col,.6*strand);"""
content = content.replace(shader_orig, shader_new)

# 7. Form ID
content = content.replace('<form name="booking-longhairid"', '<form id="booking-form" name="booking-longhairid"')

# 8. JS Backend hook
js_backend = """
// Form submission mock backend
document.getElementById('booking-form')?.addEventListener('submit', async (e) => {
  e.preventDefault();
  const btn = e.target.querySelector('button[type="submit"]');
  const origText = btn.innerHTML;
  btn.innerHTML = 'Invio in corso...';
  
  const formData = new FormData(e.target);
  const data = Object.fromEntries(formData.entries());
  
  try {
    const response = await fetch('http://localhost:8000/api/prenotazione', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    });
    const result = await response.json();
    if(result.success) {
      alert(e.target.getAttribute('data-success-message') || "Prenotazione inviata con successo!");
      e.target.reset();
    } else {
      alert("Errore nell'invio della prenotazione.");
    }
  } catch (err) {
    console.error(err);
    alert("Impossibile contattare il server. Assicurati che il backend (server.py) sia in esecuzione sulla porta 8000.");
  } finally {
    btn.innerHTML = origText;
  }
});
"""
content = content.replace('// Parallax', js_backend + '\n// Parallax')

with open('jy5W-fQfL4.html', 'w', encoding='utf-8') as f:
    f.write(content)

