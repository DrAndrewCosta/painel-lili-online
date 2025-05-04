
import streamlit as st
import pandas as pd

st.set_page_config(page_title='Painel Lili Online', layout='wide')
st.title('Painel Lili - Variações + Editor Integrado')

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

frases_disponiveis = filtro['descricao_da_alteracao'] if 'descricao_da_alteracao' in filtro.columns else filtro.iloc[:,0]
frases_lista = frases_disponiveis.tolist()

col1, col2 = st.columns([1.1, 1.6])  # Painel à esquerda, laudo à direita

with col1:
    st.markdown("### 🧠 Painel de sugestões clínicas")
    if frases_lista:
        selecionada = st.radio("Selecione uma frase:", frases_lista, index=0)
        st.markdown("---")
        st.write("💬 **Frase original:**")
        st.info(selecionada)

        def gerar_tecnica(frase):
            return frase if frase.endswith('.') else frase + "."

        def gerar_concisa(frase):
            return frase.split(",")[0].strip() + "."

        def gerar_explicativa(frase):
            return "Achado compatível com " + frase.lower().rstrip(".") + ", em concordância com padrão ultrassonográfico benigno."

        st.write("✳️ **Técnica:**")
        st.success(gerar_tecnica(selecionada))

        st.write("✳️ **Concisa:**")
        st.success(gerar_concisa(selecionada))

        st.write("✳️ **Explicativa:**")
        st.success(gerar_explicativa(selecionada))

with col2:
    st.markdown("### 📄 Editor do laudo em tempo real")
    laudo_inicial = "Insira aqui o conteúdo do laudo completo. Conforme editar ou aplicar frases, o texto será atualizado em tempo real."
    laudo = st.text_area("Laudo final:", value=laudo_inicial, height=500)
    st.success("Você pode copiar e colar diretamente as variações ou usar comandos de voz em breve.")
