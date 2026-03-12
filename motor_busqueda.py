import webbrowser

def obtener_precio_mas_bajo(articulo):
    # En una fase avanzada, aquí se integrará el scraping real.
    # Por ahora, simulamos la detección para activar el cuadro naranja del dashboard.
    nodos_simulados = {
        "Mercado Libre": 5000.00,
        "AliExpress": 4850.00,
        "Amazon": 5200.00
    }
    
    # Buscamos el mínimo valor
    mejor_nodo = min(nodos_simulados, key=nodos_simulados.get)
    precio_minimo = nodos_simulados[mejor_nodo]
    
    return mejor_nodo, precio_minimo

def ejecutar_radar(articulo): 
    url_meli = f"https://listado.mercadolibre.com.ar/{articulo.replace(' ', '-')}"
    url_google = f"https://www.google.com.ar/search?q=precio+{articulo.replace(' ', '+')}&tbm=shop"
    
    webbrowser.open(url_meli)
    webbrowser.open(url_google)
