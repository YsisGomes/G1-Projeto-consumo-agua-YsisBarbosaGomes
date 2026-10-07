# Consumo de Água no Brasil

## Projeto G1 — Análise e Visualização de Dados

**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python  
**Professor:** Alexandre Neves Louzada  
**Aluna:** Ysis Barbosa Gomes  

---

## Sobre o projeto

Este projeto apresenta uma análise do consumo de água no Brasil entre os anos de 2015 e 2024.

A partir de uma base de dados com informações sobre consumo, desperdício, níveis de reservatórios, chuva, temperatura, população e setores de consumo, foram desenvolvidas análises exploratórias e visualizações para identificar padrões relacionados ao uso dos recursos hídricos.

O projeto é composto por uma análise exploratória desenvolvida em Python e por um dashboard interativo criado com Streamlit.

## Objetivos da análise

O projeto busca analisar questões como:

- Quais estados apresentam maior consumo de água?
- Quais regiões concentram os maiores volumes de consumo?
- Quais setores apresentam maior consumo?
- Existem padrões sazonais no consumo de água?
- Qual é o nível médio de desperdício?
- Como estão os níveis dos reservatórios?
- Existe relação entre chuva e consumo de água?

## Indicadores principais

O dashboard apresenta os seguintes indicadores:

- Consumo total de água;
- UF com maior consumo;
- Setor com maior consumo;
- Consumo per capita médio;
- Desperdício médio;
- Nível médio dos reservatórios.

## Dashboard interativo

O dashboard permite aplicar filtros por:

- Ano;
- Mês;
- Região;
- UF;
- Setor de consumo;
- Nível de alerta.

Os indicadores, gráficos, análises e interpretações são atualizados de acordo com os filtros selecionados.

## Visualizações

Entre as principais análises apresentadas estão:

- Evolução do consumo ao longo dos anos;
- Consumo por região;
- Consumo por setor;
- Ranking de consumo por UF;
- Sazonalidade do consumo;
- Relação entre chuva e consumo.

## Tecnologias utilizadas

- Python
- Pandas
- Matplotlib
- Seaborn
- Streamlit
- NumPy
- SQLAlchemy
- SQLite
- GitHub
- GitHub Pages

## Estrutura do projeto

```text
projeto-consumo-agua/
├── .streamlit/
│   └── config.toml
├── dados/
│   └── simulacao_consumo_agua_brasil.csv
├── database/
├── imagens/
├── notebooks/
│   └── analise_consumo_agua.ipynb
├── app.py
├── index.html
├── README.md
└── requirements.txt