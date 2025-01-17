# generar_pdf.py

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Título
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Guía Básica de Pandas", border=False, ln=1, align="C")
        self.ln(5)  # Espacio extra

    def footer(self):
        # Pie de página
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        page_num = f"Página {self.page_no()}"
        self.cell(0, 10, page_num, 0, 0, "C")


def generar_pdf():
    # Contenido de la guía (en español)
    contenido = [
        "Introducción",
        "Pandas es una biblioteca de Python especializada en la "
        "manipulación y análisis de datos. Proporciona estructuras "
        "de datos (principalmente Series y DataFrame) y múltiples "
        "funciones que permiten leer, limpiar, transformar, agrupar "
        "y exportar información de manera sencilla y eficiente.",

        "1. Lectura de Datos",
        "1.1 pd.read_csv:\n"
        "- Descripción: Carga datos desde un archivo CSV (u otros separados "
        "por delimitadores) a un DataFrame.\n"
        "- Uso Típico:\n"
        "    import pandas as pd\n"
        "    df = pd.read_csv('data.csv', delimiter=',')\n"
        "- Parámetros frecuentes:\n"
        "    delimiter: Define el separador (default ',')\n"
        "    header: Indica la fila de nombres de columnas (default 0)\n"
        "    encoding: Codificación (por ej. 'utf-8')",

        "1.2 pd.read_excel:\n"
        "- Descripción: Carga datos desde un archivo Excel (.xls o .xlsx).\n"
        "- Uso Típico:\n"
        "    df_excel = pd.read_excel('data.xlsx', sheet_name='Hoja1')\n"
        "- Parámetros frecuentes:\n"
        "    sheet_name: Nombre o índice de la hoja\n"
        "    header: Indica la fila de nombres de columnas\n"
        "    usecols: Columnas específicas a leer",

        "2. Exploración de Datos",
        "2.1 df.head(): Muestra las primeras filas del DataFrame.\n"
        "    df.head(5)",
        "2.2 df.tail(): Muestra las últimas filas.\n"
        "    df.tail(3)",
        "2.3 df.info(): Proporciona un resumen de las columnas, tipos de datos y nulos.\n"
        "    df.info()",
        "2.4 df.describe(): Estadísticas descriptivas de columnas numéricas.\n"
        "    df.describe()",
        "2.5 df.shape: Retorna (num_filas, num_columnas).\n"
        "    num_filas, num_cols = df.shape",
        "2.6 df.columns: Lista los nombres de columnas.\n"
        "    print(df.columns)",

        "3. Limpieza de Datos",
        "3.1 df.dropna(): Elimina filas o columnas con valores nulos.\n"
        "    df_sin_nulos = df.dropna(axis=0)",
        "3.2 df.fillna(): Rellena los valores nulos.\n"
        "    df_relleno = df.fillna(0)",
        "3.3 df.rename(): Cambia el nombre de columnas o filas.\n"
        "    df_renombrado = df.rename(columns={'old': 'new'})",

        "4. Selección e Indexación",
        "4.1 df.loc: Selección con etiquetas de filas y columnas.\n"
        "    df.loc['A', 'edad']\n"
        "    df.loc[['A','B'], ['edad','salario']]",
        "4.2 df.iloc: Selección basada en índices enteros.\n"
        "    df.iloc[0, 0]\n"
        "    df.iloc[0:2, 0:3]",

        "5. Agrupación y Combinación de Datos",
        "5.1 df.groupby(): Agrupa filas y permite funciones de agregación.\n"
        "    df.groupby('departamento')['salario'].mean()",
        "5.2 df.merge(): Combina DataFrames basados en columnas.\n"
        "    df_merged = pd.merge(df1, df2, on='id', how='inner')",
        "5.3 pd.concat(): Concatena DataFrames por filas o columnas.\n"
        "    df_concat = pd.concat([df1, df2], axis=0)",

        "6. Exportar Datos",
        "6.1 df.to_csv(): Exporta un DataFrame a un archivo CSV.\n"
        "    df.to_csv('resultado.csv', index=False)",
        "6.2 df.to_excel(): Exporta a un archivo de Excel.\n"
        "    df.to_excel('resultado.xlsx', sheet_name='Hoja1', index=False)",

        "Conclusión",
        "Esta guía cubre funciones y métodos esenciales de Pandas: "
        "lectura, limpieza, exploración, transformación y exportación de datos. "
        "Para más información, visita la documentación oficial:\n"
        "https://pandas.pydata.org/docs"
    ]

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Agregamos la primera página
    pdf.add_page()

    # Fuente general para el texto
    pdf.set_font("Arial", size=11)

    # Añadir el contenido al PDF usando multi_cell para manejar saltos de línea
    for seccion in contenido:
        pdf.multi_cell(0, 7, seccion, 0, 1)
        pdf.ln(2)

    # Guardar el PDF
    pdf.output("Guia_Basica_Pandas.pdf")
    print("PDF generado con éxito: Guia_Basica_Pandas.pdf")


if __name__ == "__main__":
    generar_pdf()
