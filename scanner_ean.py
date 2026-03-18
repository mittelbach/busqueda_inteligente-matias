import streamlit as st
import requests
import streamlit.components.v1 as components

def obtener_nombre_por_ean(ean):
    """Traduce el código EAN a nombre de producto usando Open Food Facts"""
    try:
        url = f"https://world.openfoodfacts.org/api/v0/product/{ean}.json"
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            data = response.json()
            if data.get('status') == 1:
                return data['product'].get('product_name', None)
    except:
        pass
    return None

def ejecutar_escaner():
    st.markdown("#### 📷 Lector de Góndola")
    
    components.html(
        """
        <div id="interactive" class="viewport"></div>
        <script src="https://cdn.jsdelivr.net/npm/@ericblade/quagga2/dist/quagga.min.js"></script>
        <script>
            Quagga.init({
                inputStream: {
                    name: "Live",
                    type: "LiveStream",
                    target: document.querySelector('#interactive'),
                    constraints: { facingMode: "environment" }
                },
                decoder: { readers: ["ean_reader"] },
                locate: true
            }, function(err) {
                if (err) { console.log(err); return }
                Quagga.start();
            });

            Quagga.onDetected(function(result) {
                const code = result.codeResult.code;
                window.parent.postMessage({type: 'barcode', value: code}, '*');
            });
        </script>
        <style>
            video { width: 100%; border-radius: 12px; border: 2px solid #00ffa2; }
            canvas.drawingBuffer { display: none; }
        </style>
        """,
        height=320,
    )
    
    return st.text_input("O ingresá el número EAN a mano:", key="manual_ean_scan")
