import streamlit as st
import scanner_ean 
import streamlit.components.v1 as components

# --- ESTILO ---
st.set_page_config(page_title="Find Easy 🔍", page_icon="🔍", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b1622 !important; }
    h1 { color: #ffffff !important; text-align: center; font-weight: 800; }
    .stTextInput input { background-color: #1e293b !important; color: white !important; border: 1px solid #00ffa2 !important; }
    div.stButton > button { background-color: #00ffa2 !important; color: #001f3f !important; font-weight: bold !important; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# PUENTE DE DATOS
components.html("""
<script>
    window.parent.addEventListener('message', function(e) {
        if (e.data.type === 'barcode') {
            const inputs = window.parent.document.querySelectorAll('input');
            for (let input of inputs) {
                if (input.type === "text") {
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

if "ver_esc" not in st.session_state: st.session_state.ver_esc = False

cat = st.radio("Origen:", ["Tecno y Vestimenta", "Alimentos"], horizontal=True)

if st.button("✨ ACTIVAR ESCÁNER"):
    st.session_state.ver_esc = not st.session_state.ver_esc

if st.session_state.ver_esc:
    scanner_ean.ejecutar_escaner()

query = st.text_input("Buscador", placeholder="779 o producto...", key="search_main")

if query:
    nombre_final = query
    if query.isdigit() and len(query) >= 8:
        with st.spinner('Buscando en base de datos...'):
            res = scanner_ean.obtener_nombre_por_ean(query)
            if res:
                st.info(f"📦 Producto: {res}")
                nombre_final = res

    st.markdown(f"### Nodos de {cat}:")
    cols = st.columns(4)
    q_final = query if query.isdigit() else nombre_final
    
    if cat == "Alimentos":
        nodos = [
            ("Carrefour", f"https://www.carrefour.com.ar/buscar?q={q_final}"),
            ("Jumbo", f"https://www.jumbo.com.ar/{q_final}"),
            ("La Anónima", f"https://supermercado.laanonima.com.ar/buscar?busqueda={q_final}"),
            ("Coto", f"https://www.cotodigital3.com.ar/sitios/cdigit/search?searchterm={nombre_final.replace(' ', '%20')}")
        ]
        for i, (n, l) in enumerate(nodos):
            with cols[i % 4]: st.link_button(n, l)

st.divider()
st.caption("QAP - Matías Mittelbach © 2026")
