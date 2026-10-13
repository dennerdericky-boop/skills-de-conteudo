---
name: pauta
description: "Monta a pauta do dia: busca notícias em tempo real de mercado financeiro, economia, política, geopolítica e negócios e sugere o que postar. Use com /pauta."
---

# /pauta — O que postar hoje (Brasil + mundo, incluindo os 27 países da UE)

Objetivo: transformar as notícias e os dados de mercado **em tempo real** de Brasil e do mundo em ideias de posts.

## 0. Regra principal: sempre em tempo real
- Toda execução busca dados novos. Nunca responda de memória nem reaproveite pauta antiga.
- Pegue a data e a hora atuais com a ferramenta de horário antes de buscar.
- Mostre o horário da coleta (Brasília) e indique se cada bolsa está **aberta, fechada ou em pré-mercado**.

## 1. Fontes (sempre consultar)

### Conectores
Bigdata.com (`bigdata_market_tearsheet`, `bigdata_country_tearsheet`, `bigdata_events_calendar`, `bigdata_search`, `bigdata_company_tearsheet`) e outros conectores financeiros, se houver. Se o Bigdata.com não estiver conectado, avise e siga com as demais fontes.

### Sites de mercado fixos
Consulte sempre, com WebFetch (e WebSearch restrito ao domínio, via `allowed_domains`, quando a página não carregar direto):
- **TradingView** (br.tradingview.com): cotações e gráficos em tempo real, análise técnica, maiores altas e baixas, ideias e notícias da comunidade
- **Investing.com** (br.investing.com): cotações ao vivo de ações, moedas, commodities e índices globais; calendário econômico; notícias de mercado
- **Status Invest** (statusinvest.com.br): fundamentos de empresas da B3 — dividendos, P/L, balanços, histórico
- **Investidor10** (investidor10.com.br): fundamentos, dividendos, indicadores e comparativos de ações e FIIs da B3
- **B3** (b3.com.br): dados oficiais de cotações e índices — as cotações públicas gratuitas podem ter **atraso de cerca de 15 minutos**; sinalize isso quando usar

Como usar cada um:
- Cotações e movimento do dia: Investing.com e TradingView; confirme fechamentos oficiais da bolsa brasileira na B3
- Empresas da B3 em destaque (balanço, dividendos, P/L): Status Invest e Investidor10
- Agenda da semana: calendário econômico do Investing.com + `bigdata_events_calendar`
- Se duas fontes divergirem, mostre a fonte e o horário de cada número

### Veículos de notícias fixos
Consulte sempre, buscando por veículo (WebSearch com `allowed_domains`) e lendo as matérias com WebFetch:
- **Valor Econômico** (valor.globo.com): negócios, finanças e política econômica com análise aprofundada — referência principal para Brasil
- **InfoMoney** (infomoney.com.br): mercado em tempo real, B3, análises de investimento e impacto da política nos ativos
- **Forbes Brasil** (forbes.com.br): empreendedorismo, grandes negócios, economia global, líderes e empresas
- **InvestNews** (investnews.com.br): economia e investimentos em linguagem simples — bom termômetro do que interessa ao público geral
- **Bloomberg** (bloomberg.com e Bloomberg Línea) e **Wall Street Journal** (wsj.com): cenário macro internacional, câmbio e bolsas globais

Também: Reuters, Estadão, Folha e veículos locais dos países cobertos quando necessário.
Valor, Bloomberg e WSJ têm paywall: use títulos, resumos e trechos abertos, confirme o fato em outra fonte aberta e nunca tente contornar o paywall.

### Fontes oficiais (dados brutos do Brasil)
- **Banco Central do Brasil** (bcb.gov.br): Selic, atas e comunicados do Copom, Focus, câmbio, crédito
- **IBGE** (ibge.gov.br): IPCA, PIB, desemprego (PNAD), produção, varejo
- **IPEA** (ipea.gov.br e ipeadata.gov.br): séries históricas e estudos econômicos

Números oficiais do Brasil vêm daqui; os veículos servem para contexto e repercussão. No exterior, use os equivalentes (Fed, BCE, Eurostat, BLS, institutos nacionais de estatística).

### Quando uma fonte falhar
Se algum site recusar o acesso ou não renderizar (páginas muito dinâmicas ou com paywall), diga qual falhou e use as outras fontes; nunca tente contornar o bloqueio. Se o navegador do app estiver disponível e o usuário quiser, ele pode ser usado para ler essas páginas.

## 2. Países cobertos
Se o usuário indicar outra lista ou um foco, siga o pedido.

### Prioridade máxima
🇧🇷 Brasil

### Principais
🇺🇸 EUA · 🇨🇦 Canadá · 🇦🇺 Austrália · 🇪🇺 União Europeia (bloco + 27 países, abaixo)

### 🇪🇺 União Europeia — 27 países-membros
**Nível do bloco (sempre):** BCE, euro, Euro Stoxx 50, Comissão Europeia, Parlamento Europeu, política comercial e tarifas da UE.

**Destaque sempre (maiores economias):** 🇩🇪 Alemanha (DAX) · 🇫🇷 França (CAC 40) · 🇮🇹 Itália (FTSE MIB) · 🇪🇸 Espanha (IBEX 35) · 🇳🇱 Países Baixos (AEX)

**Monitorar todos e destacar quando houver notícia relevante:**
🇦🇹 Áustria · 🇧🇪 Bélgica · 🇧🇬 Bulgária · 🇨🇿 Chéquia · 🇨🇾 Chipre · 🇭🇷 Croácia · 🇩🇰 Dinamarca · 🇸🇰 Eslováquia · 🇸🇮 Eslovénia · 🇪🇪 Estónia · 🇫🇮 Finlândia · 🇬🇷 Grécia · 🇭🇺 Hungria · 🇮🇪 Irlanda · 🇱🇻 Letónia · 🇱🇹 Lituânia · 🇱🇺 Luxemburgo · 🇲🇹 Malta · 🇵🇱 Polónia · 🇵🇹 Portugal · 🇷🇴 Roménia · 🇸🇪 Suécia

**Países da UE fora do euro (acompanhar moeda e banco central próprios):** Chéquia (coroa checa, CNB), Dinamarca (coroa dinamarquesa, Danmarks Nationalbank), Hungria (florim, MNB), Polónia (zloty, NBP), Roménia (leu, BNR), Suécia (coroa sueca, Riksbank). Confirme na busca se houve mudança recente na adesão ao euro.

### Demais países (monitorar e destacar quando houver notícia relevante)
🇬🇧 Reino Unido · 🇨🇭 Suíça · 🇨🇳 China · 🇯🇵 Japão · 🇮🇳 Índia · 🇰🇷 Coreia do Sul · 🇲🇽 México · 🇦🇷 Argentina · 🇨🇱 Chile · 🇨🇴 Colômbia · 🇿🇦 África do Sul · 🇸🇦 Arábia Saudita · 🇹🇷 Turquia · 🇷🇺 Rússia · 🇮🇩 Indonésia

## 3. Coleta (buscas separadas, agrupadas por região)
Para cada país, levante o que for relevante nas últimas 24 h:
- **Mercado:** principal índice, moeda contra o dólar e o real, juros de 10 anos
- **Banco central:** decisões, atas e falas
- **Economia:** inflação, emprego, PIB, fiscal
- **Política e geopolítica:** governo, eleições, conflitos, sanções, tarifas
- **Negócios:** balanços, fusões e aquisições, IPOs, empresas em destaque

**Brasil em detalhe:** Ibovespa, dólar, DI/juros futuros, maiores altas e baixas da B3 do dia, dados oficiais do BCB/IBGE/IPEA divulgados no dia, manchetes de Valor, InfoMoney, InvestNews e Forbes Brasil, e para as empresas em destaque os fundamentos no Status Invest/Investidor10.

Para os 22 países menores da UE, faça buscas agrupadas (ex.: "Europa Central e Leste", "Nórdicos e Bálticos", "Benelux", "Sul da Europa") e aprofunde só onde houver fato relevante.

Ativos globais: petróleo (Brent/WTI), gás natural europeu (TTF), ouro, minério de ferro, soja/milho, bitcoin e ethereum.

Confirme números em pelo menos uma fonte e registre o horário de cada cotação.

## 4. Seleção
Pontue cada notícia de 1 a 5 em: relevância para o público brasileiro, impacto no bolso/investimentos, potencial de engajamento, urgência e facilidade de explicar. Notícias internacionais ganham pontos quando afetam o Brasil (dólar, juros, commodities, exportações, acordo Mercosul–UE). Notícias repercutidas por vários veículos ao mesmo tempo ganham pontos de engajamento.

## 5. Entrega
1. **Horário da coleta** e status das bolsas
2. **Painel por região** (Américas, União Europeia, Resto da Europa, Ásia-Pacífico, Oriente Médio e África): uma linha por país com bandeira, índice, moeda e o fato do dia. Na UE, os 5 países de destaque sempre aparecem; os demais aparecem numa tabela compacta e, sem novidade relevante, só com os números.
3. **Destaques da B3:** maiores altas e baixas e empresas em evidência, com fundamentos (P/L, dividend yield) quando forem pauta
4. **Top 5 pautas**, cada uma com: gancho, o que aconteceu (2–3 frases, com fonte), por que importa para o seguidor brasileiro, formato sugerido (reel, carrossel ou stories) e urgência (hoje, esta semana ou perene)
5. **Agenda global dos próximos 7 dias:** decisões de juros, dados importantes, eleições, cimeiras da UE, balanços
6. **Fontes** com links de todas as páginas usadas

Como o painel cobre mais de 45 países, entregue as 5 pautas, os destaques da B3 e a agenda na conversa, e o painel completo como documento ou dashboard, oferecendo isso em uma linha.

## 6. Cuidados
- Não faça recomendação de compra ou venda; sugira o aviso "não é recomendação de investimento" nos posts.
- Política: fatos e posições de forma equilibrada, sem tomar partido.
- Não invente números nem citações; se algo não foi confirmado ou o dado está atrasado, diga isso.
- Parafraseie as notícias com suas próprias palavras; não copie trechos das matérias e cite sempre o veículo.

## 7. Rotina (opcional)
Se o usuário quiser receber a pauta automaticamente, ofereça tarefas agendadas, por exemplo: 7h45 (antes da abertura, com fechamento da Ásia e Europa aberta), 12h45 (meio do pregão) e 18h15 (fechamento), horário de Brasília, dias úteis.
