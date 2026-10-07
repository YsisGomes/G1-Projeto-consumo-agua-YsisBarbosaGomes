import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="Consumo de Água no Brasil",
    layout="wide"
)

st.title("Consumo de Água no Brasil")

st.write(
    "Dashboard de análise e visualização dos dados "
    "de consumo de água no Brasil entre 2015 e 2024."
)

st.markdown("""
**Disciplina:** Linguagem de Programação — Análise e Visualização de Dados com Python  
**Professor:** Alexandre Neves Louzada  
**Aluna:** Ysis Barbosa Gomes
""")

st.divider()

df = pd.read_csv(
    "dados/simulacao_consumo_agua_brasil.csv"
)

df["data"] = pd.to_datetime(df["data"])

st.sidebar.header("Filtros")

anos = sorted(df["ano"].unique())
anos_selecionados = st.sidebar.multiselect(
    "Ano",
    anos,
    default=anos
)

meses = sorted(df["mes"].unique())
meses_selecionados = st.sidebar.multiselect(
    "Mês",
    meses,
    default=meses
)

regioes = sorted(df["regiao"].unique())
regioes_selecionadas = st.sidebar.multiselect(
    "Região",
    regioes,
    default=regioes
)

ufs = sorted(df["uf"].unique())
ufs_selecionadas = st.sidebar.multiselect(
    "UF",
    ufs,
    default=ufs
)

setores = sorted(df["setor_consumo"].unique())
setores_selecionados = st.sidebar.multiselect(
    "Setor de consumo",
    setores,
    default=setores
)

alertas = sorted(df["nivel_alerta"].unique())
alertas_selecionados = st.sidebar.multiselect(
    "Nível de alerta",
    alertas,
    default=alertas
)

df_filtrado = df[
    (df["ano"].isin(anos_selecionados)) &
    (df["mes"].isin(meses_selecionados)) &
    (df["regiao"].isin(regioes_selecionadas)) &
    (df["uf"].isin(ufs_selecionadas)) &
    (df["setor_consumo"].isin(setores_selecionados)) &
    (df["nivel_alerta"].isin(alertas_selecionados))
]

st.subheader("Indicadores principais")

if not df_filtrado.empty:

    consumo_total = df_filtrado["consumo_milhoes_litros"].sum()

    consumo_uf = (
        df_filtrado.groupby("uf")["consumo_milhoes_litros"]
        .sum()
        .sort_values(ascending=False)
    )

    maior_uf = consumo_uf.index[0]

    consumo_setor = (
        df_filtrado.groupby("setor_consumo")["consumo_milhoes_litros"]
        .sum()
        .sort_values(ascending=False)
    )

    maior_setor = consumo_setor.index[0]

    consumo_per_capita = df_filtrado["consumo_per_capita"].mean()
    desperdicio_medio = df_filtrado["desperdicio_percentual"].mean()
    reservatorio_medio = df_filtrado["reservatorios_percentual"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Consumo total",
        f"{consumo_total:,.2f} milhões L"
    )

    col2.metric(
        "UF com maior consumo",
        maior_uf
    )

    col3.metric(
        "Setor com maior consumo",
        maior_setor
    )

    col4, col5, col6 = st.columns(3)

    col4.metric(
        "Consumo per capita médio",
        f"{consumo_per_capita:.2f}"
    )

    col5.metric(
        "Desperdício médio",
        f"{desperdicio_medio:.2f}%"
    )

    col6.metric(
        "Nível médio dos reservatórios",
        f"{reservatorio_medio:.2f}%"
    )
else:
    st.warning("Nenhum dado encontrado para os filtros selecionados.")

st.divider()
st.subheader("Análise do consumo")

if not df_filtrado.empty:

    col_grafico1, col_grafico2 = st.columns(2)

    consumo_anual = (
        df_filtrado.groupby("ano")["consumo_milhoes_litros"]
        .sum()
        .reset_index()
    )

    fig1, ax1 = plt.subplots(figsize=(8, 5))

    sns.lineplot(
        data=consumo_anual,
        x="ano",
        y="consumo_milhoes_litros",
        marker="o",
        ax=ax1
    )

    ax1.set_title("Evolução do Consumo")
    ax1.set_xlabel("Ano")
    ax1.set_ylabel("Milhões de litros")

    col_grafico1.pyplot(fig1)

    plt.close(fig1)

    consumo_regiao = (
        df_filtrado.groupby("regiao")["consumo_milhoes_litros"]
        .sum()
        .reset_index()
        .sort_values(
            "consumo_milhoes_litros",
            ascending=False
        )
    )

    fig2, ax2 = plt.subplots(figsize=(8, 5))

    sns.barplot(
        data=consumo_regiao,
        x="regiao",
        y="consumo_milhoes_litros",
        ax=ax2
    )

    ax2.set_title("Consumo por Região")
    ax2.set_xlabel("Região")
    ax2.set_ylabel("Milhões de litros")

    ax2.tick_params(axis="x", rotation=20)

    col_grafico2.pyplot(fig2)

    plt.close(fig2)


    col_grafico3, col_grafico4 = st.columns(2)

    consumo_setor_grafico = (
        df_filtrado.groupby("setor_consumo")["consumo_milhoes_litros"]
        .sum()
        .reset_index()
        .sort_values("consumo_milhoes_litros", ascending=False)
    )

    fig3, ax3 = plt.subplots(figsize=(8, 5))

    sns.barplot(
        data=consumo_setor_grafico,
        x="setor_consumo",
        y="consumo_milhoes_litros",
        ax=ax3
    )

    ax3.set_title("Consumo por Setor")
    ax3.set_xlabel("Setor")
    ax3.set_ylabel("Milhões de litros")
    ax3.tick_params(axis="x", rotation=20)

    col_grafico3.pyplot(fig3)

    plt.close(fig3)

    consumo_uf_grafico = (
        df_filtrado.groupby("uf")["consumo_milhoes_litros"]
        .sum()
        .reset_index()
        .sort_values("consumo_milhoes_litros", ascending=False)
    )

    fig4, ax4 = plt.subplots(figsize=(8, 5))

    sns.barplot(
        data=consumo_uf_grafico,
        x="consumo_milhoes_litros",
        y="uf",
        ax=ax4
    )

    ax4.set_title("Ranking de Consumo por UF")
    ax4.set_xlabel("Milhões de litros")
    ax4.set_ylabel("UF")

    col_grafico4.pyplot(fig4)

    plt.close(fig4)

    st.subheader("Sazonalidade do Consumo")

    consumo_mensal = (
        df_filtrado.groupby(["ano", "mes"])["consumo_milhoes_litros"]
        .sum()
        .reset_index()
    )

    tabela_sazonalidade = consumo_mensal.pivot(
        index="ano",
        columns="mes",
        values="consumo_milhoes_litros"
    )

    fig5, ax5 = plt.subplots(figsize=(12, 6))

    sns.heatmap(
        tabela_sazonalidade,
        cmap="Blues",
        annot=True,
        fmt=".0f",
        ax=ax5
    )

    ax5.set_title("Consumo de Água por Ano e Mês")
    ax5.set_xlabel("Mês")
    ax5.set_ylabel("Ano")

    st.pyplot(fig5)

    plt.close(fig5)

    st.subheader("Relação entre Chuva e Consumo")

    fig6, ax6 = plt.subplots(figsize=(10, 5))

    sns.scatterplot(
        data=df_filtrado,
        x="chuva_mm",
        y="consumo_milhoes_litros",
        ax=ax6
    )

    ax6.set_title("Chuva × Consumo de Água")
    ax6.set_xlabel("Chuva (mm)")
    ax6.set_ylabel("Consumo (milhões de litros)")

    st.pyplot(fig6)

    plt.close(fig6)

    correlacao = df_filtrado[
        ["chuva_mm", "consumo_milhoes_litros"]
    ].corr().iloc[0, 1]

    st.write(
        f"**Correlação entre chuva e consumo:** {correlacao:.3f}"
    )

    st.subheader("Interpretação dos Resultados")

    regiao_maior_consumo = (
        df_filtrado.groupby("regiao")["consumo_milhoes_litros"]
        .sum()
        .idxmax()
    )

    uf_maior_consumo = (
        df_filtrado.groupby("uf")["consumo_milhoes_litros"]
        .sum()
        .idxmax()
    )

    setor_maior_consumo = (
        df_filtrado.groupby("setor_consumo")["consumo_milhoes_litros"]
        .sum()
        .idxmax()
    )

    st.write(
        f"""
        Considerando os filtros selecionados, a região com maior consumo de água
        é **{regiao_maior_consumo}**, enquanto a UF com maior consumo é
        **{uf_maior_consumo}**.
        \nO setor que apresenta o maior consumo é o **{setor_maior_consumo}**.
        \nO desperdício médio no período selecionado é de
        **{desperdicio_medio:.2f}%**, enquanto o nível médio dos reservatórios
        é de **{reservatorio_medio:.2f}%**.
        """
    )

    st.subheader("Conclusão Executiva")

    st.write(
        f"""
        A análise dos dados permite observar diferenças nos padrões de consumo
        de água entre regiões, estados, setores e períodos.\n
        Para os filtros selecionados, **{uf_maior_consumo}** apresenta o maior
        consumo entre as UFs analisadas, enquanto o setor **{setor_maior_consumo}**
        possui o maior volume de consumo.\n
        O desperdício médio de **{desperdicio_medio:.2f}%** reforça a importância
        de ações voltadas ao uso eficiente da água e à redução de perdas.\n
        A análise da relação entre chuva e consumo apresentou correlação de
        **{correlacao:.3f}**, indicando o grau de associação linear entre essas
        duas variáveis no recorte selecionado.\n
        Esses indicadores contribuem para identificar padrões e apoiar o
        acompanhamento do consumo e da disponibilidade de recursos hídricos.
        """
    )

st.subheader("Dados filtrados")

st.write(f"Registros encontrados: {len(df_filtrado)}")

st.dataframe(
    df_filtrado,
    use_container_width=True
)