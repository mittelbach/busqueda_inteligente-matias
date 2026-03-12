import streamlit as st
import motor_busqueda as motor 

# Configuración Mittelbach
st.set_page_config(page_title="Radar Mittelbach v5.0", layout="centered")

st.title("🌐 Centro de Mandos: SMLabs")

# Selector de Modo de Radar
modo = st.radio("Seleccione Objetivo del Radar:", ["🛒 Consumo & Global", "📜 Búsqueda de Antepasados"], horizontal=True)

st.markdown("---")

# --- MODO 1: CONSUMO ---
if modo == "🛒 Consumo & Global":
    producto = st.text_input("¿Qué buscamos hoy, socio?", placeholder="Ej: Queso, Resina, BTC...")
    
    if producto:
        p_plus = producto.replace(' ', '+')
        p_dash = producto.replace(' ', '-')
        
        # Ejecución Radar
        nodo, precio = motor.obtener_precio_mas_bajo(producto)
        st.warning(f"🎯 **Radar:** El mejor precio detectado es **${precio:,.2f}** en **{nodo}**.")
        
        # DISPARO AUTOMÁTICO GOOGLE SHOPPING
        url_google = f"https://www.google.com.ar/search?q=precio+{p_plus}&udm=28"
        js = f'window.open("{url_google}", "_blank").focus();'
        st.components.v1.html(f'<script>{js}</script>', height=0)

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

# --- MODO 2: ANTEPASADOS (GENEALOGÍA) ---
elif modo == "📜 Búsqueda de Antepasados":
    persona = st.text_input("Ingrese Nombre del Antepasado:", placeholder="Nombre Apellido")
    
    if persona:
        p_plus = persona.replace(' ', '+')
        st.info(f"🔍 **Radar Histórico:** Rastreando registros de: {persona}")
        
        # DISPARO AUTOMÁTICO: Google con Dorks para archivos y actas
        url_historia = f"https://www.google.com/search?q=%22{p_plus}%22+(acta+OR+registro+OR+genealogia+OR+censo)"
        js_genea = f'window.open("{url_historia}", "_blank").focus();'
        st.components.v1.html(f'<script>{js_genea}</script>', height=0)

        nodos_id = motor.generar_nodos_genealogia(persona)
        
        # Simetría 3x2 para Archivos Históricos
        i1, i2 = st.columns(2)
        with i1:
            st.link_button("🌳 FamilySearch (Global)", nodos_id["FamilySearch"], use_container_width=True)
            st.link_button("🇮🇹 Antenati (Italia)", nodos_id["Antenati"], use_container_width=True)
            st.link_button("🚢 CEMLA (Inmigración)", nodos_id["CEMLA"], use_container_width=True)
        with i2:
            st.link_button("🇪🇺 Geneanet (Europa)", nodos_id["Geneanet"], use_container_width=True)
            st.link_button("🧬 MyHeritage", nodos_id["MyHeritage"], use_container_width=True)
            st.link_button("🇪🇸 PARES (España)", nodos_id["PARES"], use_container_width=True)

st.markdown("---")
st.caption("QAP - Protocolo Mittelbach v5.0 | Radar de Identidad Histórica Activado.")
