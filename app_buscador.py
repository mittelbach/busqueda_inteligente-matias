import streamlit as st
import motor_busqueda as motor 

# Configuración de página para móviles
st.set_page_config(page_title="Radar de Precios", layout="centered")

st.title("🌐 Centro de Mandos: Radar")
st.markdown("---")

# Contenedor de entrada
with st.container():
    producto = st.text_input("Ingresá el producto:", placeholder="Ej: Resina dental, BTC...")
    
    col1, col2 = st.columns(2)
    with col1:
        boton_disparar = st.button("🚀 Lanzar Radar")
    with col2:
        if st.button("🧹 Nueva Búsqueda"):
            st.rerun()

if producto:
    p_low = producto.lower()
    
    # --- ANÁLISIS TÁCTICO (HEURÍSTICA) ---
    if any(x in p_low for x in ["btc", "bitcoin", "crypto", "xrp", "eth"]):
        st.warning("₿ **Activo de Resguardo:** Escaneando válvulas de escape. Revisar liquidez y volatilidad.")
    elif any(x in p_low for x in ["diente", "dental", "resina", "protesis"]):
        st.success("🦷 **Insumo Especializado:** Análisis de costo activo. Priorizar nodos internacionales.")
    else:
        st.info("📊 **Análisis General:** Búsqueda estándar activada.")

    st.markdown("---")
    st.subheader(f"🎯 Nodos para: {producto}")
    
    # Preparación de URLs
    p_plus = producto.replace(' ', '+')
    p_dash = producto.replace(' ', '-')
    
    urls = {
        "Mercado Libre": f"https://listado.mercadolibre.com.ar/{p_dash}",
        "Google Shopping": f"https://www.google.com.ar/search?q=precio+{p_plus}&tbm=shop",
        "Tiendamia": f"https://tiendamia.com/ar/search?amz={p_plus}",
        "AliExpress": f"https://es.aliexpress.com/w/wholesale-{p_dash}.html",
        "Amazon": f"https://www.amazon.com/s?k={p_plus}",
        "eBay": f"https://www.ebay.com/sch/i.html?_nkw={p_plus}"
    }

    # PANEL DE NODOS (Botones táctiles)
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🇦🇷 Mercado Libre", urls["Mercado Libre"], use_container_width=True)
        st.link_button("🔍 Google Shopping", urls["Google Shopping"], use_container_width=True)
        st.link_button("✈️ Tiendamia", urls["Tiendamia"], use_container_width=True)
    with c2:
        st.link_button("🇨🇳 AliExpress", urls["AliExpress"], use_container_width=True)
        st.link_button("📦 Amazon", urls["Amazon"], use_container_width=True)
        st.link_button("🛒 eBay", urls["eBay"], use_container_width=True)

    if boton_disparar:
        st.toast(f"Escaneando nodos para {producto}...", icon='🚀')

st.markdown("---")
st.caption("QAP - Radar en la Nube v3.3")
