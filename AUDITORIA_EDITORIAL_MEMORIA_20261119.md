# Revisão editorial | Memória da atuação política do Chama + ATPS em 2026

**Data da revisão de enquadramento:** 19/11/2026  
**Status:** proposta para revisão, sem alteração de produção  
**Escopo:** microsite eleitoral em quatro HTMLs; conteúdo, contexto histórico, SEO e rótulos de navegação.

## Decisão editorial
Preservar o microsite como **acervo histórico da participação política da Comissão do Cadastro Reserva de ATPS em 2026**, não como campanha eleitoral corrente nem recomendação de voto. Registrar o que foi defendido no período, com sujeito político, data, documentos, resultados e limites de representação claros.

A posição eleitoral registrada é da Comissão no contexto do movimento, não do MGI, da ANDEPS, de toda a carreira nem de todas as pessoas no CR.

## Alterações propostas

| Página | Antes | Agora |
|---|---|---|
| / | Home com chamadas em presente no segundo turno | Arquivo histórico de 2026; caminhos para posicionamento, debates, resultados parlamentares e o resultado oficial presidencial |
| /apoio-lula/ | Texto abre como peça de apoio em andamento | Mantém o dossiê original com aviso de documento de época e comparação situada em outubro |
| /fundamentos/ | Apresenta proposições como questão eleitoral atual | Dossiê histórico com fonte, recorte e ressalvas: propostas não são medidas executadas |
| /candidaturas/ | Mostra 47 eleitos sem enquadramento temporal suficiente | Mostra 47 dos 69 nomes pesquisados, conforme conferência de 06/10, com link ao TSE e limite sobre atualidade dos resultados |

## Linha temporal da documentação
- 09/09/2026: deliberação da Comissão quanto ao posicionamento político.
- 11–12/09/2026: consulta interna voluntária; 117 de 123 participantes (95,1%) favoráveis à manifestação pública de apoio à candidatura presidencial, conforme o dossiê do movimento; não é censitária.
- 10/09/2026: corte do levantamento de candidaturas, atuação e referências documentais.
- 04/10/2026: primeiro turno das eleições.
- 06/10/2026: conferência dos resultados dos parlamentares no levantamento (47 eleitos, 45 Câmara e 2 Senado).
- 25/10/2026: segundo turno presidencial; resultado oficial: Lula reeleito, 51,79% dos votos válidos, Flávio Bolsonaro 48,21%.
- 19/11/2026: revisão **apenas do enquadramento histórico**, sem retotalizar a pesquisa ou revisar todas as fichas e fontes.

## Preservação técnica
- Zero alterações em `assets/`, estilos, fontes, logos, SVGs, cores ou imagens.
- Trechos `<style>`, `<script>`, dados JSON e filtros são idênticos aos da branch `main`.
- Nenhum link âncora interno existente foi quebrado; mantidos os `href` e `id` de navegação e dos módulos.
- Não foram recalculados os resultados do painel, nem modificadas as evidências originais.
- Os metadados e as primeiras telas foram atualizados para evitar que buscadores e visitantes leiam o arquivo como campanha ativa.

## Fontes principais
- Resultado presidencial oficial, TSE:
  https://www.tse.jus.br/comunicacao/noticias/2026/Outubro/presidente-do-tse-anuncia-reeleicao-de-lula-e-faz-balanco-do-2o-turno-das-eleicoes-2026
- Resultados oficiais gerais:
  https://www.tse.jus.br/eleicoes/eleicoes-2026-content/divulgacao-dos-resultados-das-eleicoes-2026
- Dataset original do microsite: `assets/resultados-20261006.json`
- QA original: `QA_REFRESH_20261006.md`
- Registro interno da deliberação: dossiê do movimento no Drive, com recorte 10/09 e consulta 11–12/09.

## Pendências antes de publicar
1. Revisar visualmente a apresentação nas larguras 320/390/768/1440 sem alterar a identidade.
2. Verificar a prévia do Vercel e os quatro caminhos reais com teclado, sem script e com filtros de candidaturas.
3. Confirmar os links externos ainda funcionais e, se algum recurso histórico estiver indisponível, acrescentar a indicação de arquivo em vez de substituir silenciosamente a fonte.
4. A Comissão deve validar o texto de delimitação do sujeito político e o contexto dado à consulta de setembro.
5. Fazer merge apenas após o QA e autorização editorial; não apagar o registro histórico de 06/10.
