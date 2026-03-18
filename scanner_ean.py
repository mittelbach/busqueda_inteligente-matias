import streamlit as st
import requests
import streamlit.components.v1 as components

def obtener_nombre_por_ean(ean):
    try:
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
    st.markdown("#### 📷 Lector en Tiempo Real")
    
    # Este bloque de HTML/JS es el que fuerza la apertura en el móvil
    components.html(
        """
        <div id="reader-container" style="width: 100%; text-align: center;">
            <div id="reader" style="width: 100%; border-radius: 10px; border: 2px solid #00ffa2; background: #001f3f;"></div>
            <button id="start-btn" style="margin-top: 15px; padding: 15px; background: #00ffa2; color: #001f3f; border: none; border-radius: 8px; font-weight: bold; width: 100%;">
                ACTIVAR CÁMARA TRASERA
            </button>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const startBtn = document.getElementById('start-btn');
            const readerDiv = document.getElementById('reader');

            startBtn.addEventListener('click', () => {
                const html5QrCode = new Html5Qrcode("reader");
                const config = { fps: 15, qrbox: { width: 250, height: 150 } };

                html5QrCode.start(
                    { facingMode: "environment" }, 
                    config,
                    (decodedText) => {
                        window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                        alert("Código detectado: " + decodedText);
                        html5QrCode.stop();
                    }
                ).catch(err => {
                    console.error("Error de cámara:", err);
                    alert("Error: Asegúrate de estar en HTTPS y dar permisos de cámara.");
                });
                
                startBtn.style.display = 'none'; // Ocultar botón tras activar
            });
        </script>
        """,
        height=500,
    )
    
    # Campo para ver el resultado
    return st.text_input("Confirmá el código detectado:", key="ean_manual_res")
