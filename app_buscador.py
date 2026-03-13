import streamlit as st
import motor_busqueda as motor 

st.set_page_config(page_title="Radar Mittelbach v8.6", layout="centered")

# --- LÓGICA DE LIMPIEZA TOTAL ---
if 'contador_limpieza' not in st.session_state:
    st.session_state.contador_limpieza = 0

def limpiar_radar():
    # Al aumentar el contador, el 'key' del text_input cambia y Streamlit lo resetea
    st.session_state.contador_limpieza += 1
    st.rerun()

st.title("🌐 Centro de Mandos: SMLabs")
st.markdown("---")

# Fila de búsqueda
col_in, col_btn = st.columns([4, 1])

with col_in:
    # El secreto está en el key dinámico: f"input_{st.session_state.contador_limpieza}"
    entrada = st.text_input(
        "Ingresar consulta:", 
        key=f"input_{st.session_state.contador_limpieza}",
        placeholder="Ej: Queso Port Salut o Laptop..."
    )

with col_btn:
    st.write("") # Alineadores de espacio
    st.write("")
    if st.button("🗑️ Limpiar"):
        limpiar_radar()

if entrada:
    # El Radar procesa la información
    info = motor.obtener_datos_radar(entrada)
    
    st.warning(f"🎯 **Radar Mittelbach:** Mejor precio estimado **{info['precio']}** en **{info['mercado']}**.")

    # Separación por Mundo (Carbono vs Silicio)
    if info['tipo'] == "carbono":
        st.subheader("🛒 Nodos de Consumo Local (Argentina)")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇦🇷 Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={entrada}", use_container_width=True)
        with c2:
            st.link_button("🤝 Coop. Obrera", f"https://www.lacoopeencasa.coop/buscar?q={entrada}", use_container_width=True)
    else:
        st.subheader("🌎 Nodos Globales (Miami / China)")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{entrada}.html", use_container_width=True)
        with g2:
            st.link_button("🛒 eBay (Refurbished)", f"https://www.ebay.com/sch/i.html?_nkw={entrada}", use_container_width=True)

st.markdown("---")
st.caption(f"QAP - v8.6 | Ciclo de limpieza: {st.session_state.contador_limpieza}")
