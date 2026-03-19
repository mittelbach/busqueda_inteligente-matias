import streamlit as st

st.set_page_config(page_title="Find Easy - Radar", layout="centered")

st.title("🔍 Find Easy: Radar")

st.write("### Escaneá el producto")
# Componente nativo: el más estable para celulares
foto_producto = st.camera_input("Apuntá al código de barras")

if foto_producto:
    # Aquí es donde el AHG entraría a procesar la imagen
    st.success("✅ Imagen capturada con éxito.")
    
    # Simulación de detección para que el radar funcione ya mismo
    ean_manual = st.text_input("Confirmá el número del código (EAN):")
    
    if ean_manual:
        st.divider()
        st.write(f"### 🛡️ Resultados para: {ean_manual}")
        
        col1, col2 = st.columns(2)
        with col1:
            url_google = f"https://www.google.com/search?q={ean_manual}"
            st.link_button("🔍 Buscar en Google", url_google, use_container_width=True)
        with col2:
            url_ml = f"https://listado.mercadolibre.com.ar/{ean_manual}"
            st.link_button("🛍️ Mercado Libre", url_ml, use_container_width=True)

st.divider()
st.caption("QAP - Protocolo Homeostasis Global v1.2")
