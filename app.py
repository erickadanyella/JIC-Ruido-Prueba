import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Obtener la fecha de hoy en el formato del archivo (Año-Mes-Día)
hoy = datetime.now().strftime("%Y-%m-%d")

# 2. Construir la URL dinámica (Asegúrate de que la ruta sea idéntica a la de la imagen)
# Reemplaza 'Usuario' y 'Repo' con los datos reales de tu profesor
base_url = "https://raw.githubusercontent.com/AlejoBSmith/SmartCampus_UTP/main/Data/Monitoreo_de_Ruido/"
nombre_archivo = f"Monitoreo_de_Ruido_{hoy}.csv"
url_final = base_url + nombre_archivo

st.title("🛰️ Monitoreo de Ruido en Tiempo Real")
st.write(f"Consultando datos del día: {hoy}")

# 3. Intentar cargar los datos
try:
    df = pd.read_csv(url_final)
    
    # Mostrar el último registro
    ultimo_dato = df.iloc[-1]
    st.metric("Nivel de Ruido Actual", f"{ultimo_dato['decibelios']} dB")
    
    # Alerta visual
    if ultimo_dato['decibelios'] > 75:
        st.error("🚨 ALERTA: Ruido excesivo detectado.")
    else:
        st.success("✅ Ambiente tranquilo.")

except Exception as e:
    st.warning(f"Aún no hay datos registrados para hoy ({hoy}). Mostrando mensaje de espera...")