import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Cargamos el modelo entrenado y el LabelEncoder para `cut`
model = joblib.load("models/pipeline_clasificacion.joblib")
label_encoder = joblib.load("models/label_encoder_cut.joblib")

# Botones de navegacion
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button('Volver a inicio'): 
        st.switch_page('Home.py')
with col2:
    if st.button('Ir a EDAs'):
        st.switch_page('pages/1-EDA.py')
    
with col3:
    if st.button('Ir a Predicción'):
        st.switch_page('pages/2-Regresion.py')
    
# Título de la Aplicación
st.title("💎 Clasificación de Diamantes 💎")
st.write("Introduce las características del diamante para predecir su categoría")

# Formulario para ingresar los datos
with st.form("diamond_form"):
    carat = st.number_input("Carat (Peso)", min_value=0.1, max_value=5.0, step=0.1)
    depth = st.number_input("Depth (%)", min_value=50.0, max_value=75.0, step=0.1)
    table = st.number_input("Table (%)", min_value=50.0, max_value=75.0, step=0.1)
    x = st.number_input("X (Longitud en mm)", min_value=0.1, max_value=10.0, step=0.1)
    y = st.number_input("Y (Ancho en mm)", min_value=0.1, max_value=10.0, step=0.1)
    z = st.number_input("Z (Profundidad en mm)", min_value=0.1, max_value=10.0, step=0.1)

    # Entradas para variables categóricas
    color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
    clarity = st.selectbox("Clarity (Claridad)", ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"])

    submit = st.form_submit_button("Predecir categoria")

# Procesamos la predicción cuando se presione el botón
if submit:
    # Creamos Dataframe con las características ingresadas
    data = pd.DataFrame({
        "carat": [carat],
        "depth": [depth],
        "table": [table],
        "x": [x],
        "y": [y],
        "z": [z],
        "color": [color],
        "clarity": [clarity]
    })

    # Realizamos la predicción
    prediction = model.predict(data)
    predicted_cut = label_encoder.inverse_transform([prediction[0]])[0]  # Convertimos el número a la categoría real
    
    # Mostramos resultado con st.metric()
    st.metric(label="Categoría teorica", value=predicted_cut)