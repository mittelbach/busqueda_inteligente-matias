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

    /* BUSCADOR: Fondo blanco, Letras NEGRAS (Para que se vea lo que escribís) */
    .stTextInput>div>div>input {
        background-color: #ffffff !important;
        color: #000000 !important;
        caret-color: #000000 !important;
    }

    /* BOTONES (NODOS): Fondo Azul Oscuro, Letras BLANCAS, Borde Neón */
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #003366 !important; /* Azul botón */
        color: #ffffff !important; /* LETRAS BLANCAS FORZADAS */
        border: 2px solid #00ffa2 !important;
        font-weight: bold;
    }

    /* Hover de botones */
    .stButton>button:hover {
        background-color: #00ffa2 !important;
        color: #001f3f !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. FUNCIÓN DE CAZA DE OFERTAS (MEJORADA PARA EVITAR ERRORES) ---
def buscar_oferta_meli(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        # Agregamos filtros para que busque productos con mayor relevancia
        url = f"https://www.mercadolibre.com.ar/ofertas?keywords={query}"
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Buscamos los contenedores de productos de oferta
        item = soup.find('div', {'class': 'promotion-item__container'})
        if item:
            precio = item.find('span', {'class': 'andes-money-amount__fraction'}).text
            descuento = item.find('span', {'class': 'andes-money-amount__discount'}).text
            nombre_corto = item.find('p', {'class': 'promotion-item__title'}).text[:30] # Limitamos texto
            return f"💰 **${precio}** ({descuento} OFF) - *{nombre_corto}...* en **Meli 🇦🇷**"
    except:
        return None

# --- 3. INTERFAZ DE USUARIO ---
st.title("Busca Fácil:")

categoria = st.radio("Seleccioná el sector de búsqueda:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

producto = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí y presioná Enter...")

if producto:
    # LÍNEA INYECTADA: Ofertas
    with st.spinner('Analizando veracidad de ofertas...'):
        resultado_oferta = buscar_oferta_meli(producto)
        
        if resultado_oferta:
            # Usamos un contenedor que resalte pero no tape
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")
        else:
            st.info("No hay 'Ofertas Relámpago' ahora. Usá los nodos para búsqueda general.")

    st.markdown(f"### Nodos de {categoria}:")

    # --- ESTRUCTURA DE 4 NODOS ---
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
