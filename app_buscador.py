import streamlit as st
import motor_busqueda as motor 

# Configuración Mittelbach
st.set_page_config(page_title="Radar Mittelbach v4.0", layout="centered")

st.title("🌐 Centro de Mandos: SMLabs")

# Selector de Modo de Radar (Consumo vs Identidad)
modo = st.radio("Seleccione Objetivo del Radar:", ["🛒 Consumo & Global", "👤 Búsqueda de Personas"], horizontal=True)

st.markdown("---")

# MODO 1: CONSUMO Y MERCADOS
if modo == "🛒 Consumo & Global":
    producto = st.text_input("¿Qué buscamos hoy, socio?", placeholder="Ej: Queso, Resina, BTC...")
    
    if producto:
        p_low = producto.lower()
        p_plus = producto.replace(' ', '+')
        p_dash = producto.replace(' ', '-')
        
        # Ejecución Radar Dinámico
        nodo, precio = motor.obtener_precio_mas_bajo(producto)
        
        if any(x in p_low for x in ["btc", "bitcoin", "xrp", "eth"]):
            st.warning("₿ **Activo de Resguardo:** Analizando mercados. Ojo con la entropía.")
        else:
            st.warning(f"🎯 **Radar:** El mejor precio detectado es **${precio:,.2f}** en **{nodo}**.")

        # Nodos de Consumo (Simetría 3x2)
        st.subheader(f"🛒 Nodos de Consumo: {producto}")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇦🇷 Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={p_plus}", use_container_width=True)
            st.link_button("🇫🇷 Carrefour", f"https://www.carrefour.com.ar/{p_plus}", use_container_width=True)
            st.link_button("🇪🇸 Día Online", f"https://diaonline.supermercadosdia.com.ar/{p_plus}", use_container_width=True)
        with c2:
            st.link_button("🏢 Cencosud (J/D/V)", f"https://www.jumbo.com.ar/{p_plus}", use_container_width=True)
            st.link_button("🤝 Coop. Obrera", f"https://www.lacoopeencasa.coop/buscar?q={p_plus}", use_container_width=True)
            st.link_button("🏔️ La Anónima", f"https://supermercado.laanonimaonline.com/buscar?busqueda={p_plus}", use_container_width=True)

        # Nodos Globales (Simetría 3x2)
        st.markdown("---")
        st.subheader("🌎 Nodos Globales")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇦🇷 Mercado Libre", f"https://listado.mercadolibre.com.ar/{p_dash}", use_container_width=True)
            st.link_button("✈️ Tiendamia", f"https://tiendamia.com/ar/search?amz={p_plus}", use_container_width=True)
            st.link_button("🧡 Temu", f"https://www.temu.com/search_result.html?search_key={p_plus}", use_container_width=True)
        with g2:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{p_dash}.html", use_container_width=True)
            st.link_button("📦 Amazon", f"https://www.amazon.com/s?k={p_plus}", use_container_width=True)
            st.link_button("🛒 eBay", f"https://www.ebay.com/sch/i.html?_nkw={p_plus}", use_container_width=True)

# MODO 2: RADAR DE IDENTIDAD (Buscador de Personas Potente)
elif modo == "👤 Búsqueda de Personas":
    persona = st.text_input("Ingrese Nombre Completo:", placeholder="Nombre Apellido")
    
    if persona:
        st.info(f"🔍 **Radar de Identidad:** Escaneando huella digital de: {persona}")
        nodos_id = motor.generar_nodos_persona(persona)
        
        # Simetría 3x2 para Personas
        i1, i2 = st.columns(2)
        with i1:
            st.link_button("👔 LinkedIn (Profesional)", nodos_id["LinkedIn"], use_container_width=True)
            st.link_button("📄 Dateas (Registros)", nodos_id["Dateas"], use_container_width=True)
            st.link_button("🆔 CuitOnline (Fiscal)", nodos_id["CuitOnline"], use_container_width=True)
        with i2:
            st.link_button("📸 Instagram (Social)", nodos_id["Instagram"], use_container_width=True)
            st.link_button("👥 Facebook (Familiar)", nodos_id["Facebook"], use_container_width=True)
            st.link_button("🎓 Scholar (Académico)", nodos_id["Scholar"], use_container_width=True)

st.markdown("---")
st.caption("QAP - Protocolo Mittelbach v4.0 | El que no entiende, funciona como célula cancerosa.")
