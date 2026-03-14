import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 1. CONFIGURACIÓN VISUAL (AZUL MARINO Y CONTRASTE EXTREMO) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    /* Fondo de la App */
    .stApp {
        background-color: #001f3f !important;
    }
    
    /* Textos generales */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
    }

    /* BUSCADOR: Fondo blanco, Letras NEGRAS */
    .stTextInput>div>div>input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* BOTONES (NODOS): Letras BLANCAS SIEMPRE */
    div.stButton > button:first-child {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #003366 !important; 
        color: #ffffff !important; /* BLANCO FIJO */
        border: 2px solid #00ffa2 !important;
        font-weight: bold;
        display: block;
    }

    /* HOVER: Cambia a fondo turquesa y letras azules para contraste */
    div.stButton > button:first-child:hover {
        background-color: #00ffa2 !important;
        color: #001f3f !important;
        border: 2px solid #ffffff !important;
    }

    /* Forzar visibilidad del texto dentro del botón de enlace */
    div.stButton > button p {
        color: #ffffff !important;
    }
    div.stButton > button:hover p {
        color: #001f3f !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MOTOR DE CAZA DE OFERTAS (CON TÍTULO PARA EVITAR ERRORES) ---
def buscar_oferta_meli(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://www.mercadolibre.com.ar/ofertas?keywords={query}"
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        item = soup.find('div', {'class': 'promotion-item__container'})
        if item:
            precio = item.find('span', {'class': 'andes-money-amount__fraction'}).text
            descuento = item.find('span', {'class': 'andes-money-amount__discount'}).text
            nombre = item.find('p', {'class': 'promotion-item__title'}).text[:35]
            return f"💰 **${precio}** ({descuento} OFF) - *{nombre}...* en **Meli 🇦🇷**"
    except:
        return None

# --- 3. INTERFAZ DE USUARIO ---
st.title("Busca Fácil:")

categoria = st.radio("Seleccioná el sector de búsqueda:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí y presioná Enter...")

if producto:
    # LÍNEA INYECTADA: Ofertas
    with st.spinner('Escaneando ofertas reales...'):
        resultado_oferta = buscar_oferta_meli(producto)
        
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")
        else:
            st.info("Sin ofertas relámpago detectadas. Usá los nodos para búsqueda manual.")

    st.markdown(f"### Nodos de {categoria}:")

    # --- ESTRUCTURA DE 4 NODOS ---
    cols = st.columns(4)
    
    if categoria == "Tecno y Vestimenta":
        nodos_tecno = [
            ("Meli 🇦🇷", f"https://lista.mercadolibre.com.ar/{producto.replace(' ', '-')}"),
            ("Amazon 🌐", f"https://www.amazon.com/s?k={producto}"),
            ("AliExpress 🇨🇳", f"https://es.aliexpress.com/wholesale?SearchText={producto}"),
            ("eBay 🇺🇸", f"https://www.ebay.com/sch/i.html?_nkw={producto}")
        ]
        for i, (nombre, url) in enumerate(nodos_tecno):
            with cols[i]:
                st.link_button(nombre, url)

    elif categoria == "Alimentos":
        nodos_alimentos = [
            ("Carrefour", f"https://www.carrefour.com.ar/{producto}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{producto}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?_dyncharset=utf-8&question={producto}"),
            ("Vea", f"https://www.vea.com.ar/{producto}")
        ]
        for i, (nombre, url) in enumerate(nodos_alimentos):
            with cols[i]:
                st.link_button(nombre, url)

st.divider()
st.caption("Busca Fácil - Matías Mittelbach © 2026")
