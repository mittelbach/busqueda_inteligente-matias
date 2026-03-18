import streamlit as st
import scanner_ean 

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Busca Fácil 🔍", page_icon="🔍", layout="centered")

# Estilo Neón Matías
st.markdown("""
    <style>
    .stApp { background-color: #001f3f !important; }
    h1 { color: #ffffff !important; text-align: center; }
    .stTextInput input { background-color: #484848 !important; color: white !important; border: 2px solid #00ffa2 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("Busca Fácil 🔍")

# Inicializar el estado si no existe
if "ver_escaner" not in st.session_state:
    st.session_state.ver_escaner = False

categoria = st.radio("Origen del flujo:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

# Botón para activar el escáner (Control de Bucle)
if st.button("✨ ACTIVAR ESCÁNER (CÁMARA)"):
    st.session_state.ver_escaner = not st.session_state.ver_escaner

# Si el estado es True, mostramos la "Habitación Contigua"
if st.session_state.ver_escaner:
    scanner_ean.ejecutar_escaner()

# Entrada manual/resultados
producto_input = st.text_input("Ingresa producto o número EAN:", placeholder="779...")

if producto_input:
    nombre_final = producto_input
    
    # Si es EAN, traducimos
    if producto_input.isdigit() and len(producto_input) >= 8:
        with st.spinner('Identificando...'):
            traduccion = scanner_ean.obtener_nombre_por_ean(producto_input)
            if traduccion:
                st.success(f"📦 Producto: {traduccion}")
                nombre_final = traduccion

    # Nodos de búsqueda
    st.markdown(f"### Nodos de {categoria}:")
    cols = st.columns(4)
    query_busqueda = producto_input if producto_input.isdigit() else nombre_final
    
    if categoria == "Alimentos":
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/buscar?q={query_busqueda}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{query_busqueda}"),
            ("La Anónima", f"https://supermercado.laanonima.com.ar/buscar?busqueda={query_busqueda}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigit/search?searchterm={nombre_final.replace(' ', '%20')}")
        ]
        for i, (nombre, link) in enumerate(nodos):
            with cols[i % 4]:
                st.link_button(nombre, link)

st.divider()
st.caption("QAP - Radar de Homeostasis | Matías Mittelbach © 2026")
