
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Painel Lili Online', layout='wide')
st.title('Painel Lili - Versão Online (Lote 5 - MSK)')

uploaded_file = st.file_uploader("📁 Enviar nova base de frases (.csv)", type="csv")

if uploaded_file:
    frases = pd.read_csv(uploaded_file)
    st.success("Base carregada com sucesso!")
else:
    frases = pd.read_csv("banco_frases_app_lili_lote5.csv")

sistemas = frases['sistema_anatomico'].dropna().unique()
sistema = st.selectbox("Selecionar sistema anatômico:", sorted(sistemas))
busca = st.text_input("Buscar frase ou alteração:").strip().lower()

filtro = frases[frases['sistema_anatomico'] == sistema]
if busca:
    filtro = filtro[filtro.apply(lambda row: busca in str(row).lower(), axis=1)]

st.write(f"### {len(filtro)} frase(s) encontrada(s):")
st.dataframe(filtro, use_container_width=True)
