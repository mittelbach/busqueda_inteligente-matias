import streamlit as st
import streamlit.components.v1 as components

# Configuración Maserati
st.set_page_config(page_title="Easy Find - Radar", layout="centered")

st.title("🔍 Easy Find: Radar de Precios")

# Inicializar el código de barras en la memoria de la sesión si no existe
if 'barcode_scan' not in st.session_state:
    st.session_state['barcode_scan'] = ""

# --- COMPONENTE DEL ESCÁNER ---
st.write("### 1. Escanear Producto")

# Este script es el que hace la magia sin instalaciones
scanner_html = """
<div id="reader" style="width: 100%;"></div>
<script src="https://unpkg.com/html5-qrcode"></script>
<script>
    const html5QrCode = new Html5Qrcode("reader");
    const qrCodeSuccessCallback = (decodedText, decodedResult) => {
        // Enviar resultado a Streamlit
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: decodedText
        }, '*');
        html5QrCode.stop();
    };
    const config = { fps: 10, qrbox: { width: 250, height: 150 } };

    // Iniciar cámara trasera automáticamente
    html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback);
</script>
"""

# Renderizamos el escáner y capturamos el valor
# Usamos un key para que Streamlit sepa qué estamos escuchando
scan_value = components.html(scanner_html, height=350)

# Actualizar el estado si el componente devuelve algo
if scan_value:
    st.session_state['barcode_scan'] = scan_value

# --- BUSCADOR ---
st.write("### 2. Resultado del Radar")
barcode = st.text_input("Código EAN detectado:", value=st.session_state['barcode_scan'], key="input_ean")

if barcode:
    st.success(f"📦 Producto identificado: {barcode}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Enlace directo a Google para que el usuario vea precios ya mismo
        link_google = f"https://www.google.com/search?q={barcode}"
        st.markdown(f"[![Google](https://img.shields.io/badge/Buscar-Google-blue)]({link_google})")
            
    with col2:
        link_ml = f"https://listado.mercadolibre.com.ar/{barcode}"
        st.markdown(f"[![ML](https://img.shields.io/badge/Ver-MercadoLibre-yellow)]({link_ml})")
        
    with col3:
        if st.button("Limpiar Radar"):
            st.session_state['barcode_scan'] = ""
            st.rerun()

st.divider()
st.info("QAP: Escaneando directamente desde el navegador (Motorola G9 / PC).")
