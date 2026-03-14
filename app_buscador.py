import streamlit as st
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components

# --- 1. CONFIGURACIÓN VISUAL (AZUL MARINO + GRIS TOPO + LETRAS GRANDES) ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    /* Fondo Principal */
    .stApp {
        background-color: #001f3f !important;
    }
    
    /* LETRAS GRANDES */
    h1 {
        font-size: 3.5rem !important;
        color: #ffffff !important;
        font-weight: 800 !important;
    }
    h3 {
        font-size: 2rem !important;
        color: #ffffff !important;
    }
    
    /* BUSCADOR: Gris Topo con LETRAS BLANCAS FUERTES */
    .stTextInput input {
        background-color: #484848 !important;
        color: #ffffff !important;
        font-size: 1.5rem !important;
        border: 2px solid #00ffa2 !important;
        border-radius: 10px !important;
        padding: 10px;
    }

    /* BOTONES DE LOS NODOS */
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 4em;
        background-color: #484848 !important; 
        border: 1px solid #00ffa2 !important;
        color: #ffffff !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
    }
    div.stButton > button:hover {
        border: 2px solid #ffffff !important;
        color: #00ffa2 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def buscar_oferta_meli(query):
    """Función de scraping para detectar 'fiebre' de ofertas relámpago"""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        # Usamos la ruta de ofertas para el scraping
        url = f"https://www.mercadolibre.com.ar/ofertas?keywords={query.replace(' ', '%20')}"
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        item = soup.find('div', {'class': 'promotion-item__container'})
        if item:
            precio = item.find('span', {'class': 'andes-money-amount__fraction'}).text
            nombre = item.find('p', {'class': 'promotion-item__title'}).text[:35]
            return f"💰 **${precio}** - *{nombre}...*"
        return None
    except:
        return None

# --- ESTRUCTURA DE LA APP ---

st.title("Busca Fácil 🔍")

categoria = st.radio("Seleccioná el origen del flujo:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

# Input principal
producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí aquí y presioná Enter...")

if producto:
    # --- 2. PROTOCOLO DE APERTURA AUTOMÁTICA (Google Shopping) ---
    # Este es el 'reflejo' inmediato que pediste
    target_url_shopping = f"https://www.google.com.ar/search?q={producto.replace(' ', '+')}&tbm=shop"
    
    components.html(
        f"""
        <script>
