import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Cargamos el modelo entrenado
model = joblib.load("models/pipeline_regresion.joblib")

# Botones de navegacion
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button('Volver a inicio'): 
        st.switch_page('Home.py')
with col2:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1-EDA.py')
    
with col3:
    if st.button('Ir a Clasificación'):
        st.switch_page('pages/3-Clasificacion.py')

# Creamos el formulario para introducir datos
st.markdown(
    """
    <div style="display: flex; justify-content: center;">
        <h1>💎 💎</h1>
    </div>
    """,
    unsafe_allow_html=True
)

st.title("Predicción del Precio de Diamantes")
st.write("Introduce las características del diamante para predecir su precio.")

# Entradas para las características
carat = st.number_input("Carat (Peso)", min_value=0.1, max_value=5.0, step=0.1)
depth = st.number_input("Depth (%)", min_value=50.0, max_value=75.0, step=0.1)
table = st.number_input("Table (%)", min_value=50.0, max_value=75.0, step=0.1)
x = st.number_input("X (Longitud en mm)", min_value=0.1, max_value=10.0, step=0.1)
y = st.number_input("Y (Ancho en mm)", min_value=0.1, max_value=10.0, step=0.1)
z = st.number_input("Z (Profundidad en mm)", min_value=0.1, max_value=10.0, step=0.1)

# Entradas para variables categóricas
cut = st.selectbox("Cut (Corte)", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox("Clarity (Claridad)", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

# Convertimos las entradas en un Dataframe
data = pd.DataFrame({
    "carat": [carat],
    "depth": [depth],
    "table": [table],
    "x": [x],
    "y": [y],
    "z": [z],
    "cut": [cut],
    "color": [color],
    "clarity": [clarity]
})

# Hacemos la predicción
if st.button("Predecir Precio"):
    prediction = model.predict(data)
    
    # Mostramos la prediccion
    st.metric(label="Precio aproximado ($)", value=f"${prediction[0]:,.2f}")
