import streamlit as st
import pandas as pd
import plotly.express as px
from functions import *


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
    st.write("**Análise de Exportação de Vinhos (2012-2022): Destaques e Tendências**")

    # Storytelling
    st.markdown(
        "Nos últimos 10 anos, a exportação de vinhos da vinícola do Rio Grande do Sul revela um cenário notável. O Paraguai se destaca como o principal importador, ultrapassando 25 milhões de litros, seguido pela Rússia, que também desempenha um papel significativo. Esses dois países lideram as tendências de exportação, refletindo a importância da América do Sul e Europa como regiões estratégicas. Em essência, a expressiva presença nos mercados paraguaio e russo molda o panorama global, consolidando a relevância dessas duas regiões-chave."
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
        "Aprofundando nossa exploração, voltamos nosso olhar para o preço médio do litro de vinho exportado, uma métrica valiosa para avaliar o potencial de novos mercados. Nessa análise, a Áustria surge como um ponto notável, atingindo incríveis 21 dólares por litro, destacando-se como um possível outlier. Ao analisarmos mais detalhadamente, percebemos que esse valor elevado se deve, em grande parte, à importação de quantidades relativamente baixas de vinho por um preço mais alto, o que pode distorcer a média e tornar essa percepção do mercado potencial um tanto enganadora."
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
    "Ao analisarmos os gráficos, é notável que em 2017 ocorreram vários valores significativamente altos para o preço médio do litro. Essa tendência pode ser atribuída ao fato de que o Brasil atingiu recordes de produção de vinho neste ano, impactando diretamente nos valores médios"
    )

    st.markdown(
        "Ao aplicarmos uma filtragem técnica na análise, optamos por considerar apenas os países que importaram mais de 10.000 litros de vinho anualmente. Essa abordagem proporciona uma visão mais específica, destacando mercados consumidores robustos que, apesar de seu potencial, podem não estar sendo totalmente explorados."
    )
    st.markdown(
        "Essa filtragem técnica visa focar em países que não apenas apresentam um alto preço médio por litro, mas também sustentam uma demanda consistente, indicando um mercado consumidor forte. Ao identificar essas oportunidades, a estratégia da vinícola pode ser ajustada para aproveitar ao máximo esses mercados ainda não totalmente explorados."
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
        "Concluímos nossa análise com não apenas números, mas com estratégias práticas que moldarão a expansão das exportações de vinhos brasileiros. Nossa jornada pelos dados, embasada em insights, aponta para um caminho promissor que nos conduzirá ao sucesso global."
    )
    st.markdown(
        "Na fase final da análise, ao compararmos diferentes abordagens, a aplicação da filtragem pela quantidade em litros revela oportunidades de mercado alinhadas com nossos objetivos de crescimento. O preço médio do litro, combinado com volumes substanciais de exportação, destaca mercados promissores que merecem nossa atenção estratégica. Nossa trajetória nos leva a considerar não apenas os maiores compradores, mas também aqueles que representam verdadeiros potenciais de expansão para nossos vinhos brasileiros."
    )
    st.markdown(
        "Um enfoque particular merece destaque: ao mirarmos na Suíça, Finlândia, Canadá, Catar e Austrália, percebemos que, embora Paraguai e Rússia tenham registros expressivos em quantidade, há um vasto terreno a ser explorado em outros mercados. Especialmente ao considerar países fora da América do Sul e Europa, como Austrália e Catar, identificamos possibilidades estratégicas na Ásia e Oceania, incluindo potenciais expansões para China e Taiwan. Esta abordagem focada e estratégica nos posiciona para evidenciar um mercado promissor, diversificando nossos esforços de exportação e impulsionando o sucesso global de nossos vinhos."
    )

    st.divider()
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
    st.markdown(
        """
        ###### DataFrame com todos as informações utilizadas na análise.
        """
    )
    st.dataframe(Tabela_Exportacao_Vinhos)
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
