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
    # Usamos el componente oficial con un listener de alta velocidad
    components.html(
        """
        <div id="wrapper" style="width: 100%; text-align: center; font-family: sans-serif;">
            <div id="reader" style="width: 100%; border-radius: 10px; border: 2px solid #00ffa2; background: #000; min-height: 250px;"></div>
            <button id="start-btn" style="margin-top: 20px; width: 100%; padding: 18px; background: #00ffa2; color: #001f3f; border: none; border-radius: 10px; font-weight: bold; font-size: 18px; cursor: pointer;">
                📸 ACTIVAR LENTE DE GÓNDOLA
            </button>
            <p id="status-msg" style="color: #00ffa2; margin-top: 15px; font-size: 14px;">QAP - Esperando activación de hardware.</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const startBtn = document.getElementById('start-btn');
            const statusMsg = document.getElementById('status-msg');

            startBtn.addEventListener('click', async () => {
                statusMsg.innerText = "Sincronizando con la cámara...";
                const html5QrCode = new Html5Qrcode("reader");
                
                const config = { 
                    fps: 20, 
                    qrbox: { width: 280, height: 160 },
                    aspectRatio: 1.0 
                };

                try {
                    await html5QrCode.start(
                        { facingMode: "environment" }, 
                        config,
                        (decodedText) => {
                            // Comunicación directa con el buscador padre
                            window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                            statusMsg.innerText = "✅ Detectado: " + decodedText;
                            html5QrCode.stop();
                            startBtn.style.display = 'block';
                            startBtn.innerText = "ESCANEAR OTRO";
                        }
                    );
                    startBtn.style.display = 'none';
                    statusMsg.innerText = "Buscando patrón de barras...";
                } catch (err) {
                    statusMsg.innerText = "❌ Error: Verificá los permisos de cámara en el navegador.";
                }
            });
        </script>
        """,
        height=450,
    )
