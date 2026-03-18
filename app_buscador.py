import streamlit as st
import scanner_ean 
import streamlit.components.v1 as components

# --- CONFIGURACIÓN MATÍAS ---
st.set_page_config(page_title="Find Easy 🔍", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b1622 !important; }
    h1 { color: #ffffff !important; text-align: center; }
    .stTextInput input { background-color: #1e293b !important; color: white !important; border: 1px solid #00ffa2 !important; }
    div.stButton > button { background-color: #00ffa2 !important; color: #000 !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

# SCRIPT QUE ESCUCHA EL ESCÁNER
components.html("""
<script>
    window.parent.addEventListener('message', function(e) {
        if (e.data.type === 'barcode') {
            const inputs = window.parent.document.querySelectorAll('input');
            for (let input of inputs) {
                if (input.dataset.testid === "stTextInput" || input.type === "text") {
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

st.title("Find Easy 🔍")

if "cam_on" not in st.session_state: st.session_state.cam_on = False

categoria = st.radio("Seleccioná el origen:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

if st.button("✨ ABRIR / CERRAR ESCÁNER"):
    st.session_state.cam_on = not st.session_state.cam_on

if st.session_state.cam_on:
    scanner_ean.ejecutar_escaner()

# Donde cae el resultado del escaneo
producto_input = st.text_input("Buscador", placeholder="779 o nombre...", key="main_search")

if producto_input:
    nombre_final = producto_input
    if producto_input.isdigit() and len(producto_input) >= 8:
        with st.spinner('Identificando...'):
            traduccion = scanner_ean.obtener_nombre_por_ean(producto_input)
            if traduccion:
                st.info(f"📦 Producto: {traduccion}")
                nombre_final = traduccion

    st.markdown(f"### Nodos de {categoria}:")
    cols = st.columns(4)
    query = producto_input if producto_input.isdigit() else nombre_final
    
    if categoria == "Alimentos":
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/buscar?q={query}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{query}"),
            ("La Anónima", f"https://supermercado.laanonima.com.ar/buscar?busqueda={query}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigit/search?searchterm={nombre_final.replace(' ', '%20')}")
        ]
        for i, (nombre, link) in enumerate(nodos):
            with cols[i % 4]:
                st.link_button(nombre, link)

st.divider()
st.caption("QAP - Radar de Homeostasis | Matías Mittelbach © 2026")
