import streamlit as st
import requests
import streamlit.components.v1 as components

def obtener_nombre_por_ean(ean):
    try:
        url = f"https://world.openfoodfacts.org/api/v0/product/{str(ean).strip()}.json"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 1:
                return data['product'].get('product_name', None)
    except:
        pass
    return None

def ejecutar_escaner():
    # El secreto está en este bloque: fuerza la cámara trasera ('environment')
    components.html(
        """
        <div id="scanner-wrapper" style="width: 100%; text-align: center;">
            <div id="reader" style="width: 100%; border-radius: 10px; border: 2px solid #00ffa2; background: #000;"></div>
            <button id="start-scan" style="margin-top: 15px; width: 100%; padding: 20px; background: #00ffa2; color: #001f3f; border: none; border-radius: 10px; font-weight: bold; font-size: 16px;">
                📸 PULSAR PARA ESCANEAR PRODUCTO
            </button>
            <p id="msg" style="color: #00ffa2; margin-top: 10px;">Estado: Esperando acción del usuario...</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const btn = document.getElementById('start-scan');
            const msg = document.getElementById('msg');

            btn.addEventListener('click', () => {
                msg.innerText = "Iniciando hardware de cámara...";
                const html5QrCode = new Html5Qrcode("reader");
                
                const config = { 
                    fps: 20, 
                    qrbox: { width: 280, height: 180 },
                    aspectRatio: 1.0 
                };

                // Intentamos abrir la cámara trasera directamente
                html5QrCode.start(
                    { facingMode: "environment" }, 
                    config,
                    (decodedText) => {
                        // Enviamos el código al buscador principal
                        window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                        msg.innerText = "✅ ¡CÓDIGO CAPTURADO!";
                        btn.style.display = 'block';
                        btn.innerText = "ESCANEAR OTRO";
                        html5QrCode.stop();
                    }
                ).catch(err => {
                    msg.innerText = "❌ Error: " + err;
                });
                
                btn.style.display = 'none';
            });
        </script>
        """,
        height=480,
    )
