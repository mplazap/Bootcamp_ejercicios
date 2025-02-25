import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# Cargar datos
df = sns.load_dataset('penguins').dropna()
st.title('Graficos de Matplotlib, Seaborn y Plotly en Streamlit')
st.dataframe(df)


# Matplotlib
st.header('1. Gráficos de Matplotlib')
#Histograma
fig, ax = plt.subplots(figsize=(6,4))
ax.hist(df['flipper_length_mm'], bins=20, color='skyblue', edgecolor='black')
ax.set_title('Histograma de flipper length')
ax.set_xlabel('flipper_length_mm')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

# Boxplot
fig, ax = plt.subplots(figsize=(6,4))
ax.boxplot(x=df['bill_length_mm'], showmeans=True)
ax.set_title('Boxplot de Bill Length')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('Frecuencia')
st.pyplot(fig)

# Scatterplot
species_colors = {'Adelie': 'blue', 'Gentoo': 'green', 'Chinstrap': 'red'}
fig, ax = plt.subplots(figsize=(6,4))
for specie, color in species_colors.items():
    df_specie = df[df['species'] == specie]
    ax.scatter(x=df_specie['bill_length_mm'], y=df_specie['body_mass_g'], color=color, label=specie)
ax.set_title('Scatterplot - Relación entre bill_length_mm y body_mass_g')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('body_mass_g')
ax.legend()
ax.grid()
st.pyplot(fig)


# Seaborn
st.header('2- Graficos con Seaborn')

# Kdeplot, Rugplot e Histograma
fig, ax = plt.subplots(figsize=(6, 4))
sns.kdeplot(df, x='body_mass_g')
sns.rugplot(df, x='body_mass_g')
sns.histplot(df, x='body_mass_g')
st.pyplot(fig)

# Scatterplot
fig, ax = plt.subplots(figsize=(6, 4))
sns.scatterplot(df, x='bill_length_mm', y='body_mass_g', hue='species', palette='deep', ax=ax)
ax.set_title('Scatterplot - Relación entre bill_length_mm y body_mass_g')
ax.set_xlabel('bill_length_mm')
ax.set_ylabel('body_mass_g')
ax.legend()
ax.grid()
st.pyplot(fig)
# ax=ax si solo creamos una grafica y no necesitamos controlar lo sejes de manera explicita entoncers no hace falta
# ax=ax si queremos insertar la grafica en un eje especifico, cuando varios subplots dentro del mismo grafico podria hacer falta

# Heatmap (Correlaciones)
fig, ax = plt.subplots(figsize=(6, 4))
sns.heatmap(df.corr(numeric_only=True).round(2), annot=True, cmap='viridis')
ax.set_title('Heatmap - Correlaciones')
st.pyplot(fig)


# Plotly
st.header('3- Graficos con Plotly')

# GroupBy
df_grouped = df.groupby('species', as_index=False)['body_mass_g'].mean()
st.table(df_grouped)
fig = px.bar(df_grouped, x='species', y='body_mass_g', color='species', title='Peso medio por especie')
st.plotly_chart(fig)

# Scatterplot
fig = px.scatter(df, x='bill_length_mm', y='body_mass_g', color='species')
st.plotly_chart(fig)

fig = px.scatter(df, x='bill_length_mm', y='flipper_length_mm', color='species', size='body_mass_g', width=800, height=700)
st.plotly_chart(fig)

fig = px.scatter(df, x='bill_length_mm', y='flipper_length_mm', color='species', facet_col='sex')
st.plotly_chart(fig)