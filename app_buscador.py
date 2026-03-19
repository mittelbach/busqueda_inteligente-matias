import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner

# Configuración Maserati
st.set_page_config(page_title="Easy Find - Radar", layout="centered")

st.title("🔍 Easy Find: Radar de Precios")
st.write("Escaneá el código de barras con la cámara de tu Motorola o Laptop.")

# --- EL ESCÁNER (La pieza clave) ---
# Esto abre la cámara y nos da el número directamente
codigo_detectado = qrcode_scanner(key='scanner')

# --- LÓGICA DE RESULTADOS ---
if codigo_detectado:
    st.success(f"📦 Producto Identificado: {codigo_detectado}")
    
    # Creamos los botones de búsqueda neguentrópica
    col1, col2 = st.columns(2)
    
    with col1:
        url_google = f"https://www.google.com/search?q={codigo_detectado}"
        st.link_button("🔍 Buscar en Google", url_google, use_container_width=True)
        
    with col2:
        url_ml = f"https://listado.mercadolibre.com.ar/{codigo_detectado}"
        st.link_button("🛍️ Ver en Mercado Libre", url_ml, use_container_width=True)

    # Espacio para tu algoritmo AHG
    st.info("💡 Consejo: Compará el precio con el historial para evitar la entropía inflacionaria.")

else:
    st.info("A la espera de un código... Apuntá la cámara al código de barras.")

st.divider()
st.caption("QAP - Sistema Easy Find v1.0 | Protocolo AHG")
