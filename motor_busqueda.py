def obtener_datos_radar(consulta):
    c_low = consulta.lower()
    
    # 🛒 MUNDO DEL CARBONO (Alimentos/Consumo Local)
    # Si detecta comida, el precio DEBE ser en Pesos AR y buscar en distribuidores.
    alimentos = ["queso", "leche", "fideos", "yerba", "carne", "pan", "aceite"]
    if any(x in c_low for x in alimentos):
        return {
            "mercado": "Distribuidor Directo / Supermercados AR",
            "precio": "$ 4.100,00", # Referencia local
            "tipo": "carbono"
        }
    
    # 💻 MUNDO DEL SILICIO (Tecnología/Global)
    # Si detecta tech, busca en dólares y apunta a Miami/China.
    tech = ["laptop", "reloj", "ssd", "refurbished", "iphone", "resina"]
    if any(x in c_low for x in tech):
        return {
            "mercado": "eBay / AliExpress (Global)",
            "precio": "USD 315.00", # Referencia internacional
            "tipo": "silicio"
        }

    return {"mercado": "Radar General", "precio": "Consultando...", "tipo": "general"}
