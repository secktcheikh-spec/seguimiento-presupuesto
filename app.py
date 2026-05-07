import streamlit as st
import pandas as pd
from datetime import date
import smtplib
from email.mime.text import MIMEText

# Título
st.title("💰 Seguimiento de Presupuesto")

# 1. Campos de entrada
num_albaran = st.text_input("Número de albarán")
fecha = st.date_input("Fecha", date.today())
trabajador = st.text_input("Trabajador")
partida = st.selectbox("Categoría", ["Material Eléctrico", "Mecanismos", "Domótica", "Varios"])
gasto = st.number_input("Valor del albarán (€)", min_value=0.0)
comentarios = st.text_area("Comentarios")

st.markdown("---")

# 2. Botón de Registro Local
if st.button("💾 Registrar y Generar Excel"):
    if num_albaran and trabajador:
        datos = {"Albarán": [num_albaran], "Fecha": [fecha], "Trabajador": [trabajador], "Gasto": [gasto]}
        df = pd.DataFrame(datos)
        st.success("Registrado. Ahora puedes descargarlo.")
        st.download_button("📥 Descargar Excel", df.to_csv(index=False).encode('utf-8'), "presupuesto.csv")
    else:
        st.error("Faltan datos obligatorios.")

# 3. BOTÓN DE ENVIAR EMAIL (Esto es lo que te falta)
if st.button("📧 ENVIAR A LA PROFESORA"):
    if num_albaran and trabajador:
        try:
            # Cuerpo del mensaje
            mensaje_texto = f"""
            Nuevo informe de presupuesto:
            ----------------------------
            Trabajador: {trabajador}
            Albarán Nº: {num_albaran}
            Fecha: {fecha}
            Partida: {partida}
            Importe: {gasto}€
            Comentarios: {comentarios}
            """
            
            msg = MIMEText(mensaje_texto)
            msg['Subject'] = f"Albarán Obra - {trabajador}"
            msg['From'] = st.secrets["email"]["user"]
            msg['To'] = st.secrets["email"]["profesora"]

            # Conexión técnica
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(st.secrets["email"]["user"], st.secrets["email"]["password"])
            server.send_message(msg)
            server.quit()

            st.success("✅ ¡Correo enviado con éxito!")
        except Exception as e:
            st.error(f"Error al enviar: {e}")
    else:
        st.error("Rellena el nombre y el número de albarán primero.")
