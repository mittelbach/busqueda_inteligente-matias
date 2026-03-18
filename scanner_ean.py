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
    # Usamos un ID único para el componente
    components.html(
        """
        <div id="reader-wrapper" style="width: 100%; font-family: sans-serif;">
            <div id="reader" style="width: 100%; border-radius: 10px; border: 2px solid #00ffa2; background: #000;"></div>
            <p id="status" style="color: #00ffa2; text-align: center; margin-top: 10px;">Cámara lista...</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const html5QrCode = new Html5Qrcode("reader");
            const config = { fps: 15, qrbox: { width: 250, height: 150 } };

            html5QrCode.start(
                { facingMode: "environment" }, 
                config,
                (decodedText) => {
                    // Enviamos el dato a Streamlit y detenemos
                    window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                    document.getElementById('status').innerText = "✅ Detectado: " + decodedText;
                    html5QrCode.stop();
                }
            ).catch(err => {
                document.getElementById('status').innerText = "❌ Error: " + err;
            });
        </script>
        """,
        height=380,
    )
