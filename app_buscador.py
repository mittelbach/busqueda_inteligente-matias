import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 1. CONFIGURACIÓN VISUAL (AZUL MARINO + GRIS TOPO + LETRAS GRANDES) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    /* Fondo Principal */
    .stApp {
        background-color: #001f3f !important;
    }
    
    /* LETRAS GRANDES (Título y Subtítulos) */
    h1 {
        font-size: 3.5rem !important;
        color: #ffffff !important;
        font-weight: 800 !important;
    }
    h3 {
        font-size: 2rem !important;
        color: #ffffff !important;
    }
    
    /* BUSCADOR (EL "ENTER"): Gris Topo con LETRAS BLANCAS FUERTES */
    .stTextInput input {
        background-color: #484848 !important; /* Gris Topo Interno */
        color: #ffffff !important; /* TEXTO QUE TIPEA EL USUARIO EN BLANCO */
        font-size: 1.5rem !important; /* Letra más grande para el input */
        border: 2px solid #00ffa2 !important; /* Borde neón para marcar el área */
        border-radius: 10px !important;
        padding: 10px !important;
    }
    
    /* Color del cursor y del texto de ayuda */
    .stTextInput input::placeholder {
        color: #bbbbbb !important;
    }

    /* NODOS: Gris Topo con Letra Blanca */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 4em;
        background-color: #484848 !important; 
        border: 1px solid #00ffa2 !important;
    }

    /* Texto de los Nodos en Blanco Fijo */
    div.stButton > button div p, 
    div.stButton > button span {
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }

    /* Efecto al tocar/pasar el mouse */
    div.stButton > button:hover {
        background-color: #00ffa2 !important;
    }
    div.stButton > button:hover div p {
        color: #001f3f !important;
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

# Input con estilo de "Caja de Enter"
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
