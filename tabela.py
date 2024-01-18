import streamlit as st
from functions import *




def tabela(df):
    st.markdown(
        """
        ###### DataFrame com todos as informações utilizadas na análise.
        """
    )
    st.dataframe(df)