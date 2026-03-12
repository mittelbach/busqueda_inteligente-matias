def obtener_precio_mas_bajo(articulo):
    articulo_l = articulo.lower()
    
    # Base de datos simulada (esto luego vendrá del scraping real)
    nodos = {
        "Mercado Libre": 5200.00,
        "AliExpress": 850.00,  # Este es el "falso positivo" (ej: un molde)
        "Amazon": 5100.00
    }

    # --- LÓGICA DE EXCLUSIÓN INTELIGENTE ---
    # Si detectamos productos locales/frescos, ignoramos nodos internacionales
    productos_locales = ["queso", "carne", "leche", "pan", "fresco", "kilo"]
    
    if any(x in articulo_l for x in productos_locales):
        # Eliminamos AliExpress y Amazon de la comparativa de precio bajo
        nodos.pop("AliExpress", None)
        nodos.pop("Amazon", None)
        nodos.pop("Temu", None)

    # Si no hay nodos restantes (caso raro), devolvemos un aviso
    if not nodos:
        return "Sin nodos locales", 0

    mejor_nodo = min(nodos, key=nodos.get)
    precio_minimo = nodos[mejor_nodo]
    
    return mejor_nodo, precio_minimo
