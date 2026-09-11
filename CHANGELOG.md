# CHANGELOG — Microsite #ChamaMaisATPS · Eleições 2026

Formato: `[TIPO] Arquivo afetado — descrição`

Tipos: `ESTRUTURA` | `CONTEÚDO` | `PATCH` | `META` | `ACESSIBILIDADE`

---

## v4.6-release-20260911 — 11/09/2026

### Consolidação em microsite estático

#### ESTRUTURA — Arquitetura

- **[ESTRUTURA]** `release/` — criação da pasta de release com quatro rotas estáticas:
  `/` (landing), `/apoio-lula/`, `/fundamentos/`, `/candidaturas/`.
- **[ESTRUTURA]** `release/assets/styles.css` — criação do sistema visual compartilhado:
  tokens de cor (`--cm-navy`, `--cm-blue`, `--cm-turq`, `--cm-cyan`, `--cm-paper`,
  `--cm-yellow`, `--cm-red`, `--cm-green`, `--cm-muted`, `--cm-line`, `--cm-card`),
  tipografia Poppins via Google Fonts, componente `.site-nav`, padrão `.skip-link`,
  utilitários `.wrap`, `.eyebrow`, `.sr-only`.

#### ESTRUTURA — Landing (`index.html`)

- **[ESTRUTURA]** `release/index.html` — criação da landing estática a partir do conteúdo
  canônico de `landing-source/src/routes/index.tsx`. Texto da Nota de Esclarecimento
  reproduzido na íntegra, sem alterações.
- **[ESTRUTURA]** Links dos três documentos substituídos: de URLs do Google Drive
  (`drive.google.com/file/d/...`) pelas rotas internas `./apoio-lula/`, `./fundamentos/`,
  `./candidaturas/`.
- **[ESTRUTURA]** Texto de introdução da seção de documentos atualizado: de
  "abrem em nova aba no Google Drive" para "estão disponíveis como páginas desta publicação"
  (adequação à mudança de destino dos links).
- **[META]** `<title>`, `<meta name="description">`, OG tags e canonical adicionados
  com marcador `{{BASE_URL}}` para substituição antes do deploy.
- **[ACESSIBILIDADE]** Skip link `.skip-link` adicionado como primeiro elemento do `<body>`.
- **[ESTRUTURA]** Componente `<nav class="site-nav">` adicionado com links para as
  quatro seções. `aria-current="page"` na rota ativa.

#### PATCH — Infográfico (`apoio-lula/index.html`)

- **[PATCH · P1-01]** Quatro links com UUID `433ac1f4-07dc-44a2-bcbe-c87a2073721a`:
  labels corrigidos para indicar que o recurso é o pacote ZIP com todos os planos
  presidenciais, e não um arquivo por candidato.
  - "Programa de governo de Lula apresentado ao TSE" →
    "Planos de governo presidenciais no TSE Dados Abertos — pacote ZIP (contém programa de Lula)"
  - "Programa de governo de Flávio Bolsonaro apresentado ao TSE" →
    "Planos de governo presidenciais no TSE Dados Abertos — pacote ZIP (arquivo de Flávio: 2026BR280002551544_01.pdf)"
  - `href` preservado sem alteração.
- **[PATCH · P2-02]** OG meta (`og:title`, `og:description`, `og:type`, `og:url`) e
  `<link rel="canonical">` adicionados ao `<head>`.
- **[ACESSIBILIDADE · P1-02-prep]** Classe do skip link existente: `skip` → `skip-link`
  (usa estilo compartilhado com foco amarelo).
- **[ESTRUTURA]** Link interno `href="dossie-fundamentos-apoio-lula-2026.html"` →
  `href="../fundamentos/"`.
- **[ESTRUTURA]** Componente `<nav class="site-nav">` injetado após skip link.
- **[META]** `<link rel="stylesheet" href="../assets/styles.css">` adicionado ao `<head>`.

#### PATCH — Dossiê (`fundamentos/index.html`)

- **[PATCH · P1-01]** Sete links com UUID `433ac1f4-07dc-44a2-bcbe-c87a2073721a`:
  mesmo patch de label aplicado (4 referências a Lula, 3 a Flávio Bolsonaro).
- **[PATCH · P2-03]** OG meta e `<link rel="canonical">` adicionados ao `<head>`.
- **[PATCH · P2-05]** `body{font-family:Arial,Helvetica,sans-serif;...}` → `body{...}`
  (declaração de Arial removida da base; o override Poppins já presente no final do
  `<style>` permanece como fonte efetiva).
- **[ACESSIBILIDADE]** Classe do skip link: `skip` → `skip-link`.
- **[ESTRUTURA]** Link interno `href="infografico-apoio-lula-2026.html"` →
  `href="../apoio-lula/"`.
- **[ESTRUTURA]** Componente `<nav class="site-nav">` injetado após skip link.
- **[META]** `<link rel="stylesheet" href="../assets/styles.css">` adicionado ao `<head>`.

#### PATCH — Painel (`candidaturas/index.html`)

- **[ACESSIBILIDADE · P1-02]** Skip link adicionado: `<a class="skip-link" href="#conteudo">
  Ir para o conteúdo</a>` como primeiro elemento de `<body>`.
- **[ACESSIBILIDADE · P1-02]** `id="conteudo"` adicionado ao `<main class="wrap">` como
  destino do skip link.
- **[PATCH · P2-04]** "69 candidaturas em 17 estados e no DF" →
  "69 candidaturas em 18 unidades da federação — 17 estados + Distrito Federal".
- **[PATCH · P2-02]** OG meta e `<link rel="canonical">` adicionados ao `<head>`.
- **[ESTRUTURA]** Componente `<nav class="site-nav">` injetado após skip link,
  antes do `<header class="mast">` original.
- **[META]** `<link rel="stylesheet" href="../assets/styles.css">` adicionado ao `<head>`.
- **Preservado sem alteração**: dataset de 69 candidaturas, todos os IDs, totais por
  cargo/UF/partido, referências de evidência, todo o JavaScript (busca, filtros, expansão),
  SEI 72042/2026 e SEI 18172/2026 (conforme decisão: preservar separadamente).

---

## v4.6-release-20260911-v2 — 11/09/2026 (patch pré-deploy)

### Patch editorial

- **[CONTEÚDO · Seção 5]** `release/index.html` — substituição integral e aprovada da Seção 5
  da Nota de Esclarecimento:
  - Título anterior: "Limites do apoio"
  - Título novo: "Limites do apoio e autonomia da pauta institucional"
  - Conteúdo anterior (3 parágrafos): versão sintética sobre garantias, expectativas e negociação.
  - Conteúdo novo (5 parágrafos): versão aprovada que contextualiza a origem do posicionamento
    eleitoral, nega promessas/negociações, reafirma que apoio não é garantia de nomeação,
    preserva o trecho sobre expectativas do cadastro, e declara autonomia da pauta institucional
    de provimento independentemente do calendário eleitoral.
  - Seções 1, 2, 3, 4 e 6 preservadas integralmente sem alteração.
  - Sujeito político mantido: Comissão do Cadastro Reserva de ATPS do CPNU 1.
  - Nenhuma ampliação para todo o cadastro reserva, toda a carreira de ATPS, Andeps ou MGI.

### Patch técnico

- **[META · CSS]** `release/assets/styles.css` — `@import` da Poppins movido para posição
  válida: imediatamente após o bloco de comentário de cabeçalho, antes de todas as regras CSS
  aplicáveis (`*, *::before, *::after`, `:root`, etc.).
  Motivação: a especificação CSS exige que `@import` preceda todas as regras exceto `@charset`
  e `@layer`; a posição anterior (após `:root {}`) era tecnicamente inválida e poderia fazer
  navegadores ignorarem a importação da fonte.
  Família, pesos (400;500;600;700;800) e URL preservados sem alteração.
  Nenhuma importação duplicada introduzida.

### Patch documental

- **[META · README]** `release/README_RELEASE.md` — correção da afirmação incorreta sobre
  o número de tags HTML com `{{BASE_URL}}`:
  - Texto anterior: "O marcador aparece em quatro tags por página: `<link rel="canonical">`, `og:url`."
  - Texto novo: "O marcador aparece em **duas tags HTML** por página: `<link rel="canonical">` e
    `<meta property="og:url">`. Há também uma ocorrência em comentário HTML documental em cada
    arquivo, que serve apenas como instrução de deploy e não afeta o comportamento da página."
  - Nenhum HTML alterado por causa desta correção documental.

### QA de regressão

- **[QA]** Executado QA de regressão completo pós-patch:
  - Nota: 6 seções, Seção 5 nova, seções 1–4 e 6 idênticas ao release anterior. PASS.
  - CSS/Poppins: `@import` em posição válida, sem duplicação, tokens preservados. PASS.
  - Navegação: 12 pares de navegação interna, skip links, aria-current. PASS.
  - Painel: 69 candidatos (62 Câmara / 6 Senado / 1 Distrital), 18 UFs, JS preservado. PASS.
  - Links externos: 477 `target="_blank"` com `noopener noreferrer`. PASS.
  - SEO/OG: canonical + og:url presentes nas 4 rotas; `{{BASE_URL}}` intacto. PASS.
  - Nenhuma regressão conhecida.

---

## Patches NÃO aplicados (por decisão explícita)

- **P1-03 — SEI**: SEI 72042/2026 + 18172/2026 e SEI 88368/2025 + 21776/2025 preservados
  como estão. Os dois conjuntos pertencem a cadeias documentais distintas; substituição
  automática não autorizada sem comprovação do objeto de cada cadeia.
- **Remoção de candidatos**: nenhuma alteração no recorte de candidaturas.
- **Redesenho de identidade visual**: painel mantém CSS original (usa tokens `--blue`,
  `--turq` próprios, não `--cm-*`); harmonização aplicada somente via nav compartilhada.
