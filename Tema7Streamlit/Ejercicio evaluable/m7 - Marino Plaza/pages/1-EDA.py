import streamlit as st
import joblib
import seaborn as sns
import pandas as pd 


st.set_page_config(
    page_title='EDAs', 
    page_icon=':bar_chart:'
)

st.title('Página 1 - EDAs')

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('Home.py')
        
st.header('1. Carga de datos')

df = sns.load_dataset('diamonds')

# Mostramos los datos
st.write('Ejemplo de los datos')
st.table(df.head())



st.header('2. Gráficos univariantes')




st.header('3. Gráficos bivariantes')




st.header('4. Gráficos multivariantes')