import streamlit as st
import motor_busqueda as motor 

st.set_page_config(page_title="Radar Mittelbach v7.2", layout="centered")

st.title("🌐 Centro de Mandos: SMLabs")

modo = st.radio("Objetivo del Radar:", ["🛒 Consumo & Global", "📜 Búsqueda de Antepasados"], horizontal=True)

st.markdown("---")

if modo == "🛒 Consumo & Global":
    producto = st.text_input("¿Qué buscamos hoy, socio?", placeholder="Ej: Addiesdive, Laptop...")
    
    if producto:
        p_plus = producto.replace(' ', '+')
        nodo, precio_ref = motor.obtener_precio_mas_bajo(producto)
        
        # Alerta visual con el precio corregido
        st.warning(f"🎯 **Radar Mittelbach:** Referencia estimada **{precio_ref}** en **{nodo}**.")

        # Disparo automático a Google Shopping
        url_google = f"https://www.google.com/search?q={p_plus}+price+usd"
        st.components.v1.html(f'<script>window.open("{url_google}", "_blank").focus();</script>', height=0)

        st.subheader("🌎 Nodos Globales (Miami / China)")
        col1, col2 = st.columns(2)
        with col1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{p_plus}.html", use_container_width=True)
            st.link_button("🛒 eBay", f"https://www.ebay.com/sch/i.html?_nkw={p_plus}", use_container_width=True)
        with col2:
            st.link_button("📦 Amazon", f"https://www.amazon.com/s?k={p_plus}", use_container_width=True)
            st.link_button("🇦🇷 Mercado Libre", f"https://listado.mercadolibre.com.ar/{p_plus}", use_container_width=True)

elif modo == "📜 Búsqueda de Antepasados":
    persona = st.text_input("Ingrese Antepasado:", placeholder="Ej: Maria Cesira Giustini")
    if persona:
        nodos_id = motor.generar_nodos_identidad(persona)
        st.info(f"🔍 Escaneando registros para: {persona}")
        
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇮🇹 Antenati", nodos_id["Antenati"], use_container_width=True)
            st.link_button("🚢 CEMLA", nodos_id["CEMLA"], use_container_width=True)
        with c2:
            st.link_button("🌳 FamilySearch", nodos_id["FamilySearch"], use_container_width=True)
            st.link_button("🇪🇺 Geneanet", nodos_id["Geneanet"], use_container_width=True)

st.markdown("---")
st.caption("QAP - v7.2 | Sensor de precios recalibrado.")
