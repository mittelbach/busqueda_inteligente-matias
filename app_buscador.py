import streamlit as st
import requests
from bs4 import BeautifulSoup

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Busca Fácil", page_icon="🔍")

# --- FUNCIÓN DE CAZA DE OFERTAS (LA INYECCIÓN) ---
def buscar_oferta_destacada(query):
    try:
        # Buscamos en la sección de ofertas de Mercado Libre Argentina
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = f"https://www.mercadolibre.com.ar/ofertas?keywords={query}"
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Intentamos capturar el primer precio y el % de descuento
        precio = soup.find('span', {'class': 'andes-money-amount__fraction'}).text
        descuento = soup.find('span', {'class': 'andes-money-amount__discount'}).text
        return f"💰 ${precio} ({descuento} OFF)"
    except:
        return None

# --- INTERFAZ DE USUARIO ---
st.title("Busca Fácil:")

# Input de búsqueda
producto = st.text_input("¿Qué estás buscando?", placeholder="Ej: zapatillas, celular, televisor...")

if producto:
    # 1. LÍNEA INYECTADA: Detección de Ofertas de la Semana
    with st.spinner('Rastreando ofertas calientes...'):
        oferta = buscar_oferta_destacada(producto)
        if oferta:
            st.success(f"🔥 **OFERTA DE LA SEMANA DETECTADA:** {oferta} en la sección especial.")
        else:
            st.info("No detecté etiquetas de 'Oferta' activas, pero podés revisar los nodos abajo.")

    st.subheader("Seleccioná un Nodo de búsqueda:")

    # --- NODOS DE BÚSQUEDA ---
    
    # Categoría: Tecno y Vestimenta
    st.markdown("### 📱 Tecno y Vestimenta")
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

    # Categoría: Alimentos y Supermercado
    st.markdown("### 🛒 Alimentos y Super")
    col4, col5, col6 = st.columns(3)
    
    with col4:
        url_carrefour = f"https://www.carrefour.com.ar/{producto}"
        st.link_button("Carrefour", url_carrefour)
        
    with col5:
        url_jumbo = f"https://www.jumbo.com.ar/{producto}"
        st.link_button("Jumbo", url_jumbo)
        
    with col6:
        url_coto = f"https://www.cotodigital3.com.ar/sitios/cdigi/browse?_dyncharset=utf-8&question={producto}"
        st.link_button("Coto", url_coto)

# Pie de página simple
st.divider()
st.caption("Busca Fácil - Inteligencia de Mercado")
