import streamlit as st
import motor_busqueda as motor 

st.set_page_config(page_title="Radar Mittelbach v8.8", layout="centered")

if 'contador' not in st.session_state:
    st.session_state.contador = 0

def limpiar_radar():
    st.session_state.contador += 1

st.title("🌐 Centro de Mandos: SMLabs")
st.markdown("---")

col_in, col_btn = st.columns([4, 1])
with col_in:
    entrada = st.text_input(
        "Ingresar consulta:", 
        key=f"input_{st.session_state.contador}",
        placeholder="Ej: Queso Port Salut o Laptop..."
    )

with col_btn:
    st.write("") 
    st.write("")
    if st.button("🗑️ Limpiar"):
        limpiar_radar()
        st.rerun()

if entrada:
    info = motor.obtener_datos_radar(entrada)
    st.warning(f"🎯 **Radar:** Precio estimado **{info['precio']}** en **{info['mercado']}**.")

    # Disparo automático
    p_url = entrada.replace(' ', '+')
    url_auto = f"https://www.google.com/search?q={p_url}+price" + ("+argentina" if info['tipo'] == "carbono" else "+usd")
    st.components.v1.html(f'<script>window.open("{url_auto}", "_blank").focus();</script>', height=0)

    # --- NODOS DINÁMICOS AMPLIADOS ---
    if info['tipo'] == "carbono":
        st.subheader("🛒 Nodos de Consumo Local (Argentina)")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇦🇷 Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={entrada}", use_container_width=True)
            st.link_button("🇫🇷 Carrefour", f"https://www.carrefour.com.ar/{entrada}", use_container_width=True)
        with c2:
            st.link_button("🤝 Coop. Obrera", f"https://www.lacoopeencasa.coop/buscar?q={entrada}", use_container_width=True)
            st.link_button("🇨🇱 Jumbo", f"https://www.jumbo.com.ar/{entrada}", use_container_width=True)
    else:
        st.subheader("🌎 Nodos Globales (Tecnología)")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{entrada}.html", use_container_width=True)
            st.link_button("📦 Amazon", f"https://www.amazon.com/s?k={entrada}", use_container_width=True)
        with g2:
            st.link_button("🛒 eBay", f"https://www.ebay.com/sch/i.html?_nkw={entrada}", use_container_width=True)
            st.link_button("🧡 Temu", f"https://www.temu.com/search_result.html?search_key={entrada}", use_container_width=True)

st.markdown("---")
st.caption(f"QAP - v8.8 | Cobertura total: 4 nodos por mundo.")
