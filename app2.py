import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configuración de la fecha y URL base
hoy = datetime.now().strftime("%Y-%m-%d")

# URL base exacta según tus capturas de GitHub
base_url = "https://raw.githubusercontent.com/AlejoBSmith/SmartCampus_UTP/main/Data/Monitoreo_de_Ruido/"
nombre_archivo = f"Monitoreo_de_Ruido_{hoy}.csv"
url_final = base_url + nombre_archivo

st.set_page_config(page_title="Monitor de Ruido UTP", page_icon="🔊")
st.title("🛰️ Monitoreo de Ruido en Tiempo Real")
st.write(f"Consultando datos del campus: **{hoy}**")

# 2. Intento de carga de datos
try:
    # Leemos el CSV directamente desde el Raw de GitHub
    df = pd.read_csv(url_final)
    
    # Obtenemos el último registro (la fila de hasta abajo)
    ultimo_dato = df.iloc[-1]
    
    # Extraemos los valores usando los nombres exactos de tus imágenes
    nivel_ruido = ultimo_dato['laeq_global_dB']
    ubicacion = ultimo_dato['deviceName']
    hora_lectura = ultimo_dato['time']

    # 3. Interfaz Visual
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(label="Nivel de Ruido Actual", value=f"{nivel_ruido:.2f} dB")
    
    with col2:
        st.info(f"**Ubicación:** {ubicacion}\n\n**Última actualización:** {hora_lectura}")

    # Semáforo de alerta (Lógica de ingeniería)
    if nivel_ruido > 75:
        st.error(f"🚨 **ALERTA CRÍTICA:** Ruido excesivo detectado en {ubicacion}. Se recomienda intervención.")
    elif nivel_ruido > 55:
        st.warning(f"⚠️ **AVISO:** El nivel de ruido en {ubicacion} está por encima de lo recomendado para áreas de estudio.")
    else:
        st.success(f"✅ **Ambiente Óptimo:** Los niveles en {ubicacion} son adecuados.")

    # Extra: Una pequeña gráfica de los últimos 20 datos para que se vea más profesional
    st.subheader("Tendencia reciente (últimas lecturas)")
    st.line_chart(df['laeq_global_dB'].tail(20))

except Exception as e:
    st.warning(f"Esperando nuevos datos del sensor para el día de hoy ({hoy})...")
    st.info("Nota: Si el sensor aún no ha realizado la primera transmisión del día, esta pantalla se actualizará automáticamente en la siguiente lectura.")