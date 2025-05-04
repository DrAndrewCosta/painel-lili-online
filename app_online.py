
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

busca = st.text_input("🔍 Buscar frase ou alteração:").strip().lower()

filtro = frases[frases['sistema_anatomico'] == sistema]
if busca:
    filtro = filtro[filtro.apply(lambda row: busca in str(row).lower(), axis=1)]

st.write(f"### {len(filtro)} frase(s) encontrada(s):")
selecionada = st.radio("Selecione uma frase para ver variações:", filtro['descricao_da_alteracao'].tolist(), index=0 if len(filtro) > 0 else None)

if selecionada:
    st.markdown("---")
    st.subheader("🎯 Variações automáticas sugeridas")
    st.write("💬 **Frase original:**")
    st.info(selecionada)

    st.write("✳️ **Técnica:**")
    st.success("Paciente com " + selecionada.lower())

    st.write("✳️ **Concisa:**")
    st.success(selecionada.split(",")[0] + ".")

    st.write("✳️ **Explicativa:**")
    st.success("Achado compatível com " + selecionada.lower() + ", conforme padrão ultrassonográfico observado.")

