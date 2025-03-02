import streamlit as st
import joblib

@st.cache_resource
def load_scikit_model():
    return joblib.load('pipeline.joblib')

st.title('Regresion Tip')

model = load_scikit_model()

st.header('Introduce los datos para la predicción')



