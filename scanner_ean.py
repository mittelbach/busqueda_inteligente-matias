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
    componente_html = """
    <div id="scanner-container" style="width: 100%; font-family: sans-serif; text-align: center;">
        <div id="reader" style="width: 100%; border: 4px solid #555; border-radius: 15px; background: #000; transition: border 0.3s;"></div>
        <div id="feedback" style="margin-top: 15px; padding: 15px; border-radius: 10px; background: #262730; color: #00ffa2; font-weight: bold; font-size: 1.2rem;">
            🔍 APUNTE AL CÓDIGO DE BARRAS
        </div>
        <audio id="beep" src="https://www.soundjay.com/buttons/beep-07a.mp3" preload="auto"></audio>
    </div>

    <script src="https://unpkg.com/html5-qrcode"></script>
    <script>
        const feedback = document.getElementById('feedback');
        const readerDiv = document.getElementById('reader');
        const beep = document.getElementById('beep');

        function onScanSuccess(decodedText) {
            // 1. Feedback Visual: Borde Verde y Mensaje
            readerDiv.style.border = "6px solid #00ffa2";
            feedback.innerText = "✅ DETECTADO: " + decodedText;
            feedback.style.background = "#00ffa2";
            feedback.style.color = "#001f3f";
            
            // 2. Feedback Sonoro
            beep.play();

            // 3. Feedback Háptico (Celular)
            if (navigator.vibrate) navigator.vibrate(200);

            // 4. Envío de datos a Streamlit
            window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
            
            // 5. Pausa y reinicio limpio
            html5QrcodeScanner.clear();
            setTimeout(() => {
                location.reload(); // Recarga el componente para estar listo de nuevo
            }, 2000);
        }

        let html5QrcodeScanner = new Html5QrcodeScanner(
            "reader", 
            { 
                fps: 25, 
                qrbox: {width: 300, height: 180},
                aspectRatio: 1.33,
                formatsToSupport: [ 0, 1, 6 ] // EAN_13, EAN_8, CODE_128
            }
        );
        
        html5QrcodeScanner.render(onScanSuccess);
    </script>
    """
    components.html(componente_html, height=550)
