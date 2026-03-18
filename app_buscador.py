import streamlit as st
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components
import scanner_ean  # Importación del módulo contiguo

# --- 1. CONFIGURACIÓN VISUAL (ESTILO MATÍAS) ---
st.set_page_config(page_title="Busca Fácil 🔍", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #001f3f !important; }
    h1 { font-size: 3.5rem !important; color: #ffffff !important; font-weight: 800 !important; }
    h3 { font-size: 1.8rem !important; color: #ffffff !important; }
    .stTextInput input {
        background-color: #484848 !important;
        color: #ffffff !important;
        font-size: 1.2rem !important;
        border: 2px solid #00ffa2 !important;
        border-radius: 10px !important;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 3.5em;
        background-color: #484848 !important; 
        border: 1px solid #00ffa2 !important;
        color: #ffffff !important;
        font-weight: bold !important;
    }
    .resaltado-ean {
        background: rgba(0, 255, 162, 0.15);
        border: 1px solid #00ffa2;
        padding: 15px;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def buscar_oferta_meli(query):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
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

# --- INTERFAZ ---
st.title("Busca Fácil 🔍")

# Selector de Flujo
categoria = st.radio("Seleccioná el origen del flujo:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

# HABITACIÓN CONTIGUA: Sección de Escáner
with st.expander("✨ ABRIR ESCÁNER (CÁMARA)"):
    ean_detectado = scanner_ean.ejecutar_escaner()

# Entrada de búsqueda (se autocompleta con el escáner)
producto_input = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", 
                               value=ean_detectado if ean_detectado else "",
                               placeholder="Escribí o escaneá un producto...")

if producto_input:
    nombre_final = producto_input
    
    # Si el input es un número (EAN), intentamos humanizarlo
    if producto_input.isdigit() and len(producto_input) >= 8:
        with st.spinner('Identificando producto por EAN...'):
            identidad = scanner_ean.obtener_nombre_por_ean(producto_input)
            if identidad:
                st.markdown(f"<div class='resaltado-ean'>📦 **Producto:** {identidad}</div>", unsafe_allow_html=True)
                nombre_final = identidad

    # --- PROTOCOLO DE APERTURA (Google Shopping) ---
    target_url = f"https://www.google.com.ar/search?q={nombre_final.replace(' ', '+')}&tbm=shop"
    components.html(f"<script>window.open('{target_url}', '_blank');</script>", height=0)

    # Buscar Oferta en Meli
    with st.spinner('Rastreando precios...'):
        resultado_oferta = buscar_oferta_meli(nombre_final)
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")

    st.markdown(f"### Nodos de {categoria}:")
    cols = st.columns(4)
    
    # Lógica de URLs para los Nodos
    if categoria == "Tecno y Vestimenta":
        nodos = [
            ("Meli 🇦🇷", f"https://www.mercadolibre.com.ar/jm/search?as_word={nombre_final.replace(' ', '%20')}"),
            ("Amazon 🌐", f"https://www.amazon.com/s?k={nombre_final.replace(' ', '+')}"),
            ("AliExpress 🇨🇳", f"https://es.aliexpress.com/wholesale?SearchText={nombre_final.replace(' ', '+')}"),
            ("eBay 🇺🇸", f"https://www.ebay.com/sch/i.html?_nkw={nombre_final.replace(' ', '+')}")
        ]
    else:
        # Aquí usamos el código EAN si está disponible para Carrefour/Jumbo
        query_super = producto_input if producto_input.isdigit() else nombre_final
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/buscar?q={query_super}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{query_super}"),
            ("La Anónima", f"https://supermercado.laanonima.com.ar/buscar?busqueda={query_super}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigit/search?searchterm={nombre_final.replace(' ', '%20')}")
        ]

    for i, (nombre, link) in enumerate(nodos):
        with cols[i % 4]:
            st.link_button(nombre, link)

st.divider()
st.caption("QAP - Radar de Homeostasis | Matías Mittelbach © 2026")
