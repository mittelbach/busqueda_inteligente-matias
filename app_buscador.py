import streamlit as st
import motor_busqueda as motor 

# Configuración de página
st.set_page_config(page_title="Radar de Precios Mittelbach", layout="centered")

st.title("🌐 Centro de Mandos: Radar")
st.markdown("---")

# Entrada de Datos
with st.container():
    producto = st.text_input("¿Qué buscamos hoy, socio?", placeholder="Ej: Resina dental, BTC, XRP...")
    
    col1, col2 = st.columns(2)
    with col1:
        boton_disparar = st.button("🚀 Lanzar Radar", use_container_width=True)
    with col2:
        if st.button("🧹 Limpiar", use_container_width=True):
            st.rerun()

if producto:
    p_low = producto.lower()
    p_plus = producto.replace(' ', '+')
    p_dash = producto.replace(' ', '-')
    
    # URL de Google Shopping para el disparo automático
    url_google_auto = f"https://www.google.com.ar/search?q=precio+{p_plus}&tbm=shop"
    
    # --- ANÁLISIS TÁCTICO ---
    if any(x in p_low for x in ["btc", "bitcoin", "crypto", "xrp", "eth"]):
        st.warning("₿ **Activo de Resguardo:** Analizando mercados. Ojo con la entropía.")
    elif any(x in p_low for x in ["diente", "dental", "resina", "protesis"]):
        st.success("🦷 **Insumo Especializado:** Nodo internacional sugerido: Tiendamia.")
    else:
        st.info("📊 **Análisis General:** Escaneando nodos estándar.")

    # DISPARADOR AUTOMÁTICO (Simula el comportamiento de la versión CSV)
    if boton_disparar:
        # Abrir Google Shopping automáticamente mediante JS
        js = f'window.open("{url_google_auto}", "_blank").focus();'
        st.components.v1.html(f'<script>{js}</script>', height=0)
        st.toast(f"Escaneando {producto} en Google Shopping...", icon='🚀')

    st.markdown("---")
    st.subheader(f"🎯 Nodos para: {producto}")
    
    urls = {
        "Mercado Libre": f"https://listado.mercadolibre.com.ar/{p_dash}",
        "Tiendamia": f"https://tiendamia.com/ar/search?amz={p_plus}",
        "AliExpress": f"https://es.aliexpress.com/w/wholesale-{p_dash}.html",
        "Amazon": f"https://www.amazon.com/s?k={p_plus}",
        "eBay": f"https://www.ebay.com/sch/i.html?_nkw={p_plus}",
        "Temu": f"https://www.temu.com/search_result.html?search_key={p_plus}"
    }

    # PANEL DE BOTONES (v3.4 con Temu)
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🇦🇷 Mercado Libre", urls["Mercado Libre"], use_container_width=True)
        st.link_button("✈️ Tiendamia", urls["Tiendamia"], use_container_width=True)
        st.link_button("🧡 Temu", urls["Temu"], use_container_width=True)
    with c2:
        st.link_button("🇨🇳 AliExpress", urls["AliExpress"], use_container_width=True)
        st.link_button("📦 Amazon", urls["Amazon"], use_container_width=True)
        st.link_button("🛒 eBay", urls["eBay"], use_container_width=True)

st.markdown("---")
st.caption("QAP - Protocolo SMLabs v3.4 | Radar Automático Activado")
