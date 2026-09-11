# README — Release #ChamaMaisATPS · Eleições 2026

Versão: **v4.6-release-20260911**
Preparado em: 11/09/2026
Publicação prevista: 13/09/2026

---

## Estrutura

```
release/
├── index.html                  # Landing + Nota de Esclarecimento
├── apoio-lula/
│   └── index.html              # Infográfico "Por que apoiamos Lula"
├── fundamentos/
│   └── index.html              # Dossiê de fundamentos e fontes
├── candidaturas/
│   └── index.html              # Painel legislativo v4.6 corrigido
├── assets/
│   └── styles.css              # Tokens de cor, tipografia e componentes compartilhados
├── README_RELEASE.md           # Este arquivo
├── CHANGELOG.md                # Registro de todas as alterações de conteúdo e estrutura
├── QA_REPORT_FINAL.md          # Relatório de QA pós-integração
└── SHA256SUMS.txt              # Checksums de integridade
```

---

## Pré-requisito antes do deploy: substituir {{BASE_URL}}

**Todos os quatro HTMLs contêm o marcador `{{BASE_URL}}`** nas metatags de SEO/OG e nos links canônicos.
Antes de publicar, substitua o marcador pelo domínio definitivo — por exemplo:

```bash
# Linux/macOS — substituição em todos os arquivos
find . -name "*.html" -exec sed -i 's|{{BASE_URL}}|https://seu-dominio.com|g' {} +
```

Se o domínio for `https://chamamais-atps-eleicoes-2026.lovable.app`, execute:

```bash
find . -name "*.html" -exec sed -i 's|{{BASE_URL}}|https://chamamais-atps-eleicoes-2026.lovable.app|g' {} +
```

O marcador aparece em **duas tags HTML** por página: `<link rel="canonical">` e `<meta property="og:url">`. Há também uma ocorrência em comentário HTML documental em cada arquivo (`<!-- SEO/OG: substituir {{BASE_URL}} antes do deploy -->`), que serve apenas como instrução para quem faz o deploy e não afeta o comportamento da página.
Links internos entre páginas são **relativos** e não precisam de ajuste.

---

## Hospedagem

O microsite é 100% estático — HTML, CSS e JavaScript nativos, sem backend, sem banco de dados,
sem autenticação.

Compatível com qualquer servidor de arquivos estáticos:

| Plataforma       | Instrução                                                  |
|------------------|------------------------------------------------------------|
| Vercel           | Aponte a pasta `release/` como raiz do projeto             |
| Netlify          | "Publish directory": `release`                             |
| Cloudflare Pages | "Build output directory": `release`                        |
| GitHub Pages     | Configure para servir a pasta `release/` (ou branch `gh-pages`) |
| Nginx/Apache     | Copie o conteúdo de `release/` para o `DocumentRoot`       |

### Rewrite / SPA fallback (não necessário)

As rotas usam diretórios com `index.html`. **Não é necessário rewrite de URL** — qualquer servidor
que sirva `index.html` de diretório funciona nativamente.

---

## Dependências externas

| Recurso | Origem | Motivo |
|---------|--------|--------|
| Poppins (webfont) | fonts.googleapis.com | Tipografia compartilhada via `@import` em `styles.css` |
| Poppins (pré-conexão) | fonts.gstatic.com | Cache de fonte (preconnect nos HTMLs filhos) |
| Links externos (TSE, Câmara, etc.) | Fontes primárias | Links de evidência nos cards do painel |

O site funciona sem conexão a `fonts.googleapis.com`, usando o fallback system-ui declarado em
`styles.css`. Todos os outros recursos são auto-contidos.

---

## Notas de conteúdo

- **Textos canônicos preservados**: o texto integral da Nota de Esclarecimento foi reproduzido
  a partir de `landing-source/src/routes/index.tsx` sem alterações.
- **Dataset do painel**: 69 candidaturas (62 Câmara, 6 Senado, 1 Deputado Distrital) em
  18 unidades da federação. **Não modificado.**
- **SEI 72042/2026 e SEI 18172/2026**: mantidos como no original do painel v4.6.
  Não substituídos por 88368/2025 / 21776/2025 — os dois conjuntos são objetos distintos,
  não verificados como versões concorrentes do mesmo documento.
- **Patches aplicados**: ver `CHANGELOG.md` para lista completa.

---

## Contato e responsabilidade

Comissão do Cadastro Reserva de ATPS do CPNU 1 · Movimento #ChamaMaisATPS
Deliberação: 09/09/2026 · Publicação: 13/09/2026
