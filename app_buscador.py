import streamlit as st
import motor_busqueda as motor 

st.set_page_config(page_title="Radar Mittelbach v8.7", layout="centered")

# --- LÓGICA DE LIMPIEZA ---
if 'contador' not in st.session_state:
    st.session_state.contador = 0

def limpiar_radar():
    st.session_state.contador += 1
    # No usamos rerun aquí para evitar que mate el proceso de apertura de pestañas
    # Simplemente cambiamos el ID del input

st.title("🌐 Centro de Mandos: SMLabs")
st.markdown("---")

# Fila de búsqueda
col_in, col_btn = st.columns([4, 1])

with col_in:
    entrada = st.text_input(
        "Ingresar consulta:", 
        key=f"input_{st.session_state.contador}", # ID Dinámico
        placeholder="Ej: Queso Port Salut o Laptop..."
    )

with col_btn:
    st.write("") 
    st.write("")
    if st.button("🗑️ Limpiar"):
        limpiar_radar()
        st.rerun() # Ahora sí, después de asegurar el estado

if entrada:
    # 1. Obtenemos datos del Radar
    info = motor.obtener_datos_radar(entrada)
    st.warning(f"🎯 **Radar:** Precio estimado **{info['precio']}** en **{info['mercado']}**.")

    # 2. DISPARO AUTOMÁTICO (Corregido)
    # Generamos la URL según sea Carbono o Silicio
    if info['tipo'] == "carbono":
        url_auto = f"https://www.google.com.ar/search?q={entrada.replace(' ', '+')}+precio+argentina"
    else:
        url_auto = f"https://www.google.com/search?q={entrada.replace(' ', '+')}+price+usd"
    
    # Inyectamos el JS para abrir la pestaña
    st.components.v1.html(f'<script>window.open("{url_auto}", "_blank").focus();</script>', height=0)

    # 3. NODOS DINÁMICOS
    if info['tipo'] == "carbono":
        st.subheader("🛒 Nodos de Consumo Local")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇦🇷 Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={entrada}", use_container_width=True)
        with c2:
            st.link_button("🤝 Coop. Obrera", f"https://www.lacoopeencasa.coop/buscar?q={entrada}", use_container_width=True)
    else:
        st.subheader("🌎 Nodos Globales")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{entrada}.html", use_container_width=True)
        with g2:
            st.link_button("🛒 eBay (Refurbished)", f"https://www.ebay.com/sch/i.html?_nkw={entrada}", use_container_width=True)

st.markdown("---")
st.caption(f"QAP - v8.7 | Radar y Disparo Automático Sincronizados.")
