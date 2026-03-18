import streamlit as st
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components
import scanner_ean  # Importa tu nuevo archivo

# --- CONFIGURACIÓN VISUAL ---
st.set_page_config(page_title="Busca Fácil 🔍", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #001f3f !important; }
    h1 { font-size: 3.5rem !important; color: #ffffff !important; font-weight: 800 !important; }
    .stTextInput input {
        background-color: #484848 !important;
        color: #ffffff !important;
        font-size: 1.5rem !important;
        border: 2px solid #00ffa2 !important;
        border-radius: 10px !important;
    }
    div.stButton > button {
        width: 100%;
        border-radius: 8px;
        height: 4em;
        background-color: #484848 !important; 
        border: 1px solid #00ffa2 !important;
        color: #ffffff !important;
        font-weight: bold !important;
    }
    .ean-card {
        background: rgba(0, 255, 162, 0.1);
        border: 1px solid #00ffa2;
        padding: 15px;
        border-radius: 10px;
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

categoria = st.radio("Seleccioná el origen del flujo:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

# Sección de Escáner en "Habitación Contigua"
with st.expander("✨ USAR ESCÁNER EAN (BETA)"):
    ean_detectado = scanner_ean.ejecutar_escaner()

# Entrada de búsqueda
manual_input = st.text_input(f"¿Qué {categoria.lower()} buscamos hoy?", placeholder="Escribí o escaneá un producto...")

# Lógica de decisión de búsqueda
query_final = ean_detectado if ean_detectado else manual_input

if query_final:
    nombre_para_nodos = query_final
    
    # Si es un código numérico, intentamos identificar el producto
    if query_final.isdigit() and len(query_final) >= 8:
        with st.spinner('Identificando producto...'):
            traduccion = scanner_ean.obtener_nombre_por_ean(query_final)
            if traduccion:
                st.markdown(f"<div class='ean-card'>📦 **Producto:** {traduccion}</div>", unsafe_allow_html=True)
                nombre_para_nodos = traduccion

    # Apertura automática Google Shopping
    target_url = f"https://www.google.com.ar/search?q={nombre_para_nodos.replace(' ', '+')}&tbm=shop"
    components.html(f"<script>window.open('{target_url}', '_blank');</script>", height=0)

    with st.spinner('Cazando ofertas...'):
        resultado_oferta = buscar_oferta_meli(nombre_para_nodos)
        if resultado_oferta:
            st.success(f"🔥 **OFERTA DETECTADA:** {resultado_oferta}")

    st.markdown(f"### Nodos de {categoria}:")
    cols = st.columns(4)
    
    if categoria == "Tecno y Vestimenta":
        nodos = [
            ("Meli 🇦🇷", f"https://www.mercadolibre.com.ar/jm/search?as_word={nombre_para_nodos.replace(' ', '%20')}"),
            ("Amazon 🌐", f"https://www.amazon.com/s?k={nombre_para_nodos.replace(' ', '+')}"),
            ("AliExpress 🇨🇳", f"https://es.aliexpress.com/wholesale?SearchText={nombre_para_nodos.replace(' ', '+')}"),
            ("eBay 🇺🇸", f"https://www.ebay.com/sch/i.html?_nkw={nombre_para_nodos.replace(' ', '+')}")
        ]
    else:
        # Aquí están los supermercados que pediste con búsqueda por EAN/Nombre
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/buscar?q={query_final}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{query_final}"),
            ("La Anónima", f"https://supermercado.laanonima.com.ar/buscar?busqueda={query_final}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigit/search?searchterm={nombre_para_nodos.replace(' ', '%20')}")
        ]

    for i, (nombre, link) in enumerate(nodos):
        with cols[i % 4]:
            st.link_button(nombre, link)

st.divider()
st.caption("QAP - Radar de Homeostasis | Matías Mittelbach © 2026")
