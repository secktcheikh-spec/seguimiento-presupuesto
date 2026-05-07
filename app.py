import streamlit as st
import pandas as pd
from datetime import date

# Título de la aplicación
st.title("💰 Seguimiento de Presupuesto")

# 1. Campos obligatorios según el documento
num_albaran = st.text_input("Número de albarán") [cite: 67]
fecha = st.date_input("Fecha", date.today()) [cite: 68]
trabajador = st.text_input("Trabajador") [cite: 69]

# 2. Categorías y Gastos
partidas = ["Material Eléctrico", "Mecanismos", "Domótica", "Varios"]
partida_seleccionada = st.selectbox("Categoría del presupuesto", partidas) [cite: 70]
valor_gasto = st.number_input("Valor del albarán (€)", min_value=0.0, step=0.01) [cite: 71]

# 3. Comentarios y Nota Extra (Fotos)
comentarios = st.text_area("Comentarios") [cite: 72]
foto = st.file_uploader("Subir fotos albarán (Nota Extra)", type=["jpg", "png", "jpeg"]) [cite: 73]

# 4. Botón para procesar datos
if st.button("Registrar y Generar Excel"):
    if num_albaran and trabajador:
        # Usamos Pandas para organizar los datos (Requisito RA3) [cite: 4]
        datos = {
            "Albarán": [num_albaran],
            "Fecha": [fecha],
            "Trabajador": [trabajador],
            "Partida": [partida_seleccionada],
            "Gasto (€)": [valor_gasto],
            "Comentarios": [comentarios]
        }
        df = pd.DataFrame(datos)
        
        # Crear el Excel para descargar (Requisito RA4) [cite: 4]
        st.success("Gasto registrado correctamente.")
        st.table(df)
        
        # Convertir a CSV/Excel para descarga
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Descargar Registro de Presupuesto", csv, "presupuesto.csv", "text/csv")
    else:
        st.error("Faltan datos obligatorios (Albarán o Trabajador)")
