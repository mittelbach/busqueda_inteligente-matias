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
    # Este bloque incluye un 'allow' explícito para la cámara
    components.html(
        """
        <div id="scanner-wrapper" style="width: 100%; text-align: center;">
            <div id="reader" style="width: 100%; border-radius: 10px; border: 2px solid #00ffa2; background: #000;"></div>
            <button id="start-scan" style="margin-top: 15px; width: 100%; padding: 20px; background: #00ffa2; color: #001f3f; border: none; border-radius: 10px; font-weight: bold; font-size: 16px;">
                📸 ACTIVAR LENTE TRASERO
            </button>
            <p id="msg" style="color: #00ffa2; margin-top: 10px;">Estado: Esperando permiso de hardware...</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const btn = document.getElementById('start-scan');
            const msg = document.getElementById('msg');

            btn.addEventListener('click', async () => {
                msg.innerText = "Solicitando permisos al sistema...";
                
                try {
                    // Forzamos el pedido de permiso nativo antes de iniciar el scanner
                    await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
                    
                    const html5QrCode = new Html5Qrcode("reader");
                    const config = { 
                        fps: 20, 
                        qrbox: { width: 250, height: 150 },
                        aspectRatio: 1.0 
                    };

                    await html5QrCode.start(
                        { facingMode: "environment" }, 
                        config,
                        (decodedText) => {
                            window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                            msg.innerText = "✅ ¡CAPTURADO!";
                            html5QrCode.stop();
                            btn.style.display = 'block';
                        }
                    );
                    btn.style.display = 'none';
                } catch (err) {
                    msg.innerText = "❌ ERROR: " + err.name + " - " + err.message;
                    console.error(err);
                }
            });
        </script>
        """,
        height=450,
        scrolling=False,
    )
