import streamlit as st
import streamlit.components.v1 as components

def ejecutar_escaner():
    # Este código usa la versión más estable y simple de la librería
    components.html(
        """
        <script src="https://unpkg.com/html5-qrcode"></script>
        <div id="reader" style="width:100%; border-radius:10px; border:5px solid #00ffa2;"></div>
        <div id="result" style="text-align:center; color:white; font-weight:bold; margin-top:10px;">ESTADO: BUSCANDO CÓDIGO...</div>
        
        <script>
            function onScanSuccess(decodedText) {
                // Sonido y aviso inmediato
                alert("¡CÓDIGO CAPTURADO: " + decodedText + "!");
                window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
            }

            let config = { 
                fps: 20, 
                qrbox: {width: 400, height: 200},
                aspectRatio: 1.0
            };

            let scanner = new Html5QrcodeScanner("reader", config, false);
            scanner.render(onScanSuccess);
        </script>
        """,
        height=500,
    )
