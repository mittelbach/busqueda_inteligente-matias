def ejecutar_escaner():
    componente_html = """
    <div id="scanner-container" style="width: 100%; font-family: sans-serif; text-align: center;">
        <div id="reader" style="width: 100%; border: 4px solid #00ffa2; border-radius: 15px; background: #000; overflow: hidden;"></div>
        <div id="feedback" style="margin-top: 15px; padding: 15px; border-radius: 10px; background: #262730; color: #ffffff; font-weight: bold;">
            📡 MODO RADAR: ALEJE EL PRODUCTO (30-40 CM) PARA QUE HAGA FOCO
        </div>
        <audio id="beep" src="https://www.soundjay.com/buttons/beep-07a.mp3" preload="auto"></audio>
    </div>

    <script src="https://unpkg.com/html5-qrcode"></script>
    <script>
        const feedback = document.getElementById('feedback');
        const readerDiv = document.getElementById('reader');
        const beep = document.getElementById('beep');

        function onScanSuccess(decodedText) {
            readerDiv.style.border = "8px solid #00ffa2";
            feedback.innerText = "✅ PRODUCTO DETECTADO: " + decodedText;
            feedback.style.background = "#00ffa2";
            feedback.style.color = "#001f3f";
            beep.play();
            window.parent.postMessage({type: 'barcode', value: decodedText}, '*');
        }

        let html5QrcodeScanner = new Html5QrcodeScanner(
            "reader", 
            { 
                fps: 30, 
                // Agrandamos el marco para que captures desde lejos
                qrbox: {width: 450, height: 250}, 
                aspectRatio: 1.33,
                formatsToSupport: [ 0, 1, 6 ] // Prioridad absoluta a EAN_13
            }
        );
        html5QrcodeScanner.render(onScanSuccess);
    </script>
    """
    components.html(componente_html, height=580)
