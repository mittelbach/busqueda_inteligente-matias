import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- 1. CONFIGURACIÓN VISUAL (MANTENIENDO EL ESTILO) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

# Inyección de CSS para asegurar que los colores se mantengan profesionales
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: #fafafa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #262730;
        color: white;
        border: 1px solid #4x4x4x;
    }
    .stButton>button:hover {
        border-color: #00ffa2;
        color: #00ffa2;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNCIÓN DE CAZA DE OFERTAS ---
def buscar_oferta_destacada(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://www.mercadolibre.com.ar/ofertas?keywords={query}"
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        precio = soup.find('span', {'class': 'andes-money-amount__fraction'}).text
        descuento = soup.find('span', {'class': 'andes-money-amount__discount'}).text
        return f"💰 ${precio} ({descuento} OFF)"
    except:
        return None

# --- 3. INTERFAZ DE USUARIO ---
st.title("Busca Fácil:")

# Selector de Categoría (Igual al original)
categoria = st.radio("Seleccioná el sector de búsqueda:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

# Input de búsqueda
producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí aquí...")

if producto:
    # LÍNEA INYECTADA: Detección de Ofertas
    with st.spinner('Escaneando oportunidades...'):
        oferta = buscar_oferta_destacada(producto)
        if oferta:
            st.success(f"🔥 **OFERTA DE LA SEMANA DETECTADA:** {oferta}")

    st.markdown(f"### Nodos de {categoria}:")

    # --- LÓGICA DE NODOS ORIGINAL ---
    if categoria == "Tecno y Vestimenta":
        col1, col2, col3 = st.columns(3)
        with col1:
            url_meli = f"https://lista.mercadolibre.com.ar/{producto.replace(' ', '-')}"
            st.link_button("Mercado Libre 🇦🇷", url_meli)
        with col2:
            url_amz = f"https://www.amazon.com/s?k={producto}"
            st.link_button("Amazon 🌐", url_amz)
        with col3:
            url_ali = f"https://es.aliexpress.com/wholesale?SearchText={producto}"
            st.link_button("AliExpress 🇨🇳", url_ali)

    elif categoria == "Alimentos":
        col1, col2, col3 = st.columns(3)
        with col1:
            url_carrefour = f"https://www.carrefour.com.ar/{producto}"
            st.link_button("Carrefour", url_carrefour)
        with col2:
            url_jumbo = f"https://www.jumbo.com.ar/{producto}"
            st.link_button("Jumbo", url_jumbo)
        with col3:
            url_coto = f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?_dyncharset=utf-8&question={producto}"
            st.link_button("Coto", url_coto)

# Pie de página
st.divider()
st.caption("Busca Fácil - Matías Mittelbach © 2026")
