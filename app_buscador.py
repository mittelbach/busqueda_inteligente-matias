import streamlit as st
import scanner_ean 
import streamlit.components.v1 as components

# --- ESTILO MATÍAS ---
st.set_page_configimport streamlit as st
import scanner_ean 
import st_components_html as sc

# --- ESTILO MATÍAS ---
st.set_page_config(page_title="Busca Fácil 🔍", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #001f3f !important; }
    h1 { color: #ffffff !important; text-align: center; font-weight: 800; }
    .stTextInput input { background-color: #484848 !important; color: white !important; border: 2px solid #00ffa2 !important; }
    div.stButton > button { background-color: #00ffa2 !important; color: #001f3f !important; font-weight: bold !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# CAPTURADOR DE MENSAJES (Invisible y estático)
# Este script atrapa el número y lo mete en el buscador sin recargar
sc.html("""
<script>
    window.parent.addEventListener('message', function(e) {
        if (e.data.type === 'barcode') {
            const inputs = window.parent.document.querySelectorAll('input');
            for (let input of inputs) {
                // Buscamos el input principal
                if (input.dataset.testid === "stTextInput" || input.placeholder.includes("779")) {
                    var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                    setter.call(input, e.data.value);
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    break;
                }
            }
        }
    });
</script>
""", height=0)

st.title("Busca Fácil 🔍")

# Inicializar estado sin Key
if "ver_zona" not in st.session_state: st.session_state.ver_zona = False

categoria = st.radio("Origen del flujo:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

# Botón para activar el escáner
if st.button("✨ ABRIR / CERRAR ZONA DE ESCANEO"):
    st.session_state.ver_zona = not st.session_state.ver_zona

# Contenedor estático para el escáner (Evita KeyError)
placeholder_escaner = st.empty()
if st.session_state.ver_zona:
    with placeholder_escaner.container():
        scanner_ean.ejecutar_escaner()

# Input donde caerá el resultado
producto_input = st.text_input("Buscador", placeholder="779 o nombre...", key="main_input_search")

if producto_input:
    nombre_final = producto_input
    if producto_input.isdigit() and len(producto_input) >= 8:
        with st.spinner('Identificando producto...'):
            traduccion = scanner_ean.obtener_nombre_por_ean(producto_input)
            if traduccion:
                st.info(f"📦 Producto identificado: {traduccion}")
                nombre_final = traduccion

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
st.caption("QAP - Radar de Homeostasis | Matías Mittelbach © 2026")(page_title="Busca Fácil 🔍", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #001f3f !important; }
    h1 { color: #ffffff !important; text-align: center; font-weight: 800; }
    .stTextInput input { background-color: #484848 !important; color: white !important; border: 2px solid #00ffa2 !important; }
    div.stButton > button { background-color: #00ffa2 !important; color: #001f3f !important; font-weight: bold !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# CAPTURADOR DE MENSAJES (Sincronización de Input)
components.html("""
<script>
    window.parent.addEventListener('message', function(e) {
        if (e.data.type === 'barcode') {
            const inputs = window.parent.document.querySelectorAll('input');
            for (let input of inputs) {
                if (input.placeholder.includes("779") || input.ariaLabel === "Buscador") {
                    var setter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                    setter.call(input, e.data.value);
                    input.dispatchEvent(new Event('input', { bubbles: true }));
                    break;
                }
            }
        }
    });
</script>
""", height=0)

st.title("Busca Fácil 🔍")

if "cam_on" not in st.session_state: st.session_state.cam_on = False

categoria = st.radio("Origen del flujo:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

if st.button("✨ ABRIR ESCÁNER DE GÓNDOLA"):
    st.session_state.cam_on = not st.session_state.cam_on

if st.session_state.cam_on:
    scanner_ean.ejecutar_escaner()

producto_input = st.text_input("Buscador", placeholder="779 o nombre...", key="main_search")

if producto_input:
    nombre_final = producto_input
    if producto_input.isdigit() and len(producto_input) >= 8:
        with st.spinner('Identificando...'):
            identidad = scanner_ean.obtener_nombre_por_ean(producto_input)
            if identidad:
                st.info(f"📦 Producto: {identidad}")
                nombre_final = identidad

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
