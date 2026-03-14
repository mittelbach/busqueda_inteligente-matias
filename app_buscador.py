import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 1. CONFIGURACIÓN VISUAL (GRIS TOPO Y AZUL MARINO) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    /* Fondo Principal */
    .stApp {
        background-color: #001f3f !important;
    }
    
    /* BUSCADOR (ENTER): Color Gris Topo */
    .stTextInput input {
        background-color: #484848 !important; /* Gris Topo */
        color: #ffffff !important; /* Letras Blancas para que se lean bien */
        border: 1px solid #00ffa2 !important;
    }
    
    /* Placeholder (lo que dice 'Escribí aquí...') en gris claro */
    .stTextInput input::placeholder {
        color: #cccccc !important;
    }

    /* BOTONES (NODOS): Fondo Gris Topo Fijo */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #484848 !important; /* Gris Topo */
        border: 1px solid #00ffa2 !important;
        transition: all 0.3s ease;
    }

    /* TEXTO DE BOTONES: Blanco absoluto, sin sombras */
    div.stButton > button div p, 
    div.stButton > button span {
        color: #ffffff !important;
        font-weight: bold !important;
        text-shadow: none !important;
    }

    /* HOVER: Cuando pasas el mouse, se ilumina el borde */
    div.stButton > button:hover {
        background-color: #00ffa2 !important;
        border: 2px solid #ffffff !important;
    }
    
    div.stButton > button:hover div p,
    div.stButton > button:hover span {
        color: #001f3f !important; /* Texto azul oscuro sobre fondo turquesa */
    }

    /* Limpieza de etiquetas de Streamlit */
    footer {visibility: hidden;}
    header {visibility: hidden;}
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

# El input ahora es Gris Topo con letras blancas
producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí aquí...")

if producto:
    with st.spinner('Cazando ofertas...'):
        resultado_oferta = buscar_oferta_meli(producto)
        
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")
        else:
            st.info("Sin ofertas relámpago detectadas. Usá los nodos para búsqueda manual.")

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
