import streamlit as st
from streamlit_camera_input_live import camera_input_live

st.set_page_config(page_title="Easy Find - Radar", layout="centered")

st.title("🔍 Easy Find: Radar")

st.write("### Escaneá el código de barras")
# Este componente es el que mejor funciona en Android/iOS
image = camera_input_live()

if image:
    st.image(image, caption="Buscando código...", width=300)
    st.info("💡 En la versión final, aquí el AHG procesará la imagen automáticamente.")
    
    # Por ahora, para que puedas probar la búsqueda:
    manual_code = st.text_input("Confirmá el número del código:")
    
    if manual_code:
        st.success(f"✅ ¡Capturado!: {manual_code}")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("🔍 Google", f"https://www.google.com/search?q={manual_code}")
        with col2:
            st.link_button("🛍️ M. Libre", f"https://listado.mercadolibre.com.ar/{manual_code}")

st.divider()
st.caption("QAP - Modo Mobile Activo")
