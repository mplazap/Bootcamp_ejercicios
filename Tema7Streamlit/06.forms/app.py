import streamlit as st

st.title("Ejemplo de formulario de Streamlit")

# Creamos un formulario llamado "mi_formulario"
with st.form("mi_formulario"):
    st.write("Por favor, completa los siguientes campos:")
    
    # Texto de una sola línea
    nombre = st.text_input("Nombre")
    
    # Texto de varias líneas
    descripcion = st.text_area("Descripción")
    
    # Número (con límites y paso específico)
    edad = st.number_input("Edad", min_value=0, max_value=120, value=25, step=1)
    
    # Control deslizable (slider)
    peso = st.slider("Peso (kg)", 0, 150, 70)
    
    # Selección de una opción entre varias (selectbox)
    genero = st.selectbox("Género", ["Masculino", "Femenino", "Otro"])
    
    # Selección múltiple (multiselect)
    intereses = st.multiselect("Intereses", 
                               ["Avistamiento de aves", "Fotografía", "Programación", "Arte", "Lectura"])
    
    # Selección de radio
    nivel_experiencia = st.radio("Nivel de experiencia en Python", 
                                 ["Principiante", "Intermedio", "Avanzado"])
    
    # Casilla de verificación (checkbox)
    aceptar_terminos = st.checkbox("Acepto los términos y condiciones")
    
    # Selección de fecha
    fecha_nacimiento = st.date_input("Fecha de nacimiento")
    
    # Selección de hora
    hora_cita = st.time_input("Hora de cita")
    
    # Selector de color
    color_favorito = st.color_picker("Elige tu color favorito", "#FFFFFF")
    
    # Subida de archivos
    archivo_subido = st.file_uploader("Sube un archivo", type=["png", "jpg", "pdf"])

    # Botón para enviar el formulario
    boton_enviar = st.form_submit_button("Enviar")

    # Si el usuario hace clic en el botón "Enviar", mostramos los datos introducidos
    if boton_enviar:
        st.write("## Datos introducidos:")
        st.write(f"- **Nombre:** {nombre}")
        st.write(f"- **Descripción:** {descripcion}")
        st.write(f"- **Edad:** {edad}")
        st.write(f"- **Peso:** {peso} kg")
        st.write(f"- **Género:** {genero}")
        st.write(f"- **Intereses:** {intereses}")
        st.write(f"- **Nivel de experiencia:** {nivel_experiencia}")
        st.write(f"- **Acepta términos:** {aceptar_terminos}")
        st.write(f"- **Fecha de nacimiento:** {fecha_nacimiento}")
        st.write(f"- **Hora de cita:** {hora_cita}")
        st.write(f"- **Color favorito:** {color_favorito}")

        # Validamos si hay un archivo subido
        if archivo_subido is not None:
            st.write("Archivo subido con éxito:")
            st.write(f"- Nombre del archivo: {archivo_subido.name}")
        else:
            st.write("No se subió ningún archivo.")