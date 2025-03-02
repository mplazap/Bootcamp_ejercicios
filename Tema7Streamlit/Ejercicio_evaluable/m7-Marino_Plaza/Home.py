import streamlit as st


st.set_page_config(
    page_title='Home', 
    page_icon=':house:'
)

st.title('Aplicación para la visualización de EDAs, regresión y clasificación del Dataset Diamonds')

st.image("images/portada.jpeg", use_container_width=True)
st.write("""
Bienvenido a mi aplicación para visualización de EDAs, regresión y clasificación, una herramienta interactiva desarrollada con Streamlit como parte del proyecto final de nuestro Bootcamp de Data Science.

¿Qué hace esta aplicación?

🔍  Exploración de Datos (EDA):
 
Analiza visualmente las características de los diamantes con gráficos y estadísticas descriptivas.

📈  Regresión: 

Predice el precio de un diamante según sus atributos como quilates, color y claridad.

📋  Clasificación: 

Determina la calidad del diamante en categorías utilizando modelos de Machine Learning.

🛠️ Tecnologías utilizadas:

Esta aplicación ha sido creada con Python, utilizando bibliotecas como pandas, scikit-learn, seaborn y Streamlit, entre otras, para el análisis y visualización de datos.

Explora, analiza y descubre información valiosa sobre el mundo de los diamantes con solo unos clics. ¡Esperamos que disfrutes la experiencia!
""")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1-EDA.py')
        
with col2:
    if st.button('Ir a Predicción'):
        st.switch_page('pages/2-Regresion.py')
        
with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3-Clasificacion.py')