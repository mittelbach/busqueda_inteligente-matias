import streamlit as st
import motor_busqueda as motor 

# Configuración de página - Estilo Mittelbach
st.set_page_config(page_title="Radar de Precios Mittelbach", layout="centered")

st.title("🌐 Centro de Mandos: Radar")
st.markdown("---")

# Entrada de Datos
with st.container():
    producto = st.text_input("¿Qué buscamos hoy, socio?", placeholder="Ej: Queso para untar, Resina dental, BTC...")
    
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
    
    # --- ANÁLISIS TÁCTICO & RADAR ---
    # Invocamos al motor para obtener el veredicto del más barato
    nodo_barato, precio_barato = motor.obtener_precio_mas_bajo(producto)
    
    if any(x in p_low for x in ["btc", "bitcoin", "xrp", "eth"]):
        st.warning("₿ **Activo de Resguardo:** Analizando mercados. Ojo con la entropía.")
    else:
        # Cuadro de veredicto dinámico (Naranja/Amarillo)
        st.warning(f"🎯 **Radar:** El precio más bajo detectado es de **${precio_barato:,.2f}** en **{nodo_barato}**.")

    # DISPARADOR AUTOMÁTICO (Google Shopping con comparación udm=28)
    if boton_disparar:
        url_shopping = f"https://www.google.com.ar/search?q=precio+{p_plus}&udm=28"
        js = f'window.open("{url_shopping}", "_blank").focus();'
        st.components.v1.html(f'<script>{js}</script>', height=0)
        st.toast(f"Escaneando comparativa para {producto}...", icon='🔍')

    # --- BLOQUE 1: NODOS DE CONSUMO (Supermercados 3x2) ---
    st.markdown("---")
    st.subheader(f"🛒 Nodos de Consumo: {producto}")
    
    supers = {
        "Coto": f"https://www.cotodigital3.com.ar/sitios/cdigital/browse?question={p_plus}",
        "Carrefour": f"https://www.carrefour.com.ar/{p_plus}",
        "Día": f"https://diaonline.supermercadosdia.com.ar/{p_plus}",
        "Cencosud": f"https://www.jumbo.com.ar/{p_plus}",
        "Coope": f"https://www.lacoopeencasa.coop/buscar?q={p_plus}",
        "La Anónima": f"https://supermercado.laanonimaonline.com/buscar?busqueda={p_plus}"
    }

    sc1, sc2 = st.columns(2)
    with sc1:
        st.link_button("🇦🇷 Coto Digital", supers["Coto"], use_container_width=True)
        st.link_button("🇫🇷 Carrefour", supers["Carrefour"], use_container_width=True)
        st.link_button("🇪🇸 Día Online", supers["Día"], use_container_width=True)
    with sc2:
        st.link_button("🏢 Cencosud (J/D/V)", supers["Cencosud"], use_container_width=True)
        st.link_button("🤝 Cooperativa Obrera", supers["Coope"], use_container_width=True)
        st.link_button("🏔️ La Anónima", supers["La Anónima"], use_container_width=True)

    # --- BLOQUE 2: NODOS GLOBALES (E-commerce 3x2)
