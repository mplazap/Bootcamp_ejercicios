import streamlit as st


# Columnas
st.title('Elementos para layout y estructura')
st.header('1. Columnas')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('Contenido de la primera columna')
    st.image('https://placehold.co/100x200', caption='Imagen 100x200')
with col2:
    st.write('Contenido de la segunda columna')
    st.image('https://placehold.co/100x250', caption='Imagen 100x250')
    
with col3:
    st.write('Contenido de la tercera columna')
    st.image('https://placehold.co/100x300', caption='Imagen 100x300')


# Tabs (Pestañas)
st.header('2. tabs')
tab1, tab2, tab3 = st.tabs(['EDA', 'Regresión', 'Clasificación'])

with tab1:
    st.html('<img src="https://placehold.co/600x200" style="text-align:center;">')
    # st.write('Contenido de la primera columna')
    # st.image('https://placehold.co/600x250', caption='Imagen 100x200')

with tab2:
    # st.write('Contenido de la segunda columna')
    st.image('https://placehold.co/600x250', caption='Imagen 100x250')
    
with tab3:
    # st.write('Contenido de la tercera columna')
    st.image('https://placehold.co/600x300', caption='Imagen 100x300')


# Expander (desplegable como el de preguntas frecuentes)


# Containers
st.header('4. container')
container1 = st.container()
container1.write('Esto es un texto')
container1.image('https://placehold.co/600x200', caption='Imagen 600x200')
container1.write('Esto es otro texto')


container2 = st.container()
container2.write('Esto es un texto')
container2.image('https://placehold.co/600x200', caption='Imagen 600x200')
container2.write('Esto es otro texto')

# Sidebar (Barra lateral)
st.header('5. sidebar')
nombre = st.sidebar.text_input('Introduce tu nombre')

if nombre:
    st.sidebar.success(f'Tu nombre es {nombre}')