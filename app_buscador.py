import streamlit as st

# Configuración de página
st.set_page_config(page_title="Radar Mittelbach v9.0", layout="centered")

# --- ESTILO DARK MODE ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🌐 Busca Facil: SMLabs")
st.markdown("---")

# --- SELECTOR DE MUNDO (CATEGORÍAS) ---
mundo = st.radio(
    "Seleccionar Mundo:",
    ["🍎 Alimentos (Carbono)", "💻 Tecno y Vestimenta (Silicio)"],
    horizontal=True
)

# --- ENTRADA DE DATOS ---
entrada = st.text_input("Ingresar consulta:", placeholder="Ej: Queso Port Salut, Laptop, etc...")

if entrada:
    p_url = entrada.replace(' ', '+')
    
    if "Alimentos" in mundo:
        st.subheader("🛒 Nodos de Consumo Local (Argentina)")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("🇦🇷 Coto Digital", f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={p_url}")
            st.link_button("🇫🇷 Carrefour", f"https://www.carrefour.com.ar/{p_url}")
            st.link_button("🛒 Google Shopping (AR)", f"https://www.google.com/search?q={p_url}+precio+argentina&tbm=shop")
        with c2:
            st.link_button("🤝 Coop. Obrera", f"https://www.lacoopeencasa.coop/buscar?q={p_url}")
            st.link_button("🇨🇱 Jumbo", f"https://www.jumbo.com.ar/{p_url}")
            st.link_button("🏢 Mercado Libre", f"https://listado.mercadolibre.com.ar/{p_url}")

    else:
        st.subheader("🌎 Nodos Globales (Tecnología)")
        g1, g2 = st.columns(2)
        with g1:
            st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{p_url}.html")
            st.link_button("📦 Amazon", f"https://www.amazon.com/s?k={p_url}")
            st.link_button("🔍 Google Shopping (USD)", f"https://www.google.com/search?q={p_url}+price+usd&tbm=shop")
        with g2:
            st.link_button("🛒 eBay", f"https://www.ebay.com/sch/i.html?_nkw={p_url}")
            st.link_button("🧡 Temu", f"https://www.temu.com/search_result.html?search_key={p_url}")
            st.link_button("💻 B&H Photo", f"https://www.bhphotovideo.com/c/search?Ntt={p_url}")

st.markdown("---")
st.caption("QAP - Radar Mittelbach v9.0 | SMLabs Systems")
