import streamlit as st
import motor_busqueda as motor 

st.set_page_config(page_title="Radar + Análisis", layout="centered")

st.title("🌐 Centro de Mandos: Radar + IA")
st.markdown("---")

with st.container():
    producto = st.text_input("Ingresá el producto:", placeholder="Ej: Reloj Addiesdive")
    
    col1, col2 = st.columns(2)
    with col1:
        boton_disparar = st.button("🚀 Lanzar Radar Base")
    with col2:
        boton_limpiar = st.button("🧹 Nueva Búsqueda")

if producto:
    # --- MÓDULO DE ANÁLISIS TÁCTICO (VERSIÓN SEGURA) ---
    p_low = producto.lower()
    
    if "reloj" in p_low:
        st.success("⌚ **Análisis Táctico:** Mercado de alta volatilidad. Si el precio local supera los $65.000, los nodos de AliExpress suelen ser la opción más eficiente.")
    elif any(x in p_low for x in ["diente", "dental", "protesis", "resina"]):
        st.warning("🦷 **Insumo Especializado:** Detectado rubro odontológico. Se recomienda priorizar el nodo de Tiendamia para comparar costos de importación.")
    else:
        st.info("📊 **Análisis General:** Mercado estable. Se recomienda comparar el precio de Google Shopping con el envío de Tiendamia.")

    st.markdown("---")
    st.subheader(f"🎯 Nodos de Información para: {producto}")
    
    p_plus = producto.replace(' ', '+')
    p_dash = producto.replace(' ', '-')

    urls = {
        "Mercado Libre": f"https://listado.mercadolibre.com.ar/{p_dash}",
        "Google Shopping": f"https://www.google.com.ar/search?q=precio+{p_plus}&tbm=shop",
        "Amazon": f"https://www.amazon.com/s?k={p_plus}",
        "eBay": f"https://www.ebay.com/sch/i.html?_nkw={p_plus}",
        "Temu": f"https://www.temu.com/search_result.html?search_key={p_plus}",
        "AliExpress": f"https://es.aliexpress.com/w/wholesale-{p_dash}.html",
        "Tiendamia": f"https://tiendamia.com/ar/search?amz={p_plus}"
    }

    c1, c2, c3 = st.columns(3)
    with c1: st.markdown(f"🇦🇷 [Mercado Libre]({urls['Mercado Libre']})")
    with c2: st.markdown(f"🔍 [Google Shopping]({urls['Google Shopping']})")
    with c3: st.markdown(f"✈️ [Tiendamia]({urls['Tiendamia']})")

    c4, c5, c6, c7 = st.columns(4)
    with c4: st.markdown(f"📦 [Amazon]({urls['Amazon']})")
    with c5: st.markdown(f"🛒 [eBay]({urls['eBay']})")
    with c6: st.markdown(f"🧡 [Temu]({urls['Temu']})")
    with c7: st.markdown(f"🇨🇳 [AliExpress]({urls['AliExpress']})")

    if boton_disparar:
        motor.ejecutar_radar(producto)
        st.toast("Radar disparado...", icon='🚀')

st.markdown("---")
st.caption("QAP - Inteligencia de Precios Activa (Modo Seguro)")