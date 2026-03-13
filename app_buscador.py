import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 1. CONFIGURACIÓN VISUAL (ESTILO PROFESIONAL LSA) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #001f3f;
    }
    h1, h2, h3, p, span, label {
        color: #ffffff !important;
    }
    /* BOTONES: Contraste Asegurado */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #003366 !important;
        color: #ffffff !important; /* Letras Blancas */
        border: 2px solid #00ffa2 !important;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ffa2 !important;
        color: #001f3f !important;
    }
    /* Input de búsqueda */
    .stTextInput>div>div>input {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. MOTOR DE CAZA DE OFERTAS (CON ORIGEN) ---
def buscar_oferta_meli(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://www.mercadolibre.com.ar/ofertas?keywords={query}"
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        precio = soup.find('span', {'class': 'andes-money-amount__fraction'}).text
        descuento = soup.find('span', {'class': 'andes-money-amount__discount'}).text
        # Retornamos precio, descuento y el nombre del portal
        return f"💰 **${precio}** ({descuento} OFF) en **Mercado Libre 🇦🇷**"
    except:
        return None

# --- 3. INTERFAZ DE USUARIO ---
st.title("Busca Fácil:")

categoria = st.radio("Seleccioná el sector de búsqueda:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

producto = st.text_input(f"¿Qué {categoria.lower()} buscamos?", placeholder="Escribí y presioná Enter...")

if producto:
    # LÍNEA INYECTADA: Ofertas con Origen
    with st.spinner('Rastreando el origen de la mejor oferta...'):
        resultado_oferta = buscar_oferta_meli(producto)
        
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")
        else:
            st.info("No hay etiquetas de 'Oferta' activas ahora. Probá con los nodos de abajo.")

    st.markdown(f"### Nodos de {categoria}:")

    # --- ESTRUCTURA DE 4 NODOS POR FILA ---
    if categoria == "Tecno y Vestimenta":
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.link_button("Meli 🇦🇷", f"https://lista.mercadolibre.com.ar/{producto.replace(' ', '-')}")
        with col2:
            st.link_button("Amazon 🌐", f"https://www.amazon.com/s?k={producto}")
        with col3:
            st.link_button("AliExpress 🇨🇳", f"https://es.aliexpress.com/wholesale?SearchText={producto}")
        with col4:
            st.link_button("eBay 🇺🇸", f"https://www.ebay.com/sch/i.html?_nkw={producto}")

    elif categoria == "Alimentos":
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.link_button("Carrefour", f"https://www.carrefour.com.ar/{producto}")
        with col2:
            st.link_button("Jumbo", f"https://www.jumbo.com.ar/{producto}")
        with col3:
            st.link_button("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?_dyncharset=utf-8&question={producto}")
        with col4:
            st.link_button("Vea", f"https://www.vea.com.ar/{producto}")

st.divider()
st.caption("Busca Fácil - Matías Mittelbach © 2026")
