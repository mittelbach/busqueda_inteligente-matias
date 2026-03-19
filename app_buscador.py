import streamlit as st
from streamlit_qrcode_scanner import qrcode_scanner

st.set_page_config(page_title="Easy Find - Radar", layout="centered")

st.title("🔍 Easy Find: Radar de Precios")

# Instrucción clara para el usuario
st.warning("⚠️ Si no ves la cámara, asegúrate de dar 'Permitir' en la ventana emergente del navegador.")

# El escáner con un pequeño retraso para asegurar carga de hardware
codigo_detectado = qrcode_scanner(key='scanner')

if codigo_detectado:
    st.success(f"📦 Producto: {codigo_detectado}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("🔍 Google", f"https://www.google.com/search?q={codigo_detectado}")
    with col2:
        st.link_button("🛍️ M. Libre", f"https://listado.mercadolibre.com.ar/{codigo_detectado}")
else:
    st.info("A la espera de un código... Apuntá la cámara al código de barras.")
