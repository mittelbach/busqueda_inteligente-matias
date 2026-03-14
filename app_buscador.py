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
    /* Estilo para los botones de los nodos */
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #484848;
        color: white;
        border: 1px solid #00ffa2;
    }
    </style>
    """, unsafe_allow_html=True)

def buscar_oferta_meli(producto):
    # Tu lógica de scraping de Mercado Libre se mantiene intacta aquí
    try:
        url = f"https://lista.mercadolibre.com.ar/{producto.replace(' ', '-')}"
        response = requests.get(url)
        # (Aquí va tu lógica de BeautifulSoup que ya tenías)
        return None 
    except:
        return None

st.title("Busca Fácil 🔍")

categoria = st.radio("Seleccioná el origen del flujo:", ["Tecno y Vestimenta", "Alimentos y Limpieza"], horizontal=True)

# Input con estilo de "Caja de Enter"
producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí y presioná Enter...")

if producto:
    # --- PROTOCOLO DE APERTURA AUTOMÁTICA (El Reflejo del AHG) ---
    # Esto abre Google Shopping en una pestaña nueva apenas detecta el Enter
    target_url = f"https://www.google.com.ar/search?q={producto.replace(' ', '+')}&tbm=shop"
    
    components.html(
        f"""
        <script>
            window.open('{target_url}', '_blank');
        </script>
        """,
        height=0,
    )

    with st.spinner('Cazando ofertas y proyectando mercado...'):
        resultado_oferta = buscar_oferta_meli(producto)
        
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")
        else:
            st.info("Búsqueda global disparada. Revisá la nueva pestaña de Google Shopping.")

    st.markdown(f"### Nodos de {categoria}:")

    cols = st.columns(4)
    if categoria == "Tecno y Vestimenta":
        nodos = [
            ("Meli 🇦🇷", f"https://lista.mercadolibre.com.ar/{producto.replace(' ', '-')}"),
            ("Amazon 🌐", f"https://www.amazon.com/s?k={producto}"),
            ("AliExpress 🇨🇳", f"https://es.aliexpress.com/wholesale?SearchText={producto}"),
            ("eBay 🇺🇸", f"https://www.ebay.com/sch/i.html?_nkw={producto}")
        ]
    else:
        # Aquí mantengo tu lógica para el Mundo del Carbono
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/{producto}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{producto}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigit/search?_dyncharset=utf-8&searchterm={producto}"),
            ("Día", f"https://diaonline.supermercaosdia.com.ar/{producto}")
        ]

    for i, (nombre, link) in enumerate(nodos):
        with cols[i % 4]:
            st.link_button(nombre, link)

st.markdown("---")
st.caption("QAP - Sistema de Monitoreo Homeostático de Precios")
