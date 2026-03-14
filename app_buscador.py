import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 1. CONFIGURACIÓN VISUAL (EXTREMA PARA ELIMINAR EL VELO BLANCO) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    /* Fondo principal */
    .stApp {
        background-color: #001f3f !important;
    }
    
    /* Forzar que todos los textos base sean blancos */
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
    }

    /* BUSCADOR: Fondo blanco y letras NEGRAS reales */
    .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    /* BOTONES (NODOS): Estilo Base */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #003366 !important;
        border: 2px solid #00ffa2 !important;
        transition: all 0.3s ease;
    }

    /* TEXTO DENTRO DE LOS BOTONES: Forzado a Blanco */
    div.stButton > button div p, 
    div.stButton > button span,
    div.stButton > button p {
        color: #ffffff !important;
        font-weight: bold !important;
    }

    /* HOVER: Cuando pasas el mouse, el fondo es Turquesa y el texto NEGRO */
    div.stButton > button:hover {
        background-color: #00ffa2 !important;
        border: 2px solid #ffffff !important;
    }
    
    div.stButton > button:hover div p,
    div.stButton > button:hover span,
    div.stButton > button:hover p {
        color: #001f3f !important; /* Azul oscuro para que se lea sobre el turquesa */
    }

    /* Eliminar cualquier sombra o borde extraño que cause el 'velo' */
    div.stButton > button:focus {
        outline: none !important;
        box-shadow: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MOTOR DE CAZA DE OFERTAS ---
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

producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí aquí...")

if producto:
    with st.spinner('Cazando ofertas...'):
        resultado_oferta = buscar_oferta_meli(producto)
        
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")
        else:
            st.info("Sin ofertas relámpago ahora. Usá los nodos para búsqueda manual.")

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
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/{producto}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{producto}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?_dyncharset=utf-8&question={producto}"),
            ("Vea", f"https://www.vea.com.ar/{producto}")
        ]

    for i, (nombre, url) in enumerate(nodos):
        with cols[i]:
            st.link_button(nombre, url)

st.divider()
st.caption("Busca Fácil - Matías Mittelbach © 2026")
