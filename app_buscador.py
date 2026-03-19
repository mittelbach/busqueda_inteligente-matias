import streamlit as st
import streamlit.components.v1 as components

# Configuración de página estilo "Maserati" (Limpio y veloz)
st.set_page_config(page_title="Easy Find - Radar", layout="centered")

st.title("🔍 Easy Find: Radar de Precios")
st.write("Escanea un producto para iniciar la búsqueda neguentrópica.")

# --- COMPONENTE DEL ESCÁNER (JavaScript + HTML5) ---
# Este bloque invoca la cámara nativa del navegador
scanner_code = """
<div id="reader" style="width: 100%;"></div>
<script src="https://unpkg.com/html5-qrcode"></script>
<script>
    function onScanSuccess(decodedText, decodedResult) {
        // Enviamos el código detectado a Streamlit
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: decodedText
        }, '*');
        // Detenemos el escáner tras el éxito
        html5QrcodeScanner.clear();
    }

    let html5QrcodeScanner = new Html5QrcodeScanner(
        "reader", { fps: 10, qrbox: 250 });
    html5QrcodeScanner.render(onScanSuccess);
</script>
"""

# Renderizamos el escáner en la app
resultado_escaneo = components.html(scanner_code, height=450)

# --- LÓGICA DE BÚSQUEDA ---
# Si detecta un código, lo pone en el buscador automáticamente
barcode = st.text_input("Código detectado / Ingresar manualmente:", value=resultado_escaneo if resultado_escaneo else "")

if barcode:
    st.success(f"Producto detectado: {barcode}")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Buscar en Google"):
            st.write(f"Buscando {barcode}...")
            # Aquí irá tu lógica de scraping del AHG
            
    with col2:
        st.button("Ver en Mercado Libre")
        
    with col3:
        st.button("Historial de Precios")

st.info("QAP: Sistema listo para escaneo desde Motorola G9 / Laptop.")
