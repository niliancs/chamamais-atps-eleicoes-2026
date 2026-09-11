# QA REPORT FINAL — Microsite #ChamaMaisATPS · Release 13/09/2026

**Data do QA pós-integração (v1):** 11/09/2026
**Data do QA de regressão (v2):** 11/09/2026
**Versão auditada:** v4.6-release-20260911-v2
**Auditor:** Claude (Cowork) — sessão de build automatizada

---

## VEREDITO FINAL — v4.6-release-20260911-v2

| Dimensão | Resultado |
|---|---|
| QA estrutural / navegação | ✅ PASS |
| QA acessibilidade | ✅ PASS |
| QA meta / SEO | ✅ PASS |
| QA links internos | ✅ PASS |
| QA segurança (noopener) | ✅ PASS |
| QA invariantes do painel | ✅ PASS |
| QA patches aplicados (v1) | ✅ PASS |
| QA patches não aplicados (por decisão) | ✅ PASS |
| **QA regressão pós-patch v2** | |
| → Nota: 6 seções, Seção 5 nova, seções 1–4 e 6 idênticas | ✅ PASS |
| → CSS/Poppins: @import em posição válida, sem duplicação | ✅ PASS |
| → Navegação: 12 pares, skip links, aria-current | ✅ PASS |
| → Acessibilidade: skip links nas 4 páginas | ✅ PASS |
| → Painel 69/62/6/1: dataset e DOM consistentes | ✅ PASS |
| → Busca/filtros: JavaScript preservado | ✅ PASS |
| → Links externos: 477 × noopener noreferrer | ✅ PASS |
| → SEO/metadados: canonical + og:url nas 4 rotas | ✅ PASS |
| → Responsividade: viewport meta + media queries | ✅ PASS |
| → Checksums: regenerados para 8 arquivos | ✅ PASS |

**READY FOR RELEASE 13/09:** ✅ SIM (com substituição de `{{BASE_URL}}` antes do deploy)

P0 abertos: **0**
P1 abertos: **0**
P2 abertos: **0**

### Patches v2 aplicados

| Patch | Arquivo | Resultado |
|---|---|---|
| Editorial: substituição da Seção 5 | `index.html` | ✅ PASS — 6 seções, título novo, 5 parágrafos aprovados, seções 1–4 e 6 intactas |
| Técnico: `@import` Poppins movido | `assets/styles.css` | ✅ PASS — posição válida, 1 importação, tokens preservados |
| Documental: contagem de tags BASE_URL | `README_RELEASE.md` | ✅ PASS — "duas tags HTML" por página documentado |

### Sem regressões conhecidas

Nenhum P0, P1 ou P2 introduzido pelo patch v2.

---

## QA FUNCIONAL — LANDING (`index.html`)

| Teste | Esperado | Encontrado | PASS/FAIL |
|---|---|---|---|
| lang="pt-BR" | presente | presente | ✅ PASS |
| charset UTF-8 | presente | presente | ✅ PASS |
| viewport meta | presente | presente | ✅ PASS |
| `<title>` | presente e descritivo | "Chama + ATPS — Posicionamento..." | ✅ PASS |
| meta description | presente | presente | ✅ PASS |
| og:title | presente | presente | ✅ PASS |
| og:url | presente | `{{BASE_URL}}/` | ✅ PASS (requer substituição) |
| canonical | presente | `{{BASE_URL}}/` | ✅ PASS (requer substituição) |
| skip link | presente | `<a class="skip-link" href="#conteudo">` | ✅ PASS |
| site-nav | presente | 3 links internos + home | ✅ PASS |
| aria-current="page" | na rota ativa | no link "Chama + ATPS" (home) | ✅ PASS |
| h1 único | 1 h1 | 1 | ✅ PASS |
| links internos | 3 rotas | ./apoio-lula/, ./fundamentos/, ./candidaturas/ | ✅ PASS |
| links externos Drive | 0 (removidos) | 0 | ✅ PASS |
| target=_blank | 0 (todos internos) | 0 | ✅ PASS |
| placeholders de conteúdo | 0 | 0 | ✅ PASS |
| {{BASE_URL}} | 3 ocorrências documentadas | 3 | ✅ PASS |
| Texto da Nota (parágrafo canônico) | íntegro | reproduzido verbatim | ✅ PASS |
| 6 seções numeradas da nota | presentes | presentes | ✅ PASS |
| Nota metodológica | presente | presente | ✅ PASS |
| styles.css referenciado | assets/styles.css | assets/styles.css | ✅ PASS |
| Poppins webfont | carregada | via @import em styles.css | ✅ PASS |

---

## QA FUNCIONAL — INFOGRÁFICO (`apoio-lula/index.html`)

| Teste | Esperado | Encontrado | PASS/FAIL |
|---|---|---|---|
| lang="pt-BR" | presente | presente | ✅ PASS |
| og:title / og:url / canonical | presentes | presentes com {{BASE_URL}} | ✅ PASS |
| skip-link | classe `skip-link` | presente | ✅ PASS |
| site-nav | presente | aria-current="page" em "Por que Lula" | ✅ PASS |
| Link para dossiê | ../fundamentos/ | ../fundamentos/ | ✅ PASS |
| Link para Drive removido | 0 links drive.google.com | 0 | ✅ PASS |
| P1-01: UUID label Lula (2 ocorrências) | "pacote ZIP (contém programa de Lula)" | corrigido | ✅ PASS |
| P1-01: UUID label Flávio (2 ocorrências) | "pacote ZIP (arquivo de Flávio: 2026BR...)" | corrigido | ✅ PASS |
| href do UUID | preservado sem alteração | `433ac1f4-07dc-44a2-bcbe-c87a2073721a` | ✅ PASS |
| target=_blank sem noopener | 0 | 0 | ✅ PASS |
| h1 único | 1 | 1 | ✅ PASS |
| styles.css referenciado | ../assets/styles.css | ../assets/styles.css | ✅ PASS |
| Conteúdo factual preservado | inalterado | inalterado | ✅ PASS |

---

## QA FUNCIONAL — DOSSIÊ (`fundamentos/index.html`)

| Teste | Esperado | Encontrado | PASS/FAIL |
|---|---|---|---|
| lang="pt-BR" | presente | presente | ✅ PASS |
| og:title / og:url / canonical | presentes | presentes com {{BASE_URL}} | ✅ PASS |
| skip-link | classe `skip-link` | presente | ✅ PASS |
| site-nav | presente | aria-current="page" em "Fundamentos" | ✅ PASS |
| Link para infográfico | ../apoio-lula/ | ../apoio-lula/ | ✅ PASS |
| P2-05: Arial removido | font-family:Arial ausente no início do CSS | removido | ✅ PASS |
| Poppins override preservado | presente no final do style | presente | ✅ PASS |
| P1-01: UUID labels Lula (4 ocorrências) | "pacote ZIP (contém programa de Lula)" | corrigidos | ✅ PASS |
| P1-01: UUID labels Flávio (3 ocorrências) | "pacote ZIP (arquivo de Flávio: ...)" | corrigidos | ✅ PASS |
| target=_blank sem noopener | 0 | 0 | ✅ PASS |
| h1 único | 1 | 1 | ✅ PASS |
| Conteúdo factual preservado | inalterado | inalterado | ✅ PASS |

---

## QA FUNCIONAL — PAINEL (`candidaturas/index.html`)

### Invariantes

| Invariante | Esperado | Encontrado | PASS/FAIL |
|---|---|---|---|
| Total candidaturas | 69 | 69 (presente em texto e em dados) | ✅ PASS |
| Câmara dos Deputados | 62 | 62 | ✅ PASS |
| Senado Federal | 6 | 6 | ✅ PASS |
| Deputado Distrital | 1 | 1 | ✅ PASS |
| UFs cobertas | 18 | 18 (texto corrigido confirma) | ✅ PASS |

### Estrutura e acessibilidade

| Teste | Esperado | Encontrado | PASS/FAIL |
|---|---|---|---|
| lang="pt-BR" | presente | presente | ✅ PASS |
| og:title / og:url / canonical | presentes | presentes com {{BASE_URL}} | ✅ PASS |
| P1-02: skip link | `<a class="skip-link" href="#conteudo">` | presente, primeiro elemento do body | ✅ PASS |
| P1-02: id="conteudo" no main | presente | `<main class="wrap" id="conteudo">` | ✅ PASS |
| site-nav | presente | aria-current="page" em "Candidaturas" | ✅ PASS |
| P2-04: texto UF | "18 unidades da federação — 17 estados + Distrito Federal" | presente | ✅ PASS |
| Texto antigo "17 estados e no DF" | removido | removido | ✅ PASS |
| target=_blank (477 links) | todos com noopener noreferrer | 477/477 ✅ | ✅ PASS |
| JavaScript (busca, filtros) | preservado | não alterado | ✅ PASS |
| h1 único | 1 | 1 | ✅ PASS |
| SEI 72042/2026 + 18172/2026 | preservados (P1-03 não aplicado) | preservados | ✅ PASS |
| console.error em código JS | 0 | 0 | ✅ PASS |
| styles.css referenciado | ../assets/styles.css | ../assets/styles.css | ✅ PASS |

---

## QA DE NAVEGAÇÃO CRUZADA

| Rota | Link para | PASS/FAIL |
|---|---|---|
| `/` → `/apoio-lula/` | `./apoio-lula/` | ✅ |
| `/` → `/fundamentos/` | `./fundamentos/` | ✅ |
| `/` → `/candidaturas/` | `./candidaturas/` | ✅ |
| `/apoio-lula/` → `/` | `../` | ✅ |
| `/apoio-lula/` → `/fundamentos/` | `../fundamentos/` | ✅ |
| `/apoio-lula/` → `/candidaturas/` | `../candidaturas/` | ✅ |
| `/fundamentos/` → `/` | `../` | ✅ |
| `/fundamentos/` → `/apoio-lula/` | `../apoio-lula/` | ✅ |
| `/fundamentos/` → `/candidaturas/` | `../candidaturas/` | ✅ |
| `/candidaturas/` → `/` | `../` | ✅ |
| `/candidaturas/` → `/apoio-lula/` | `../apoio-lula/` | ✅ |
| `/candidaturas/` → `/fundamentos/` | `../fundamentos/` | ✅ |

Todos os 12 pares de navegação interna estão corretos. ✅

---

## CHECKLIST FINAL

| Item | Status |
|---|---|
| Conteúdo factual da Nota preservado | ✅ FECHADO |
| Fontes e evidências do painel preservadas | ✅ FECHADO |
| Dataset 69/62/6/1 íntegro | ✅ FECHADO |
| TSE SQ_CANDIDATO preservados | ✅ FECHADO |
| Atos parlamentares preservados | ✅ FECHADO |
| SEI 72042/2026 + 18172/2026 preservados (P1-03: não substituídos) | ✅ FECHADO |
| P1-01: UUID labels corrigidos (infográfico + dossiê) | ✅ FECHADO |
| P1-02: Skip link no painel | ✅ FECHADO |
| P2-02: OG meta no infográfico | ✅ FECHADO |
| P2-03: OG meta no dossiê | ✅ FECHADO |
| P2-04: "18 unidades da federação" no painel | ✅ FECHADO |
| P2-05: Arial removido do dossiê | ✅ FECHADO |
| Drive links removidos da landing | ✅ FECHADO |
| Links internos relativos funcionais | ✅ FECHADO |
| skip-link em todas as páginas | ✅ FECHADO |
| site-nav em todas as páginas | ✅ FECHADO |
| aria-current="page" correto por rota | ✅ FECHADO |
| Poppins via webfont (styles.css) | ✅ FECHADO |
| lang="pt-BR" em todos os HTMLs | ✅ FECHADO |
| OG meta em todas as páginas | ✅ FECHADO |
| target=_blank com noopener noreferrer | ✅ FECHADO |
| Sem placeholders de conteúdo | ✅ FECHADO |
| {{BASE_URL}} documentado para substituição | ✅ FECHADO |
| SHA256SUMS.txt gerado | ✅ FECHADO |
| CHANGELOG.md completo | ✅ FECHADO |
| README_RELEASE.md com instrução de deploy | ✅ FECHADO |
| Mobile-first CSS preservado em todos os documentos | ✅ FECHADO |
| Zero console.error em código JS | ✅ FECHADO |

---

## PENDÊNCIA PÓS-RELEASE

| Item | Ação |
|---|---|
| `{{BASE_URL}}` nos 4 HTMLs | Substituir pelo domínio definitivo antes do deploy |
| Permissões Google Drive | Verificar e ajustar para Viewer/Leitor (se Drive ainda for referenciado em outros canais) |
| P1-03 SEI | Comprovação externa do objeto de cada cadeia documental (SEI 2025 vs. 2026) |

---

*QA pós-integração v1 executado em 11/09/2026. QA de regressão v2 executado em 11/09/2026. Nenhum P0 ou P1 aberto em nenhuma das versões.*
