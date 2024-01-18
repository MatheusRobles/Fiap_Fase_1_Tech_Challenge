import pandas as pd
import streamlit as st
import plotly.express as px
def carrega_csv(nome_arquivo):
    caminho = "https://raw.githubusercontent.com/MatheusRobles/Fiap_Fase_1_Tech_Challenge/main/"
    nome_arquivo_tratado = caminho + nome_arquivo + ".csv"
    df = pd.read_csv(nome_arquivo_tratado)
    return df

def config_streamlit() -> None:
    st.set_page_config(
        page_title="Tech Challenge: Exportação de Vinho",
        page_icon="https://images.emojiterra.com/google/noto-emoji/unicode-15/animated/1f377.gif",
        layout="wide",
    )

def scatter_geo_media_preco_litro(df, y_col='Quantidade (L)', start_year=None, end_year=None, min_quantity=0, altura_grafico=500):
    # Filtra os dados para o intervalo de anos desejado
    if start_year is not None and end_year is not None:
        df_filtered = df[(df['Anos'] >= start_year) & (df['Anos'] <= end_year)]
    else:
        df_filtered = df.copy()

    # Filtra valores maiores que 0 e quantidades maiores que min_quantity
    df_filtered = df_filtered[(df_filtered['Preço do Litro'] > 0) & (df_filtered['Quantidade (L)'] > min_quantity)]
    # Calcula a média do preço por litro por país
    df_mean_price = df_filtered.groupby(['País de Destino', 'iso_alpha', 'Regiao'])[['Preço do Litro']].mean().reset_index()

    # Arredonda o preço médio por litro para 2 casas decimais
    df_mean_price['Preço Médio do Litro'] = df_mean_price['Preço do Litro'].round(2)
    # Soma os valores para cada país
    df_sum = df_filtered.groupby(['País de Destino', 'iso_alpha', 'Regiao'])[['Quantidade (L)', 'Valor Exportado (US$)']].sum().reset_index()

    # Adiciona a coluna de preço médio ao DataFrame com a soma
    df_sum['Preço Médio do Litro (US$)'] = df_mean_price['Preço Médio do Litro']

    # Cria o scatter geo usando Plotly Express
    fig = px.scatter_geo(
        df_sum,
        locations="iso_alpha",
        size=y_col,
        color="Preço Médio do Litro (US$)",
        projection="natural earth",
        title=f'Média do Preço por Litro vs {y_col} - (Quantidade > {min_quantity} L) - ({start_year}-{end_year})',
        size_max=30,
        custom_data=["País de Destino", y_col, "Preço Médio do Litro (US$)"],
        template="seaborn",  # Define o tema como dark # Ajusta a largura da figura
        height=altura_grafico   # Ajusta a altura da figura
    )

    # Adiciona título ao eixo de cores
    fig.update_coloraxes(colorbar_title="Preço Médio por Litro (US$)")

    # Ajusta o layout para ter um fundo transparente
    fig.update_layout(
        geo=dict(bgcolor='rgba(0,0,0,0)', lakecolor='rgba(0,0,0,0)'),
        margin = {"l": 10, "r": 10, "b": 10, "t": 85, "pad": 5},  # Define a cor de fundo e de lagos como transparente
    )

    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def top_regioes_com_maior_preco_litro(df, y_col='Preço do Litro', start_year=None, end_year=None, min_quantity=0, altura_grafico=500, largura_grafico=1200):
    # Filtra os dados para o intervalo de anos desejado
    if start_year is not None and end_year is not None:
        df_filtered = df[(df['Anos'] >= start_year) & (df['Anos'] <= end_year)]
    else:
        df_filtered = df.copy()

    # Filtra valores maiores que 0 e quantidades maiores que 1000
    df_filtered = df_filtered[(df_filtered[y_col] > 0) & (df_filtered['Quantidade (L)'] > min_quantity)]

    # Calcula a média das médias por Regiao
    df_mean_region = df_filtered.groupby(['Regiao', 'País de Destino'])[y_col].mean().reset_index()
    df_top_region = df_mean_region.groupby('Regiao')[y_col].mean().nlargest(20).reset_index()

    # Cria o gráfico de barras usando Plotly Express
    fig = px.bar(df_top_region, x='Regiao', y=y_col,
                 labels={'x': 'Regiao', 'y': y_col},
                 title=f'Média do {y_col} por Região (Quantidade > {min_quantity} L) por Região - ({start_year}-{end_year})',
                 template="plotly_dark",        
                 width=largura_grafico,   # Ajusta a largura da figura
                 height=altura_grafico    # Ajusta a altura da figura
                 )  # Define o tema como dark

    # Ajusta o layout para ter um fundo transparente
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Define a cor de fundo como transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Define a cor do papel como transparente
    )

    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def top_paises_maior_preco_litro_por_regiao(df, y_col='Preço do Litro', start_year=None, end_year=None, min_quantity=0, altura_grafico=500, largura_grafico=1200):
    # Filtra os dados para o intervalo de anos desejado
    if start_year is not None and end_year is not None:
        df_filtered = df[(df['Anos'] >= start_year) & (df['Anos'] <= end_year)]
    else:
        df_filtered = df.copy()

    # Filtra valores maiores que 0 e quantidades maiores que 1000
    df_filtered = df_filtered[(df_filtered[y_col] > 0) & (df_filtered['Quantidade (L)'] > min_quantity)]

    # Obtém os top países com o maior preço por litro por região
    df_top_region = df_filtered.groupby(['Regiao', 'País de Destino'])[y_col].mean().nlargest(20).reset_index()

    # Cria o gráfico de barras usando Plotly Express
    fig = px.bar(df_top_region, x='País de Destino', y=y_col, color='Regiao',
                 labels={'x': 'País', 'y': y_col},
                 title=f'Top Países com Maior {y_col} (Quantidade > {min_quantity} L) por Região - ({start_year} - {end_year})',
                 template="plotly_dark",
                 width=largura_grafico, 
                 height=altura_grafico)

    # Ajusta o layout para ter um fundo transparente
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Define a cor de fundo como transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Define a cor do papel como transparente
    )

    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def preco_medio_litro_por_ano(df, y_col='Preço do Litro', start_year=None, end_year=None, min_quantity=1000, altura_grafico=500, largura_grafico=1200):
    # Filtra os dados para o intervalo de anos desejado
    if start_year is not None and end_year is not None:
        df_filtered = df[(df['Anos'] >= start_year) & (df['Anos'] <= end_year)]
    else:
        df_filtered = df.copy()

    # Filtra valores maiores que 0 e quantidades maiores que min_quantity
    df_filtered = df_filtered[(df_filtered[y_col] > 0) & (df_filtered['Quantidade (L)'] > min_quantity)]

    # Calcula a média do Preço do Litro por Regiao
    df_mean = df_filtered.groupby(['Anos', 'Regiao'])[y_col].mean().reset_index()

    # Adiciona uma linha extra com a média total
    df_total_mean = df_filtered.groupby('Anos')[y_col].mean().reset_index()
    df_total_mean['Regiao'] = 'Total'

    # Concatena os DataFrames para incluir a linha extra
    df_mean = pd.concat([df_mean, df_total_mean])

    # Cria o gráfico de linha usando Plotly Express
    fig = px.line(df_mean, x='Anos', y=y_col, color='Regiao', labels={'x': 'Ano', 'y': y_col},
                  title=f'Média do {y_col} por Ano e Regiao - ({start_year} - {end_year})',
                  template="plotly_dark",
                  width=largura_grafico, 
                  height=altura_grafico)  # Define o tema como dark

    # Ajusta o layout para ter um fundo transparente
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Define a cor de fundo como transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Define a cor do papel como transparente
    )

    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def histograma_por_pais(df, y_col='Quantidade (L)', start_year=None, end_year=None, altura_grafico=500, largura_grafico=1200):
    # Filtra os dados para o intervalo de anos desejado
    if start_year is not None and end_year is not None:
        df_filtered = df[(df['Anos'] >= start_year) & (df['Anos'] <= end_year)]
    else:
        df_filtered = df.copy()

    # Soma os valores para cada país
    df_sum = df_filtered.groupby('País de Destino')[y_col].sum().reset_index()

    # Ordena por valor em ordem decrescente
    df_sum = df_sum.sort_values(by=y_col, ascending=False)

    # Pega os 15 maiores
    df_top15 = df_sum.head(10)

    # Cria o histograma usando Plotly Express
    fig = px.bar(df_top15, x='País de Destino', y=y_col,
                 labels={'x': 'País', 'y': y_col},
                 title=f'Top 10 {y_col} por País - ({start_year} - {end_year})',
                 template="plotly_dark",
                 width=largura_grafico,
                 height=altura_grafico)  # Define o tema como dark

    # Ajusta o layout para ter um fundo transparente
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Define a cor de fundo como transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Define a cor do papel como transparente
    )

    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def histograma_por_regiao(df, y_col='Quantidade (L)', start_year=None, end_year=None, altura_grafico=500, largura_grafico=1200):
    # Filtra os dados para o intervalo de anos desejado
    if start_year is not None and end_year is not None:
        df_filtered = df[(df['Anos'] >= start_year) & (df['Anos'] <= end_year)]
    else:
        df_filtered = df.copy()

    # Soma os valores para cada continente
    df_sum = df_filtered.groupby('Regiao')[y_col].sum().reset_index()

    # Ordena por valor em ordem decrescente
    df_sum = df_sum.sort_values(by=y_col, ascending=False)

    # Pega os maiores
    df_top = df_sum 

    # Cria o histograma usando Plotly Express
    fig = px.bar(df_top, x='Regiao', y=y_col,
                 labels={'x': 'Regiao', 'y': y_col},
                 title=f'{y_col} Total por Regiao - ({start_year} - {end_year})',
                 template="plotly_dark",
                 width=largura_grafico,
                 height=altura_grafico)  # Define o tema como dark

    # Ajusta o layout para ter um fundo transparente
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Define a cor de fundo como transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Define a cor do papel como transparente
    )
    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def total_expotado_por_ano(df, y_col='Quantidade (L)', start_year=None, end_year=None, altura_grafico=500, largura_grafico=1200):
    # Filtra os dados para o intervalo de anos desejado
    if start_year is not None and end_year is not None:
        df_filtered = df[(df['Anos'] >= start_year) & (df['Anos'] <= end_year)]
    else:
        df_filtered = df.copy()

    # Soma os valores para cada ano
    df_sum = df_filtered.groupby('Anos')[y_col].sum().reset_index()

    # Cria o histograma usando Plotly Express
    fig = px.bar(df_sum, x='Anos', y=y_col,
                 labels={'x': 'Ano', 'y': y_col},
                 title=f'Soma {y_col} Total por Ano - ({start_year} - {end_year})',
                 template="plotly_dark",
                 width=largura_grafico,
                 height=altura_grafico)  # Define o tema como dark

    # Ajusta o layout para ter um fundo transparente
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Define a cor de fundo como transparente
        paper_bgcolor='rgba(0,0,0,0)',  # Define a cor do papel como transparente
    )

    # Mostra o gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

def config_graficos(df):
    # Adiciona controles para escolher a variável y_col e o período de anos
    st.subheader("Configurações")

    # Adiciona um expander para configurar o gráfico
    with st.expander("⚙️ Configuração do Gráfico", expanded=True):
        # Barra de slider para escolher o período de anos
        start_year, end_year = st.slider("Período", df['Anos'].min(), df['Anos'].max(), (df['Anos'].min(), df['Anos'].max()), key="unique_key_for_slider")

        # Layout em uma única linha para y_col e quant_min
        col_y_col, col_quant_min = st.columns([1, 1])

        # Dropdown para escolher a variável y_col
        with col_y_col:
            y_col = st.selectbox("Variável", ["Quantidade (L)", "Valor Exportado (US$)"], index=0)

        # Input numérico para escolher a quantidade mínima
        with col_quant_min:
            quant_min = st.number_input("Quantidade Mínima de Litros Importados", min_value=0)

    return y_col, start_year, end_year, quant_min

def plot_2(func1, func2, *args, **kwargs):
    col1, col2 = st.columns(2)

    with col1:
        func1(*args, **kwargs)

    with col2:
        func2(*args, **kwargs)
