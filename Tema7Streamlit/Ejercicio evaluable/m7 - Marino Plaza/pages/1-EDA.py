import streamlit as st
import joblib
import seaborn as sns
import pandas as pd
import numpy as np 
import plotly.express as px
import matplotlib.pyplot as plt
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(
    page_title='EDAs', 
    page_icon=':bar_chart:'
)

st.title('Página 1 - EDAs')
st.subheader("Análisis Exploratorio de Datos")

if st.button('Volver a inicio'): # opcional poder volver a inicio
    st.switch_page('Home.py')
        

st.markdown("<h2 style='text-decoration: underline;'>1. Carga de datos</h2>", unsafe_allow_html=True)
df = sns.load_dataset('diamonds')

# Mostramos los datos
st.write('Ejemplo de los datos')
st.table(df.head())

st.divider()

st.markdown("<h2 style='text-decoration: underline;'>2. Gráficos univariantes</h2>", unsafe_allow_html=True)
st.subheader("Gráficos para colúmnas numéricas")

# Filtros Globales en la Barra Lateral
st.sidebar.subheader("Filtro Global")
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
st.write('Selecciona las columnas a mostrar en el filtro del Sidebar ')

st.divider()

# Seleccionamos una columna numerica
if numeric_cols:
    selected_numeric = st.sidebar.selectbox("Selecciona una colúmna numérica", numeric_cols)
else:
    selected_numeric = None

# Seleccionamos una columna categorica
if categorical_cols:
    selected_categorical = st.sidebar.selectbox("Selecciona una colúmna categórica", categorical_cols)
else:
    selected_categorical = None

# Creamos los graficos para Variables Numericas
if selected_numeric:
    st.subheader(f"Análisis de {selected_numeric}")

    # Histograma con Plotly
    fig_hist = px.histogram(df, x=selected_numeric, marginal="box",
                            title=f"Distribución de {selected_numeric}",
                            nbins=30)
    st.plotly_chart(fig_hist, use_container_width=True)

    # KDE Plot con Seaborn
    st.subheader(f"Densidad de {selected_numeric} (KDE Plot)")
    fig_kde, ax_kde = plt.subplots(figsize=(8, 4))
    sns.kdeplot(df[selected_numeric], fill=True, color="blue", alpha=0.6, ax=ax_kde)
    ax_kde.set_title(f"Distribución KDE de {selected_numeric}")
    st.pyplot(fig_kde)

    # Boxplot con Seaborn
    st.subheader(f"Boxplot de {selected_numeric}")
    fig_box, ax_box = plt.subplots(figsize=(8, 4))
    sns.boxplot(x=df[selected_numeric], color="orange", ax=ax_box)
    ax_box.set_title(f"Boxplot de {selected_numeric}")
    st.pyplot(fig_box)

st.divider()

# Creamos los graficos para columnas categoricas
st.subheader("Gráficos para colúmnas categóricas")

if selected_categorical:
    st.subheader(f"Distribución de {selected_categorical}")

    # Barplot con Seaborn
    fig_bar, ax_bar = plt.subplots(figsize=(8, 4))
    sns.countplot(x=df[selected_categorical], palette="pastel", ax=ax_bar)
    ax_bar.set_title(f"Frecuencia de {selected_categorical}")
    st.pyplot(fig_bar)

    # Pie Chart con Plotly
    value_counts = df[selected_categorical].value_counts().reset_index()
    value_counts.columns = [selected_categorical, 'Count']

    fig_pie = px.pie(value_counts, values='Count', names=selected_categorical, 
                      title=f"Distribución de {selected_categorical}")
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# Grafico bivariante
st.markdown("<h2 style='text-decoration: underline;'>3. Gráficos bivariantes</h2>", unsafe_allow_html=True)

# Creamos variables para `x` y `y` usando filtros del sidebar
col_x = st.sidebar.selectbox("Variable en Eje X", numeric_cols, index=0)
col_y = st.sidebar.selectbox("Variable en Eje Y", numeric_cols, index=1)

# Usamos las columnas categoricas como color
color_category = st.sidebar.selectbox("Colorear por Categoría", ["None"] + categorical_cols)

# Creamos scatterplot con Plotly
fig_scatter = px.scatter(df, x=col_x, y=col_y, 
                         color=df[color_category] if color_category != "None" else None,
                         title=f"Scatterplot: {col_x} vs {col_y}",
                         opacity=0.7, size_max=10)

# Mostramos el gráfico
st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

st.markdown("<h2 style='text-decoration: underline;'>4. Gráficos multivariantes</h2>", unsafe_allow_html=True)

