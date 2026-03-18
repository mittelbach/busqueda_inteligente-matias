import streamlit as st
import requests
import streamlit.components.v1 as components

def obtener_nombre_por_ean(ean):
    """Consulta Open Food Facts para traducir EAN a nombre de producto"""
    try:
        # Limpiamos el código por si trae espacios
        ean_clean = str(ean).strip()
        url = f"https://world.openfoodfacts.org/api/v0/product/{ean_clean}.json"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 1:
                return data['product'].get('product_name', None)
    except:
        pass
    return None

def ejecutar_escaner():
    st.markdown("#### 📷 Lector Inteligente (Barras / QR)")
    
    # Componente HTML con la librería html5-qrcode
    # Esta versión es la más compatible con navegadores móviles (iOS/Android)
    components.html(
        """
        <script src="https://unpkg.com/html5-qrcode"></script>
        <div id="reader" style="width: 100%; border-radius: 12px; border: 2px solid #00ffa2; background: #001f3f;"></div>
        <div id="result" style="color: #00ffa2; font-weight: bold; margin-top: 10px; text-align: center;"></div>

        <script>
            const html5QrCode = new Html5Qrcode("reader");
            const qrCodeSuccessCallback = (decodedText, decodedResult) => {
                // Enviamos el dato a la interfaz de Streamlit
                window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                document.getElementById('result').innerText = "✅ Código detectado: " + decodedText;
                html5QrCode.stop(); 
            };
            
            const config = { 
                fps: 15, 
                qrbox: { width: 280, height: 160 },
                aspectRatio: 1.0
            };

            // Iniciamos con la cámara trasera por defecto (ideal para celular)
            html5QrCode.start({ facingMode: "environment" }, config, qrCodeSuccessCallback);
        </script>
        
        <style>
            #reader__dashboard_section_csr button {
                background-color: #484848 !important;
                color: #00ffa2 !important;
                border: 1px solid #00ffa2 !important;
                padding: 10px;
                border-radius: 5px;
                cursor: pointer;
                margin: 10px;
            }
            #reader__status_span { color: #ffffff !important; font-family: sans-serif; }
            video { border-radius: 10px; }
        </style>
        """,
        height=450,
    )
    
    return st.text_input("Confirmar código o ingreso manual:", key="ean_manual_input")
