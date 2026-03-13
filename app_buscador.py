import streamlit as st
import motor_busqueda as motor 

st.set_page_config(page_title="Radar Mittelbach v8.5", layout="centered")

# Función de limpieza que REALMENTE borra la pantalla
if 'query' not in st.session_state:
    st.session_state.query = ""

def limpiar():
    st.session_state.query = ""
    st.rerun()

st.title("🌐 Centro de Mandos: SMLabs")
st.markdown("---")

# Fila de búsqueda con botón de limpieza funcional
col1, col2 = st.columns([4, 1])
with col1:
    entrada = st.text_input("Ingresar consulta:", value=st.session_state.query, placeholder="Ej: Queso Port Salut o Laptop...")
with col2:
    st.write("") # Alineación
    st.write("")
    if st.button("🗑️ Limpiar"):
        limpiar()

if entrada:
    st.session_state.query = entrada
    info = motor.obtener_datos_radar(entrada)
    
    # El Radar ahora te dice PRECIO y LUGAR correctamente
    st.warning(f"🎯 **Radar Mittelbach:** El mejor precio estimado es **{info['precio']}** en **{info['mercado']}**.")

    # Cambio dinámico de Nodos según el mundo (Carbono o Silicio)
    if info['tipo'] == "carbono":
        st.subheader("🛒 Nodos de Consumo Local (Argentina)")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇦🇷 Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={entrada}")
        with c2:
            st.link_button("🤝 Coop. Obrera", f"https://www.lacoopeencasa.coop/buscar?q={entrada}")
    else:
        st.subheader("🌎 Nodos Globales (Miami / China)")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{entrada}.html")
        with g2:
            st.link_button("🛒 eBay (Refurbished)", f"https://www.ebay.com/sch/i.html?_nkw={entrada}")

st.markdown("---")
st.caption("QAP - v8.5 | Calibrado para el mundo del carbono y silicio.")
