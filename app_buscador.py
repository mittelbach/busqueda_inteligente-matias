import streamlit as st
import motor_busqueda as motor 

# Mantenemos tu configuración original
st.set_page_config(page_title="Radar de Precios Mittelbach", layout="centered")

st.title("🌐 Centro de Mandos: Radar")
st.markdown("---")

with st.container():
    producto = st.text_input("¿Qué buscamos hoy, socio?", placeholder="Ej: Queso cremoso, Resina, BTC...")
    col1, col2 = st.columns(2)
    with col1:
        boton_disparar = st.button("🚀 Lanzar Radar", use_container_width=True)
    with col2:
        if st.button("🧹 Limpiar", use_container_width=True):
            st.rerun()

if producto:
    p_low = producto.lower()
    p_plus = producto.replace(' ', '+')
    p_dash = producto.replace(' ', '-')
    
    # --- ANÁLISIS TÁCTICO (Tu diseño original) ---
    nodo_barato, precio_barato = motor.obtener_precio_mas_bajo(producto)
    
    if any(x in p_low for x in ["btc", "bitcoin", "xrp"]):
        st.warning("₿ **Activo de Resguardo:** Analizando mercados cripto.")
    else:
        # El cuadro naranja/amarillo que te gustó
        st.warning(f"🎯 **Radar:** {nodo_barato} tiene la opción más barata (${precio_barato:,.2f})")

    if boton_disparar:
        js = f'window.open("https://www.google.com.ar/search?q=precio+{p_plus}&tbm=shop", "_blank").focus();'
        st.components.v1.html(f'<script>{js}</script>', height=0)

    # --- SECCIÓN SUPERMERCADOS (Simetría 3x2) ---
    st.markdown("---")
    st.subheader(f"🛒 Nodos de Consumo: {producto}")
    
    # URLs configuradas para búsqueda directa
    supers = {
        "Coto": f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={p_plus}",
        "Carrefour": f"https://www.carrefour.com.ar/{p_plus}",
        "Día": f"https://diaonline.supermercadosdia.com.ar/{p_plus}",
        "Cencosud": f"https://www.jumbo.com.ar/{p_plus}",
        "Coope": f"https://www.lacoopeencasa.coop/buscar?q={p_plus}",
        "La Anónima": f"https://supermercado.laanonimaonline.com/buscar?busqueda={p_plus}"
    }

    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🇦🇷 Coto Digital", supers["Coto"], use_container_width=True)
        st.link_button("🇫🇷 Carrefour", supers["Carrefour"], use_container_width=True)
        st.link_button("🇪🇸 Día Online", supers["Día"], use_container_width=True)
    with c2:
        st.link_button("🏢 Cencosud", supers["Cencosud"], use_container_width=True)
        st.link_button("🤝 Cooperativa Obrera", supers["Coope"], use_container_width=True)
        st.link_button("🏔️ La Anónima", supers["La Anónima"], use_container_width=True)

    # --- SECCIÓN GLOBAL (Tu diseño original) ---
    st.markdown("---")
    st.subheader(f"🌎 Nodos Globales")
    
    g1, g2 = st.columns(2)
    with g1:
        st.link_button("🇦🇷 Mercado Libre", f"https://listado.mercadolibre.com.ar/{p_dash}", use_container_width=True)
        st.link_button("✈️ Tiendamia", f"https://tiendamia.com/ar/search?amz={p_plus}", use_container_width=True)
        st.link_button("🧡 Temu", f"https://www.temu.com/search_result.html?search_key={p_plus}", use_container_width=True)
    with g2:
        st.link_button("🇨🇳 AliExpress", f"https://es.aliexpress.com/w/wholesale-{p_dash}.html", use_container_width=True)
        st.link_button("📦 Amazon", f"https://www.amazon.com/s?k={p_plus}", use_container_width=True)
        st.link_button("🛒 eBay", f"https://www.ebay.com/sch/i.html?_nkw={p_plus}", use_container_width=True)

st.markdown("---")
st.caption("QAP - Protocolo SMLabs v3.5 | Nodos de Consumo Activados")
