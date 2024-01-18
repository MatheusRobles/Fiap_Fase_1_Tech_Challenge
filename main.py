import streamlit as st
import pandas as pd
import requests
import plotly.express as px
from functions import *
from Intro import*
from tabela import*
from graficos import*

config_streamlit()

# Título
st.markdown("# <span style='color:#636efa'>Explorando a Exportação de Vinhos Brasileiros</span>", unsafe_allow_html=True)

# Introdução
st.markdown(
    "Bem-vindos ao Tech Challenge: Exportação de Vinho, uma imersão estratégica nos dados que delineiam o sucesso da exportação de vinhos de uma vinícola brasileira situada no Rio Grande do Sul. Como Expert em Data Analytics, nossa missão é fornecer insights valiosos que impulsionarão as decisões estratégicas da empresa. Embarque conosco nessa jornada analítica, onde cada dado é uma peça essencial para desvendar oportunidades e desafios."
)

# Contexto e Fonte de Dados
st.markdown(
    """
    **Contexto:**
    Nossa área de Data Analytics é recém-criada, e enfrentamos a emocionante tarefa de apresentar relatórios iniciais em uma reunião crucial com investidores e acionistas. Nosso foco está na exportação de vinhos do Brasil para o mundo, utilizando dados da [Embrapa Uva e Vinho](http://vitibrasil.cnpuv.embrapa.br/), uma fonte confiável e abrangente.
    """
)

st.markdown(
    """
    A vinícola, situada no Rio Grande do Sul, destaca a Região Sul do Brasil, responsável por 90% das exportações de vinhos do país. Nossa análise abrange a tendência de mercado, considerando o preço médio do vinho, a quantidade em litros exportada por país e o valor total da exportação em dólares americanos.
    """
)

Tabela_Exportacao_Vinhos = carrega_csv('Tabela_Exportacao_Vinhos')

tabs = st.tabs(["🌎 Análise", "📋 DataFrame", "📊 Gráficos"])


with tabs[0]:
    st.write("**Análise de Tendências no Mercado de Vinhos: Rio Grande do Sul - Brasil**")

    # Storytelling
    st.markdown(
        "Ao explorarmos os últimos 10 anos de exportação de vinhos (2012 - 2022), emergem histórias que moldaram o caminho da vinícola no cenário global. "
        "Ao analisarmos as quantidades exportadas por país e região, identificamos padrões intrigantes apontando para mercados promissores. Vamos agora desvendar as narrativas por trás desses dados."
    )
    st.markdown(
        "A imersão nos números da exportação de vinhos nos últimos 10 anos revela líderes em volume, com destaque para o Paraguai, que se posiciona como líder em quantidade, ultrapassando 25 milhões de litros exportados. Além disso, a Rússia também se destaca como um importante mercado consumidor."
        "Esses dados refletem o papel crucial da América do Sul e Europa, regiões que se destacam devido ao grande número de vinhos exportados para países como Paraguai e Rússia."
    )
    st.divider()
    col1, col2 = st.columns(2)
    st.divider()
    
    # Gráfico de Quantidade por País (col1)
    with col1:
        histograma_por_pais(Tabela_Exportacao_Vinhos, y_col='Quantidade (L)', start_year=2012, end_year=2022, altura_grafico=500, largura_grafico=600)

    # Gráfico de Quantidade por Região (col2)
    with col2:
        histograma_por_regiao(Tabela_Exportacao_Vinhos, y_col='Quantidade (L)', start_year=2012, end_year=2022, altura_grafico=500, largura_grafico=600)
    st.markdown(
        "Ao explorarmos a quantidade em litros exportada por país e região, emergem líderes de mercado e regiões estratégicas. Essa análise inicial nos proporciona uma visão geográfica poderosa, guiando-nos na identificação de oportunidades de crescimento e expansão."
    )
    st.markdown(
        "Aprofundando nossa exploração, voltamos nosso olhar para o preço médio do litro de vinho exportado, uma métrica valiosa para avaliar o potencial de novos mercados. Nessa análise, a Áustria surge como um ponto notável, atingindo incríveis 21 dólares por litro, destacando-se como um outlier significativo. No entanto, ao analisarmos mais detalhadamente, percebemos que esse valor elevado se deve, em grande parte, à importação de quantidades relativamente baixas de vinho por um preço mais alto, o que pode distorcer a média e tornar essa percepção do mercado potencial um tanto enganadora."
    )

    st.divider()
    col1, col2 = st.columns(2)
    st.divider()
    
    # Gráfico de Média de Preço por Litro por Região (col1)
    with col2:
        scatter_geo_media_preco_litro(Tabela_Exportacao_Vinhos, y_col='Quantidade (L)', start_year=2012, end_year=2022, min_quantity=0,altura_grafico=500)

    # Tabela dos Países com Maior Preço Médio por Litro por Região (col2)
    with col1:
        top_paises_maior_preco_litro_por_regiao(Tabela_Exportacao_Vinhos, y_col='Preço do Litro', start_year=2012, end_year=2022, min_quantity=0,altura_grafico=500, largura_grafico=600)

    st.markdown(
    "Ao refinar nossa abordagem e aplicar uma filtragem estratégica, nossa análise se torna mais precisa, revelando os verdadeiros potenciais mercados. Identificamos situações em que um país aparentemente estratégico devido a um alto preço médio do litro pode, na verdade, ser enganoso quando consideramos a quantidade exportada. Para fornecer uma visão mais realista, propomos uma abordagem estratégica: considerar apenas países que adquiriram mais de 10.000 litros por ano. Essa filtragem oferece uma visão mais fiel do mercado, destacando verdadeiros potenciais e eliminando distorções."
    )
    
    st.divider()    
    preco_medio_litro_por_ano(Tabela_Exportacao_Vinhos, y_col='Preço do Litro', start_year=2012, end_year=2022, min_quantity=10000, altura_grafico=500, largura_grafico=1200)
    st.divider() 
    col1, col2 = st.columns(2)
    st.divider()
    
    # Gráfico de Média de Preço por Litro por Região com Filtro de Quantidade Mínima (col1)
    with col2:
        scatter_geo_media_preco_litro(Tabela_Exportacao_Vinhos, y_col='Quantidade (L)', start_year=2012, end_year=2022, min_quantity=10000,altura_grafico=500)

    # Tabela dos Países com Maior Preço Médio por Litro por Região com Filtro de Quantidade Mínima (col2)
    with col1:
        top_paises_maior_preco_litro_por_regiao(Tabela_Exportacao_Vinhos, y_col='Preço do Litro', start_year=2012, end_year=2022, min_quantity=10000,altura_grafico=500, largura_grafico=600)

    st.markdown(
        "Ao concluirmos nossa análise, não apresentamos apenas números, mas sim estratégias práticas que guiarão a expansão das exportações de vinhos brasileiros. Nossa jornada pelos dados, baseada em insights, aponta para um caminho promissor que nos levará ao sucesso global."
    )
    st.markdown(
        "Na conclusão da análise, comparamos diferentes abordagens. Ao aplicar a filtragem pela quantidade em litros, visualizamos oportunidades de mercado alinhadas com nossos objetivos de crescimento. O preço médio do litro, quando combinado com volumes substanciais de exportação, destaca mercados promissores que merecem nossa atenção estratégica. Nossa trajetória nos faz considerar não apenas os maiores compradores, mas também aqueles que representam verdadeiros potenciais de expansão para nossos vinhos brasileiros. Ao adotar uma abordagem focada e estratégica, estamos prontos para evidenciar um mercado promissor e traçar um caminho que potencializa nossos esforços de exportação, impulsionando o sucesso global de nossos vinhos."
    )
    st.markdown(
        """
        ###### Tabela Detalhada da Exportação de Vinho
        Abaixo, apresentamos a tabela detalhada com informações cruciais sobre a exportação de vinho, incluindo país de origem, país de destino, anos de referência, quantidade de vinho exportado (em litros) e valor total exportado (em US$).
        """
    )


    colunas_selecionadas = ["País de Destino", "País de Origem", "Anos", "Quantidade (L)", "Valor Exportado (US$)"]
    df_visualizacao = Tabela_Exportacao_Vinhos[colunas_selecionadas]
    st.dataframe(df_visualizacao)

with tabs[1]:
    tabela(Tabela_Exportacao_Vinhos)
with tabs[2]:
    y_col, start_year, end_year, quant_min = config_graficos(Tabela_Exportacao_Vinhos)
    st.markdown("<div style='margin-bottom: 30px'></div>", unsafe_allow_html=True)
    scatter_geo_media_preco_litro(Tabela_Exportacao_Vinhos, y_col, start_year=start_year, end_year=end_year, min_quantity=quant_min,altura_grafico=500)
    st.divider()
    preco_medio_litro_por_ano(Tabela_Exportacao_Vinhos, y_col='Preço do Litro', start_year=start_year, end_year=end_year, min_quantity=quant_min, altura_grafico=500, largura_grafico=1200)
    st.divider()
    top_paises_maior_preco_litro_por_regiao(Tabela_Exportacao_Vinhos, y_col='Preço do Litro', start_year=start_year, end_year=end_year, min_quantity=quant_min,altura_grafico=500, largura_grafico=1200)
    st.divider()
    top_regioes_com_maior_preco_litro(Tabela_Exportacao_Vinhos, y_col='Preço do Litro', start_year=start_year, end_year=end_year, min_quantity=quant_min,altura_grafico=500, largura_grafico=600)
    st.divider()
    histograma_por_pais(Tabela_Exportacao_Vinhos, y_col, start_year=start_year, end_year=end_year, altura_grafico=500, largura_grafico=600)
    st.divider()
    histograma_por_regiao(Tabela_Exportacao_Vinhos, y_col, start_year=start_year, end_year=end_year, altura_grafico=500, largura_grafico=600)
    st.divider()
    total_expotado_por_ano(Tabela_Exportacao_Vinhos, y_col, start_year=start_year, end_year=end_year, altura_grafico=500, largura_grafico=600)
