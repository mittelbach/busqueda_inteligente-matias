import streamlit as st
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components

# --- 1. CONFIGURACIÓN VISUAL (AZUL MARINO + GRIS TOPO + LETRAS GRANDES) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #001f3f !important; }
    h1 { font-size: 3.5rem !important; color: #ffffff !important; font-weight: 800 !important; }
    h3 { font-size: 2rem !important; color: #ffffff !important; }
    .stTextInput input {
        background-color: #484848 !important;
        color: #ffffff !important;
        font-size: 1.5rem !important;
        border: 2px solid #00ffa2 !important;
        border-radius: 10px !important;
        padding: 10px;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 4em;
        background-color: #484848 !important; 
        border: 1px solid #00ffa2 !important;
        color: #ffffff !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

def buscar_oferta_meli(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        # URL corregida para el scraping interno
        url = f"https://www.mercadolibre.com.ar/ofertas?keywords={query.replace(' ', '%20')}"
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        item = soup.find('div', {'class': 'promotion-item__container'})
        if item:
            precio = item.find('span', {'class': 'andes-money-amount__fraction'}).text
            nombre = item.find('p', {'class': 'promotion-item__title'}).text[:35]
            return f"💰 **${precio}** - *{nombre}...*"
    except:
        return None

st.title("Busca Fácil 🔍")

categoria = st.radio("Seleccioná el origen del flujo:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí y presioná Enter...")

if producto:
    # --- PROTOCOLO DE APERTURA AUTOMÁTICA (Google Shopping) ---
    target_url = f"https://www.google.com.ar/search?q={producto.replace(' ', '+')}&tbm=shop"
    
    components.html(
        f"""<script>window.open('{target_url}', '_blank');</script>""",
        height=0,
    )

    with st.spinner('Cazando ofertas...'):
        resultado_oferta = buscar_oferta_meli(producto)
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")

    st.markdown(f"### Nodos de {categoria}:")
    cols = st.columns(4)
    
    # --- CORRECCIÓN CRÍTICA DE URL PARA EVITAR NXDOMAIN ---
    # Usamos www.mercadolibre.com.ar/search en lugar de lista.mercadolibre
    query_segura_meli = f"https://www.mercadolibre.com.ar/search?as_word={producto.replace(' ', '%20')}"
    
    if categoria == "Tecno y Vestimenta":
        nodos = [
            ("Meli 🇦🇷", query_segura_meli),
            ("Amazon 🌐", f"https://www.amazon.com/s?k={producto}"),
            ("AliExpress 🇨🇳", f"https://es.aliexpress.com/wholesale?SearchText={producto}"),
            ("eBay 🇺🇸", f"https://www.ebay.com/sch/i.html?_nkw={producto}")
        ]
    else:
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/{producto}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{producto}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigit/search?searchterm={producto}"),
            ("Día", f"https://diaonline.supermercaosdia.com.ar/{producto}")
        ]

    for i, (nombre, link) in enumerate(nodos):
        with cols[i % 4]:
            st.link_button(nombre, link)

st.divider()
st.caption("Busca Fácil - Matías Mittelbach © 2026")
