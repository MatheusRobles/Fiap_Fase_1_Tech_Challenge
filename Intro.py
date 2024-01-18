import streamlit as st
from functions import *


def intro(df):
    st.markdown(
        """
        ###### Tabela com informações sobre a exportação de vinho
        Tabela contendo as informações solicitadas sobre a exportação de vinho, como país de origem, país de destino, ano de referência, quantidade de vinho exportado (em litros) e valor total exportado (em US$)
        """
    )

    colunas_selecionadas = ["País de Destino", "País de Origem", "Anos", "Quantidade (L)", "Valor Exportado (US$)"]
    df_visualizacao = df[colunas_selecionadas]
    st.dataframe(df_visualizacao)

