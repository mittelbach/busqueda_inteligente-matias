import st_components_html as sc
import requests

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
    # Inyectamos el componente sin session_state
    sc.html(
        """
        <div id="wrapper" style="width: 100%; text-align: center; font-family: sans-serif;">
            <div id="reader" style="width: 100%; border-radius: 10px; border: 2px solid #00ffa2; background: #000; min-height: 250px;"></div>
            <button id="start-btn" style="margin-top: 20px; width: 100%; padding: 18px; background: #00ffa2; color: #001f3f; border: none; border-radius: 10px; font-weight: bold; font-size: 18px; cursor: pointer;">
                📸 ACTIVAR ESCÁNER
            </button>
            <p id="status-msg" style="color: #00ffa2; margin-top: 15px; font-size: 14px;">Listo para escanear góndola.</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const startBtn = document.getElementById('start-btn');
            const statusMsg = document.getElementById('status-msg');

            startBtn.addEventListener('click', async () => {
                statusMsg.innerText = "Iniciando hardware...";
                const html5QrCode = new Html5Qrcode("reader");
                
                const config = { 
                    fps: 15, 
                    qrbox: { width: 250, height: 150 },
                    aspectRatio: 1.0 
                };

                try {
                    await html5QrCode.start(
                        { facingMode: "environment" }, 
                        config,
                        (decodedText) => {
                            // Enviar al padre (Streamlit)
                            window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                            statusMsg.innerText = "✅ CAPTURADO: " + decodedText;
                            html5QrCode.stop();
                            startBtn.style.display = 'block';
                            startBtn.innerText = "ESCANEAR OTRO";
                        }
                    );
                    startBtn.style.display = 'none';
                    statusMsg.innerText = "Buscando barras...";
                } catch (err) {
                    statusMsg.innerText = "❌ Error: Permisos o Hardware";
                }
            });
        </script>
        """,
        height=450,
    )
