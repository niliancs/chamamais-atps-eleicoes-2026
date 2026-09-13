from pathlib import Path
import re

p = Path('candidaturas/index.html')
s = p.read_text(encoding='utf-8')

if 'first-fold-refresh-20260913' in s:
    raise SystemExit('Ajuste já aplicado')

m = re.search(r'<aside class="consult-note">.*?</aside>', s, flags=re.S)
if not m:
    raise SystemExit('Bloco de consulta não encontrado')
consult = m.group(0)
s = s[:m.start()] + s[m.end():]

new_scope = '<aside class="scope-card scope-card--compact"><div class="scope-kicker">Painel documental</div><div class="scope-metrics"><div class="scope-metric"><span class="scope-number">69</span><span class="scope-label">candidaturas</span></div><div class="scope-metric"><span class="scope-number scope-number--secondary">18</span><span class="scope-label">UFs</span></div></div><p class="scope-breakdown">6 Senado · 62 Câmara · 1 distrital</p><p class="tiny">Consulte o cargo ou condição documentada, a disputa em 2026 e o que cada documento comprova.</p></aside>'
s, n = re.subn(r'<aside class="scope-card">.*?</aside>', new_scope, s, count=1, flags=re.S)
if n != 1:
    raise SystemExit(f'Card principal não substituído: {n}')

anchor = '<div class="intro-note"><p><b>A pauta:'
if anchor not in s:
    raise SystemExit('Âncora da seção Panorama não encontrada')
s = s.replace(anchor, consult + anchor, 1)

css = '''
/* first-fold-refresh-20260913 */
.mast .wrap{padding-top:13px;padding-bottom:13px}
.hero{padding:38px 0 30px}
.hero-inner{grid-template-columns:minmax(0,1.7fr) minmax(280px,.82fr);gap:34px;align-items:stretch}
.hero h1{margin:12px 0 16px;max-width:720px}
.lead{max-width:700px}
.scope-card--compact{display:flex;flex-direction:column;justify-content:center;border:1px solid #a6ced0;background:rgba(255,255,255,.9);padding:24px 26px;border-radius:18px;box-shadow:0 12px 30px rgba(23,56,75,.06)}
.scope-kicker{text-transform:uppercase;font-size:10px;font-weight:800;letter-spacing:.13em;color:var(--muted);margin-bottom:14px}
.scope-metrics{display:grid;grid-template-columns:1.25fr 1fr;gap:12px;align-items:end}
.scope-metric{min-width:0}
.scope-number{font-size:54px!important;line-height:.95!important;font-weight:850;letter-spacing:-.055em;display:block;color:var(--green)!important;float:none!important;margin:0!important}
.scope-number--secondary{font-size:42px!important;color:var(--blue)!important}
.scope-label{display:block;margin-top:5px;font-size:12px;font-weight:750;color:var(--ink)}
.scope-breakdown{margin:16px 0 0!important;padding-top:13px;border-top:1px solid #d7e4e3;font-size:12px!important;font-weight:700;color:var(--muted)}
.scope-card--compact .tiny{margin-top:8px!important;padding:0!important;clear:none!important}
.overview>.consult-note{margin:18px 0 20px;padding:14px 17px;background:#fff;border:1px solid var(--line);border-left:4px solid var(--yellow);border-radius:10px;display:grid;grid-template-columns:minmax(210px,.55fr) minmax(0,1.45fr);gap:8px 20px;align-items:start}
.overview>.consult-note strong{grid-column:1;font-size:12px;line-height:1.4}
.overview>.consult-note>p{grid-column:2;margin:0;font-size:12px;line-height:1.55}
.overview>.consult-note .consult-meta{grid-column:2;color:var(--muted);font-size:11px}
@media(max-width:900px){.hero-inner{grid-template-columns:1.45fr .9fr;gap:24px}.scope-card--compact{padding:20px}.scope-number{font-size:48px!important}.scope-number--secondary{font-size:38px!important}.overview>.consult-note{grid-template-columns:1fr}.overview>.consult-note strong,.overview>.consult-note>p,.overview>.consult-note .consult-meta{grid-column:1}}
@media(max-width:650px){.hero{padding:28px 0 24px}.hero-inner{grid-template-columns:1fr;gap:18px}.scope-card--compact{padding:18px 20px}.scope-metrics{grid-template-columns:1fr 1fr}.scope-number{font-size:46px!important}.scope-number--secondary{font-size:38px!important}.overview>.consult-note{margin-top:14px}}
'''
s = s.replace('</style>', css + '</style>', 1)

checks = [
    'first-fold-refresh-20260913',
    'scope-card scope-card--compact',
    'scope-metrics',
    'Painel documental',
    '69</span><span class="scope-label">candidaturas',
    '18</span><span class="scope-label">UFs',
    '<aside class="consult-note">',
    '<section class="overview" id="panorama">'
]
missing = [x for x in checks if x not in s]
if missing:
    raise SystemExit('QA falhou: ' + repr(missing))
hero_end = s.index('</section>', s.index('<section class="hero">'))
consult_pos = s.index('<aside class="consult-note">')
if consult_pos < hero_end:
    raise SystemExit('Consulta ainda está dentro do hero')

p.write_text(s, encoding='utf-8')
print('Patch e QA OK')
