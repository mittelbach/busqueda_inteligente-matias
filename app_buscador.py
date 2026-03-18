import streamlit as st
import requests
from bs4 import BeautifulSoup
import streamlit.components.v1 as components
import scanner_ean 

# --- ESTILO ---
st.set_page_config(page_title="Busca Fácil 🔍", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #001f3f !important; }
    h1 { color: #ffffff !important; text-align: center; font-weight: 800; }
    .stTextInput input { background-color: #484848 !important; color: white !important; border: 2px solid #00ffa2 !important; }
    div.stButton > button { background-color: #484848 !important; border: 1px solid #00ffa2 !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("Busca Fácil 🔍")

categoria = st.radio("Seleccioná el origen:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

# HABITACIÓN CONTIGUA
with st.expander("✨ ABRIR ESCÁNER (CÁMARA)", expanded=False):
    st.write("Presioná el botón verde para activar la cámara de tu celular.")
    ean_detectado = scanner_ean.ejecutar_escaner()

# Input principal
producto_input = st.text_input("Buscador", value=ean_detectado if ean_detectado else "", placeholder="Escribí o escaneá...")

if producto_input:
    nombre_final = producto_input
    
    # Lógica de traducción EAN
    if producto_input.isdigit() and len(producto_input) >= 8:
        traduccion = scanner_ean.obtener_nombre_por_ean(producto_input)
        if traduccion:
            st.info(f"📦 Producto: {traduccion}")
            nombre_final = traduccion

    # Nodos
    st.markdown(f"### Nodos de {categoria}:")
    cols = st.columns(4)
    query_super = producto_input if producto_input.isdigit() else nombre_final
    
    if categoria == "Alimentos":
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
