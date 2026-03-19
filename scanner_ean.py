import streamlit as st
import requests
import streamlit.components.v1 as components

def obtener_nombre_por_ean(ean):
    """Consulta Open Food Facts con manejo de errores limpio."""
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
    """Inyecta el escáner con prioridad en códigos de barras EAN-13."""
    components.html(
        """
        <div id="scanner-wrapper" style="width: 100%; text-align: center; font-family: sans-serif;">
            <div id="reader" style="width: 100%; min-height: 300px; border: 3px solid #00ffa2; border-radius: 12px; background: #000; position: relative;"></div>
            <button id="start-btn" style="margin-top: 15px; width: 100%; padding: 20px; background: #00ffa2; color: #001f3f; border: none; border-radius: 10px; font-weight: bold; font-size: 18px; cursor: pointer; box-shadow: 0px 4px 15px rgba(0, 255, 162, 0.3);">
                📸 ACTIVAR RADAR DE BARRAS
            </button>
            <p id="msg" style="color: #00ffa2; margin-top: 12px; font-weight: bold;">Estado: Listo para escanear.</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const btn = document.getElementById('start-btn');
            const msg = document.getElementById('msg');
            let scannerActive = false;
            let html5QrCode;

            btn.addEventListener('click', () => {
                if (scannerActive) return;
                
                msg.innerText = "📡 Buscando señal de cámara...";
                html5QrCode = new Html5Qrcode("reader");
                
                const config = { 
                    fps: 20, 
                    qrbox: { width: 280, height: 160 }, // Ajustado para códigos de barras alargados
                    aspectRatio: 1.0,
                    // FORZAMOS FORMATOS DE BARRAS PARA MAYOR VELOCIDAD
                    formatsToSupport: [ 0, 1, 6 ] // EAN_13, EAN_8, CODE_128
                };

                html5QrCode.start(
                    { facingMode: "environment" }, 
                    config,
                    (decodedText) => {
                        // Enviamos el dato a app_buscador.py
                        window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                        msg.innerText = "✅ DETECTADO: " + decodedText;
                        
                        // Vibración corta si el dispositivo lo permite
                        if (navigator.vibrate) navigator.vibrate(100);
                        
                        // Detener tras detección para ahorrar recursos
                        html5QrCode.stop().then(() => {
                            scannerActive = false;
                        }).catch(err => console.error("Error al detener:", err));
                    }
                ).then(() => {
                    scannerActive = true;
                    msg.innerText = "🔎 Apunte al código de barras";
                }).catch(err => {
                    msg.innerText = "❌ ERROR: " + err;
                    console.error(err);
                });
            });
        </script>
        """,
        height=480,
    )
