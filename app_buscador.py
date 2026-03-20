import streamlit as st
import urllib.parse

# Configuración de Nodo - Laprida
st.set_page_config(page_title="Easy Find - Sensor de Plaza V3", layout="centered")

# BLOQUE DE COLOR: Gris oscuro forzado para los radares
st.markdown("""
<style>
    .radar-diseno {
        display: block;
        padding: 12px;
        border-radius: 8px;
        text-align: center;
        font-weight: bold;
        text-decoration: none !important;
        color: #333333 !important; /* Gris oscuro */
    }
</style>
""", unsafe_allow_html=True)

st.title("🔍 Easy Find: Sensor de Plaza")
st.caption("Protocolo SHA - Relevamiento de Homeostasis Social")

# 1. ENTRADA DE DATOS
st.markdown("### 1. Captura de Identidad")
ean_input = st.text_input("Pegá el Código EAN-13 capturado:", placeholder="Ej: 7798144810014")

if ean_input:
    ean_limpio = ean_input.strip()
    query_ean = urllib.parse.quote(ean_limpio)
    
    st.info("Paso 1: Identificar producto. Si uno falla, probá el otro:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Radar 1: Open Food Facts
        url_off = f"https://ar.openfoodfacts.org/producto/{ean_limpio}"
        st.markdown(f'''<a href="{url_off}" target="_blank" class="radar-diseno" style="background-color: #FF8C00;">🍎 Radar OpenFood</a>''', unsafe_allow_html=True)
    
    with col2:
        # Radar 2: Google Búsqueda Exacta
        url_google = f"https://www.google.com.ar/search?q=%22{ean_limpio}%22"
        st.markdown(f'''<a href="{url_google}" target="_blank" class="radar-diseno" style="background-color: #4285F4;">🔎 Radar Google</a>''', unsafe_allow_html=True)

    st.divider()

    # 2. CONFIRMACIÓN SEMÁNTICA
    st.markdown("### 2. Confirmación de Producto")
    st.write("Escribí el nombre que encontraste (ej: Bujía Bosch):")
    nombre_real = st.text_input("Nombre o Marca confirmada:", value="")
    
    if nombre_real:
        query_final = urllib.parse.quote(nombre_real)
        
        # 3. EL MOTOR DE VALOR (Vuelo a Shopping Argentina)
        st.subheader("Paso 3: Análisis de Valor de Plaza")
        url_shopping = f"https://www.google.com.ar/search?q={query_final}&tbm=shop&hl=es&gl=ar"
        
        st.markdown(f'''
            <a href="{url_shopping}" target="_blank" style="text-decoration:none;">
                <div style="background-color: #34A853; color: white; padding: 25px; border-radius: 12px; text-align: center; font-weight: bold; font-size: 1.3em; border: 2px solid #2d8e47;">
                    🛒 VER VALOR EN GOOGLE SHOPPING
                </div>
            </a>
        ''', unsafe_allow_html=True)
        st.caption(f"Buscando precios locales para: **{nombre_real}**")

else:
    st.warning("Esperando código EAN para iniciar el protocolo.")
