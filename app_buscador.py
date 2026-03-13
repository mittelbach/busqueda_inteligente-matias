import streamlit as st
import motor_busqueda as motor 

# Configuración Mittelbach
st.set_page_config(page_title="Radar Mittelbach v7.5", layout="centered")

# Lógica de Limpieza: Resetea el estado de la aplicación
def resetear_radar():
    st.session_state["query"] = ""
    st.session_state["search_active"] = False
    st.rerun()

# Inicialización de estado
if "query" not in st.session_state:
    st.session_state["query"] = ""

st.title("🌐 Centro de Mandos: SMLabs")

modo = st.radio("Objetivo del Radar:", ["🛒 Consumo & Global", "📜 Búsqueda de Antepasados"], horizontal=True)

st.markdown("---")

# CAMPO DE BÚSQUEDA CON BOTÓN DE LIMPIEZA
col_in, col_clear = st.columns([4, 1])

with col_in:
    # Vinculamos el input al session_state para poder limpiarlo
    producto = st.text_input("Ingresar consulta:", value=st.session_state["query"], key="input_text")

with col_clear:
    st.write("") # Espaciador para alinear
    st.write("") 
    if st.button("🗑️ Limpiar"):
        resetear_radar()

if producto:
    st.session_state["query"] = producto
    p_plus = producto.replace(' ', '+')
    
    if modo == "🛒 Consumo & Global":
        nodo, precio_ref = motor.obtener_precio_mas_bajo(producto)
        st.warning(f"🎯 **Radar Mittelbach:** Consultando en **{nodo}**...")

        # Disparo automático a Google
        url_google = f"https://www.google.com/search?q={p_plus}+price+usd"
        st.components.v1.html(f'<script>window.open("{url_google}", "_blank").focus();</script>', height=0)

        # Grilla 3x2 de Nodos
        st.subheader("🌎 Nodos Globales")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{p_plus}.html", use_container_width=True)
            st.link_button("🛒 eBay", f"https://www.ebay.com/sch/i.html?_nkw={p_plus}", use_container_width=True)
        with g2:
            st.link_button("📦 Amazon", f"https://www.amazon.com/s?k={p_plus}", use_container_width=True)
            st.link_button("🇦🇷 Mercado Libre", f"https://listado.mercadolibre.com.ar/{p_plus}", use_container_width=True)

    elif modo == "📜 Búsqueda de Antepasados":
        nodos_id = motor.generar_nodos_identidad(producto)
        st.info(f"🔍 Escaneando registros para: {producto}")
        
        # Disparo automático para antepasados
        url_historia = f"https://www.google.com/search?q=%22{p_plus}%22+(acta+OR+nascita)"
        st.components.v1.html(f'<script>window.open("{url_historia}", "_blank").focus();</script>', height=0)

        i1, i2 = st.columns(2)
        with i1:
            st.link_button("🇮🇹 Antenati", nodos_id["Antenati"], use_container_width=True)
            st.link_button("🚢 CEMLA", nodos_id["CEMLA"], use_container_width=True)
        with i2:
            st.link_button("🌳 FamilySearch", nodos_id["FamilySearch"], use_container_width=True)
            st.link_button("🇪🇺 Geneanet", nodos_id["Geneanet"], use_container_width=True)

st.markdown("---")
st.caption("QAP - v7.5 | Limpieza de caché y sensores dinámicos activos.")
