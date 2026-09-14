from pathlib import Path

path = Path("candidaturas/index.html")
html = path.read_text(encoding="utf-8")
marker = "criteria-refresh-20260914"

if marker in html:
    print("Atualização de critérios já aplicada.")
    raise SystemExit(0)

css_anchor = "</style>  <!-- SEO/OG: URL canônica de produção -->"
css = r'''
/* criteria-refresh-20260914 */
.scope-number::before,.scope-number::after{content:none!important}
.selection-criteria{margin:30px 0 34px;padding:28px 30px;background:#fff;border:1px solid var(--line);border-top:4px solid var(--green);border-radius:14px;scroll-margin-top:80px}
.selection-criteria .overline{margin-bottom:7px}.selection-criteria h2{font-size:28px;line-height:1.2;letter-spacing:-.025em;margin:0 0 10px}.selection-criteria>.criteria-lead{font-size:14px;line-height:1.75;max-width:920px;margin:0 0 20px;color:var(--muted)}
.selection-criteria-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px}.selection-criterion{background:#f5f9f7;border:1px solid #dde9e5;border-radius:10px;padding:16px 17px}.selection-criterion h3{font-size:14px;margin:0 0 7px}.selection-criterion p,.selection-criterion li{font-size:12px;line-height:1.65;margin-top:0}.selection-criterion ul{margin:7px 0 0;padding-left:18px}.selection-criterion--wide{grid-column:1/-1}
.selection-caveat{margin-top:16px;padding:16px 18px;background:#fff8e5;border-left:4px solid var(--yellow);border-radius:8px}.selection-caveat strong{display:block;font-size:13px;margin-bottom:5px}.selection-caveat p{font-size:12px;line-height:1.65;margin:5px 0}.why-here{margin:12px 0 4px;padding:10px 12px;background:#eef6f3;border-left:3px solid var(--green);border-radius:6px}.why-here .why-label{display:block;font-size:9px;font-weight:800;letter-spacing:.07em;text-transform:uppercase;color:var(--muted);margin-bottom:4px}.why-here strong{font-size:11px;line-height:1.45;color:var(--ink)}
@media(max-width:650px){.selection-criteria{padding:20px}.selection-criteria-grid{grid-template-columns:1fr}.selection-criterion--wide{grid-column:auto}.selection-criteria h2{font-size:24px}}
'''
if css_anchor not in html:
    raise RuntimeError("Âncora de CSS não encontrada")
html = html.replace(css_anchor, css + "\n" + css_anchor, 1)

old_nav = '<nav aria-label="Navegação" class="topnav"><div class="wrap"><a href="#panorama">Panorama</a><a data-jump="" href="#senado">Senado</a><a data-jump="" href="#camara">Câmara</a><a href="#vinculo-atps">ATPS de carreira</a><a href="#historico">Outros nomes</a><a href="#criterios">Como consultar</a><button id="print">Imprimir</button></div></nav>'
new_nav = '<nav aria-label="Navegação" class="topnav"><div class="wrap"><a href="#panorama">Panorama</a><a href="#criterios">Critérios</a><a data-jump="" href="#senado">Senado</a><a data-jump="" href="#camara">Câmara</a><a href="#vinculo-atps">ATPS de carreira</a><a href="#historico">Outros nomes</a><a href="#metodologia">Metodologia</a><button id="print">Imprimir</button></div></nav>'
if old_nav not in html:
    raise RuntimeError("Navegação esperada não encontrada")
html = html.replace(old_nav, new_nav, 1)

criteria_anchor = '<h2>Consulte por estado</h2>'
criteria_block = r'''
<section class="selection-criteria" id="criterios" aria-labelledby="criterios-titulo">
  <div class="overline">Critérios públicos e verificáveis</div>
  <h2 id="criterios-titulo">Como selecionamos as candidaturas</h2>
  <p class="criteria-lead">Esta não é uma lista automática de partidos nem uma relação de todas as candidaturas do país. O levantamento combina um recorte político assumido com evidências documentais sobre a atuação de cada nome.</p>
  <div class="selection-criteria-grid">
    <article class="selection-criterion"><h3>1. Recorte político</h3><p><strong>Pertencimento ao campo democrático e progressista</strong>, coerente com a defesa das políticas sociais, do serviço público e da capacidade do Estado de executar políticas públicas.</p></article>
    <article class="selection-criterion"><h3>2. Atuação ou vínculo documentado</h3><p>Buscamos evidências verificáveis de pelo menos uma destas relações:</p><ul><li>atuação direta em defesa dos ATPS, do cadastro de reserva ou do CPNU;</li><li>atos formais relacionados à carreira, concursos ou serviço público;</li><li>trajetória documentada em políticas sociais, direitos e fortalecimento da capacidade estatal.</li></ul></article>
    <article class="selection-criterion"><h3>3. Evidência individual, não apenas partidária</h3><p>O partido ajuda a definir o recorte político, mas <strong>não transfere automaticamente apoio ou confiança para cada candidatura</strong>. Sempre que possível, avaliamos atos, trajetória e posicionamentos individuais.</p></article>
    <article class="selection-criterion"><h3>4. Situação eleitoral conferida</h3><p>Nome, partido, cargo em disputa, número, UF e situação da candidatura são confrontados com os dados eleitorais disponíveis no <strong>TSE</strong>.</p></article>
    <article class="selection-criterion selection-criterion--wide"><h3>5. Escopo definido</h3><p>O foco principal é <strong>Câmara dos Deputados e Senado Federal</strong>. Raphael Sebba é a exceção distrital por seu vínculo direto com a carreira de ATPS. Outros registros relevantes permanecem documentados fora da seleção principal.</p></article>
  </div>
  <aside class="selection-caveat"><strong>O que esta seleção significa — e o que não significa</strong><p>Estar no painel significa que encontramos elementos que justificam a inclusão segundo esses critérios. <strong>Não significa apoio eleitoral automático da Comissão.</strong> Quando houver apoio expresso a uma candidatura, isso deve aparecer identificado como tal.</p><p>Da mesma forma, <strong>a ausência de um nome não significa oposição às nossas pautas</strong>: pode significar que ele está fora do recorte adotado ou que não localizamos evidência suficiente até o corte da pesquisa.</p></aside>
</section>
'''
if criteria_anchor not in html:
    raise RuntimeError("Ponto de inserção dos critérios não encontrado")
html = html.replace(criteria_anchor, criteria_block + criteria_anchor, 1)

old_method = '<section class="criteria" id="criterios"><h2>Como consultar este painel</h2>'
new_method = '<section class="criteria" id="metodologia"><h2>Metodologia e como consultar este painel</h2>'
if old_method not in html:
    raise RuntimeError("Seção metodológica esperada não encontrada")
html = html.replace(old_method, new_method, 1)

script_anchor = "</body>"
script = r'''
<script>
/* criteria-refresh-20260914: motivo de inclusão derivado apenas dos registros já exibidos na própria ficha */
(function(){
  function motivo(card){
    var role=((card.querySelector('.current-role strong')||{}).textContent||'').trim();
    var badge=((card.querySelector('.relation .badge')||{}).textContent||'').trim();
    var tags=Array.from(card.querySelectorAll('.tags span')).map(function(el){return el.textContent.trim();});
    if (/Analista Técnico de Políticas Sociais|Integrante da carreira de ATPS/i.test(role+' '+badge)) return 'ATPS de carreira';
    if (tags.indexOf('Apoio ao cadastro de reserva')>=0) return 'Apoio documentado ao cadastro de reserva';
    if (/ATPS|carreira de ATPS/i.test(badge) || tags.indexOf('Atos sobre ATPS')>=0) return 'Ato formal sobre ATPS';
    if (tags.indexOf('Serviço público')>=0 || tags.indexOf('CNU e outros cadastros')>=0) return 'Atuação documentada sobre concursos e serviço público';
    return 'Trajetória documentada em políticas públicas, políticas sociais e direitos';
  }
  document.querySelectorAll('article.candidate').forEach(function(card){
    if(card.querySelector('.why-here')) return;
    var target=card.querySelector('.relation');
    if(!target) return;
    var box=document.createElement('div');
    box.className='why-here';
    var label=document.createElement('span'); label.className='why-label'; label.textContent='Por que este nome está aqui?';
    var strong=document.createElement('strong'); strong.textContent=motivo(card);
    box.appendChild(label); box.appendChild(strong);
    target.parentNode.insertBefore(box,target);
  });
})();
</script>
'''
if script_anchor not in html:
    raise RuntimeError("Fechamento do body não encontrado")
html = html.replace(script_anchor, script + script_anchor, 1)

path.write_text(html, encoding="utf-8")
print("Critérios, navegação, metodologia e motivos de inclusão atualizados.")
