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
    # Inyectamos el componente que invoca permisos y escanea
    components.html(
        """
        <div id="scanner-container" style="width: 100%; text-align: center; font-family: sans-serif;">
            <div id="interactive" style="width: 100%; height: 300px; border: 2px solid #00ffa2; border-radius: 10px; background: #000; overflow: hidden;"></div>
            <button id="btn-permiso" style="margin-top: 15px; width: 100%; padding: 15px; background: #00ffa2; color: #001f3f; border: none; border-radius: 8px; font-weight: bold; cursor: pointer; font-size: 16px;">
                📸 ACTIVAR ESCÁNER (PEDIR PERMISO)
            </button>
            <p id="feedback" style="color: #00ffa2; margin-top: 10px; font-size: 14px;">Estado: Esperando permiso de hardware...</p>
        </div>

        <script src="https://unpkg.com/html5-qrcode"></script>
        <script>
            const btn = document.getElementById('btn-permiso');
            const feedback = document.getElementById('feedback');
            
            btn.addEventListener('click', async () => {
                feedback.innerText = "Invocando sistema de permisos...";
                
                try {
                    // SENTENCIA CLAVE: Invoca el sistema de permisos del celular
                    const stream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } });
                    // Si llegamos acá, el usuario dio permiso. Frenamos el stream temporal para dárselo al scanner.
                    stream.getTracks().forEach(track => track.stop()); 

                    const html5QrCode = new Html5Qrcode("interactive");
                    const config = { 
                        fps: 20, 
                        qrbox: { width: 250, height: 150 }, 
                        aspectRatio: 1.0 
                    };

                    await html5QrCode.start(
                        { facingMode: "environment" }, 
                        config,
                        (decodedText) => {
                            // Enviamos el dato al buscador principal
                            window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
                            feedback.innerText = "✅ Código capturado: " + decodedText;
                            html5QrCode.stop();
                            btn.style.display = 'block';
                            btn.innerText = "ESCANEAR OTRO";
                        }
                    );
                    btn.style.display = 'none';
                    feedback.innerText = "Escaneando... Apuntá al código de barras.";

                } catch (err) {
                    feedback.innerText = "❌ Permiso denegado o error de hardware.";
                    console.error(err);
                }
            });
        </script>
        """,
        height=450,
    )
