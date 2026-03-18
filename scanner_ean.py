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
    # El componente ahora es autocontenido para evitar errores de importación
    components.html(
        """
        <div id="scanner-wrapper" style="width: 100%; text-align: center; font-family: sans-serif;">
            <div id="reader" style="width: 100%; min-height: 250px; border: 2px solid #00ffa2; border-radius: 10px; background: #000;"></div>
            <button id="action-btn" style="margin-top: 15px; width: 100%; padding: 18px; background: #00ffa2; color: #001f3f; border: none; border-radius: 10px; font-weight: bold; font-size: 16px; cursor: pointer;">
                📸 ACTIVAR CÁMARA TRASERA
            </button>
            <p id="status" style="color: #00ffa2; margin-top: 10px;">Listo para iniciar hardware.</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const btn = document.getElementById('action-btn');
            const status = document.getElementById('status');
            let html5QrCode;

            btn.addEventListener('click', async () => {
                status.innerText = "Sincronizando permisos...";
                try {
                    // Pedimos permiso al sistema operativo del celular
                    const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
                    stream.getTracks().forEach(track => track.stop());

                    html5QrCode = new Html5Qrcode("reader");
                    const config = { fps: 20, qrbox: { width: 250, height: 150 }, aspectRatio: 1.0 };

                    await html5QrCode.start(
                        { facingMode: "environment" }, 
                        config,
                        (decodedText) => {
                            window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                            status.innerText = "✅ CAPTURADO: " + decodedText;
                            html5QrCode.stop();
                        }
                    );
                    btn.style.display = 'none';
                    status.innerText = "Buscando código de barras...";
                } catch (err) {
                    status.innerText = "❌ ERROR: Permití la cámara en los ajustes del navegador.";
                }
            });
        </script>
        """,
        height=450,
    )
