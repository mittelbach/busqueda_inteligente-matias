def obtener_precio_mas_bajo(articulo):
    articulo_l = articulo.lower()
    
    # Base de datos de escaneo (v3.5)
    nodos = {
        "Mercado Libre": 5200.00,
        "Coto": 4850.00,
        "Carrefour": 4700.00,
        "AliExpress": 950.00 # Falso positivo (ej: molde para queso)
    }

    # FILTRO DE PERTINENCIA: Si es comida o productos de "kilo", descartamos China del radar
    filtro_local = ["queso", "leche", "kilo", "yerba", "carne", "fresco", "pan", "crema"]
    
    if any(x in articulo_l for x in filtro_local):
        nodos.pop("AliExpress", None)
        nodos.pop("Temu", None)
        nodos.pop("Amazon", None)

    # Identificamos el nodo más barato de los restantes
    mejor_nodo = min(nodos, key=nodos.get)
    precio_minimo = nodos[mejor_nodo]
    
    return mejor_nodo, precio_minimo
