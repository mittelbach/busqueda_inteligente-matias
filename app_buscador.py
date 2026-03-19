import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Easy Find - Radar", layout="centered")

st.title("🔍 Easy Find: Radar")

# El secreto: Un componente HTML puro que invoca la cámara nativa del móvil
st.markdown("### Escaneá el código de barras")

scanner_html = """
<div id="interactive" class="viewport"></div>
<script src="https://cdn.jsdelivr.net/npm/@ericblade/quagga2/dist/quagga.min.js"></script>
<script>
    Quagga.init({
        inputStream: {
            name: "Live",
            type: "LiveStream",
            target: document.querySelector('#interactive'),
            constraints: { facingMode: "environment" } // FUERZA CÁMARA TRASERA
        },
        decoder: { readers: ["ean_reader"] }
    }, function(err) {
        if (err) { console.log(err); return }
        Quagga.start();
    });

    Quagga.onDetected(function(result) {
        var code = result.codeResult.code;
        window.parent.postMessage({
            type: 'streamlit:setComponentValue',
            value: code
        }, '*');
    });
</script>
<style>
    canvas.drawingBuffer { display: none; }
    video { width: 100% !important; border-radius: 10px; }
</style>
"""

# Capturamos el dato del escaneo
dato_barcode = components.html(scanner_html, height=300)

if dato_barcode:
    st.success(f"✅ ¡Capturado!: {dato_barcode}")
    st.link_button(f"🔍 Ver Precios de {dato_barcode}", f"https://www.google.com/search?q={dato_barcode}")
else:
    st.info("Apuntá al código de barras. El sistema detectará el número automáticamente.")
