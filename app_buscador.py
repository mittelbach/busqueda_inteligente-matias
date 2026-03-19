import streamlit as st

st.set_page_config(page_title="Find Easy - Radar", layout="centered")

st.title("🔍 Find Easy: Radar")

# Método de alta compatibilidad para celulares
# Si st.camera_input falla por permisos, este botón permite subir la foto
foto = st.camera_input("Sacale una foto al código de barras")

if foto:
    st.image(foto, caption="Imagen para procesar", width=300)
    st.success("✅ Foto capturada.")
    
    # Campo para el código (esto luego lo hará el AHG solo)
    ean = st.text_input("Ingresá el número del código:")
    
    if ean:
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("🔍 Google", f"https://www.google.com/search?q={ean}", use_container_width=True)
        with col2:
            st.link_button("🛍️ M. Libre", f"https://listado.mercadolibre.com.ar/{ean}", use_container_width=True)

st.divider()
st.info("💡 Si la cámara no abre: tocá el ícono del CANDADO al lado de la URL y activá el permiso de Cámara.")
