def obtener_datos_radar(consulta):
    c_low = consulta.lower()
    
    # 🛒 MUNDO DEL CARBONO (Alimentos/Consumo Local)
    alimentos = ["queso", "leche", "fideos", "yerba", "carne", "pan", "aceite", "arroz", "yogur"]
    if any(x in c_low for x in alimentos):
        return {
            "mercado": "Nodos de Proximidad / Supermercados AR",
            "precio": "$ 4.100,00", 
            "tipo": "carbono"
        }
    
    # 💻 MUNDO DEL SILICIO (Tecnología/Global)
    tech = ["laptop", "reloj", "ssd", "refurbished", "iphone", "resina", "notebook", "tablet"]
    if any(x in c_low for x in tech):
        return {
            "mercado": "Nodos Globales (Miami / China)",
            "precio": "USD 315.00", 
            "tipo": "silicio"
        }

    return {"mercado": "Radar General", "precio": "Consultando...", "tipo": "general"}
