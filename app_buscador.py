import streamlit as st
import motor_busqueda as motor 

st.set_page_config(page_title="Radar Mittelbach v6.0", layout="centered")

st.title("🌐 Centro de Mandos: SMLabs")

modo = st.radio("Seleccione Objetivo:", ["🛒 Consumo & Global", "📜 Búsqueda de Antepasados"], horizontal=True)

st.markdown("---")

if modo == "🛒 Consumo & Global":
    producto = st.text_input("¿Qué buscamos hoy, socio?", placeholder="Ej: Laptop refurbished, Queso, Resina...")
    
    if producto:
        p_plus = producto.replace(' ', '+')
        p_dash = producto.replace(' ', '-')
        
        # Ejecución Radar
        nodo, precio_formateado = motor.obtener_precio_mas_bajo(producto)
        st.warning(f"🎯 **Radar:** El mejor precio detectado es **{precio_formateado}** en **{nodo}**.")

        # Disparo Automático (Google Shopping / Global)
        url_google = f"https://www.google.com.ar/search?q={p_plus}+price+usd"
        st.components.v1.html(f'<script>window.open("{url_google}", "_blank").focus();</script>', height=0)

        # SECCIÓN 1: NODOS GLOBALES (Prioridad para Tecnología)
        st.subheader(f"🌎 Nodos Globales: {producto}")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{p_dash}.html", use_container_width=True)
            st.link_button("📦 Amazon (Global)", f"https://www.amazon.com/s?k={p_plus}", use_container_width=True)
            st.link_button("🧡 Temu", f"https://www.temu.com/search_result.html?search_key={p_plus}", use_container_width=True)
        with g2:
            st.link_button("🛒 eBay", f"https://www.ebay.com/sch/i.html?_nkw={p_plus}", use_container_width=True)
            st.link_button("✈️ Tiendamia", f"https://tiendamia.com/ar/search?amz={p_plus}", use_container_width=True)
            st.link_button("🇦🇷 Mercado Libre", f"https://listado.mercadolibre.com.ar/{p_dash}", use_container_width=True)

        # SECCIÓN 2: NODOS DE CONSUMO (Alimentos/Locales)
        st.markdown("---")
        st.subheader("🛒 Nodos de Supermercado / Locales")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇦🇷 Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={p_plus}", use_container_width=True)
            st.link_button("🇫🇷 Carrefour", f"https://www.carrefour.com.ar/{p_plus}", use_container_width=True)
            st.link_button("🇪🇸 Día Online", f"https://diaonline.supermercadosdia.com.ar/{p_plus}", use_container_width=True)
        with c2:
            st.link_button("🏢 Cencosud (J/D/V)", f"https://www.jumbo.com.ar/{p_plus}", use_container_width=True)
            st.link_button("🤝 Coop. Obrera", f"https://www.lacoopeencasa.coop/buscar?q={p_plus}", use_container_width=True)
            st.link_button("🏔️ La Anónima", f"https://supermercado.laanonimaonline.com/buscar?busqueda={p_plus}", use_container_width=True)

elif modo == "📜 Búsqueda de Antepasados":
    persona = st.text_input("Ingrese Antepasado:", placeholder="Ej: Maria Cesira Giustini")
    if persona:
        st.info(f"🔍 **Radar Histórico:** Rastreando a {persona}")
        nodos_id = motor.generar_nodos_genealogia(persona)
        
        # Disparo automático Google Genealógico
        url_historia = f"https://www.google.com/search?q=%22{persona}%22+(acta+OR+nascita+OR+registro)"
        st.components.v1.html(f'<script>window.open("{url_historia}", "_blank").focus();</script>', height=0)

        i1, i2 = st.columns(2)
        with i1:
            st.link_button("🇮🇹 Antenati", nodos_id["Antenati"], use_container_width=True)
            st.link_button("🌳 FamilySearch", nodos_id["FamilySearch"], use_container_width=True)
            st.link_button("🚢 CEMLA", nodos_id["CEMLA"], use_container_width=True)
        with i2:
            st.link_button("🇪🇺 Geneanet", nodos_id["Geneanet"], use_container_width=True)
            st.link_button("🧬 MyHeritage", nodos_id["MyHeritage"], use_container_width=True)
            st.link_button("🇪🇸 PARES", nodos_id["PARES"], use_container_width=True)

st.markdown("---")
st.caption("QAP - Protocolo Mittelbach v6.0 | El que no entiende, funciona como célula cancerosa.")
