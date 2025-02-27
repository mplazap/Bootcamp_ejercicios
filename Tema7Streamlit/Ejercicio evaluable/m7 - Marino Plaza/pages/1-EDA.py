import streamlit as st
import joblib
import seaborn as sns
import pandas as pd
import numpy as np 
import plotly.express as px


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

# Selección de variables
col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribución de variables numéricas")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    selected_numeric = st.selectbox("Selecciona una variable numérica", numeric_cols)
    
    fig = px.histogram(df, x=selected_numeric, marginal="box", 
                    title=f"Distribución de {selected_numeric}")
    st.plotly_chart(fig, use_container_width=True)
    
    # Estadísticas de la variable seleccionada
    stats = df[selected_numeric].describe().to_frame().T
    st.dataframe(stats)

with col2:
    st.subheader("Distribución de variables categóricas")
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
    if cat_cols:
        selected_cat = st.selectbox("Selecciona una variable categórica", cat_cols)
        
        # Contar valores
        value_counts = df[selected_cat].value_counts().reset_index()
        value_counts.columns = [selected_cat, 'Count']
        
        fig = px.pie(value_counts, values='Count', names=selected_cat, 
                    title=f"Distribución de {selected_cat}")
        st.plotly_chart(fig, use_container_width=True)
        
        # Tabla de frecuencias
        st.dataframe(value_counts)
    else:
        st.info("No se encontraron variables categóricas en el dataset")


st.header('3. Gráficos bivariantes')




st.header('4. Gráficos multivariantes')