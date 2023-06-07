import streamlit as st
import pandas as pd
import altair as alt
from PIL import Image



st.set_page_config(layout='wide')

df = pd.read_csv('ocorrencia.csv', encoding='ISO-8859-1', sep=';', on_bad_lines='skip')

with st.sidebar:
    logo = Image.open('icon.png')
    st.image(logo, use_column_width=True)
    st.subheader('Projeto de Data Science')
    st.subheader('Seleção de filtros')

    fCLassificacao = st.selectbox(
        "Selecione a classificação: ",
        options= df['ocorrencia_classificacao'].unique()
    )
    fuf = st.selectbox(
        "Selecione o estado: ",
        options = df['ocorrencia_uf'].unique(),
    )
    
    dadosUsuario = df.loc[(
        df['ocorrencia_classificacao'] == fCLassificacao) &
        (df['ocorrencia_uf'] == fuf
    )]

st.header('Dados de ocorrências aeronáuticas da aviação civil brasileira.')
st.markdown('Classificação de ocorrencia selecionada: ' + fCLassificacao)
st.markdown('Estado selecionado: ' + fuf)


grafOcorrenciaEstado = alt.Chart(dadosUsuario).mark_point().encode(
        x = 'codigo_ocorrencia',
        y = 'ocorrencia_cidade',
       
        strokeWidth=alt.value(3)
).properties(
        height = 350,
        width = 1000
    )


st.altair_chart(grafOcorrenciaEstado)