import streamlit as st

# API reference de elementos de texto en Streamlit

st.title('Elementos de texto en Streamlit')
st.header('Esto es un encabezado')
st.subheader('Esto es un sub-encabezado')

st.write('Texto normal con la la funcion write (**Admite formateo**)')
st.text('Texto normal con la funcion text (**NO admite formateo**)')

st.markdown('''
Este parrafo usa **Markdown** con **negritas** y *cursiva* y enlaces como [este](https://streamlit.io).

Con saltos de linea.

Otro salto de linea.

Estamo susando `st.markdown`.

lista de cosas:
- Cosa 1
- Cosa 2
- Cosa 3
            ''')

st.caption('Lo de arriba es una prueba de markdown. Esto es para poner notas al pie de la pagina o algun comentario')


st.code('''
def saludar(name):
    print(f'Hola {name}')    
        ''', language='python')

st.header('Fórmulas matemátixas con Latex')
st.latex(r"""
y = \phi\biggl(\sum_{i=1}^{n} w_i x_i + b\biggr)
""")

st.header('Imprimir Help')
st.help(st.header) # Le pasamos cualquier metodo o clase de la que queramos ver al ayuda

st.html(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>"
)

st.html("""
<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>
<p><span style='color:green;'>Oops</span>!</p>
"""
)
st.markdown(
    "<p><span style='text-decoration: line-through double red;'>Oops</span>!</p>",
    unsafe_allow_html=True
)