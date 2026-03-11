# ... (Mantené todo lo anterior igual)

    st.markdown("---")
    st.subheader(f"🎯 Nodos de Información para: {producto}")
    
    # Creamos botones de acceso rápido (Look & Feel de App Móvil)
    col1, col2 = st.columns(2)
    
    with col1:
        st.link_button("🇦🇷 Mercado Libre", urls['Mercado Libre'], use_container_width=True)
        st.link_button("🔍 Google Shopping", urls['Google Shopping'], use_container_width=True)
        st.link_button("✈️ Tiendamia", urls['Tiendamia'], use_container_width=True)

    with col2:
        st.link_button("📦 Amazon", urls['Amazon'], use_container_width=True)
        st.link_button("🇨🇳 AliExpress", urls['AliExpress'], use_container_width=True)
        st.link_button("🧡 Temu", urls['Temu'], use_container_width=True)

    st.info("💡 Como estamos en la nube, hacé clic en el nodo que quieras explorar manualmente.")
