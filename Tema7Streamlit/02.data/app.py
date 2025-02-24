import streamlit as st
import seaborn as sns

# Desactivo el certificado SSL de manera temporal para que no me de fallos
import ssl
ssl._create_default_https_context = ssl._create_unverified_context 

st.title('Streamlit API reference Data Elements')

st.header('Mostrar un DataFrame de Pandas')

# Cacheamos el dataframe para evitar recargarlo todo el rato
@st.cache_data
def load_tips_data():   
    return sns.load_dataset('tips')

df = load_tips_data()

st.dataframe(df, use_container_width=True)

st.header('Mostrar un DataFrame editable de Pandas')

df_edited = st.data_editor(df, use_container_width=True)

st.write('Este metodo``st.data_editor``permite modificar celdas, podemos guardar los cambios del dataframe')
st.write('Resultado del **dataframe editado**')

st.dataframe(df_edited, use_container_width=True)