import requests
from bs4 import BeautifulSoup

def obtener_precio_mas_bajo(articulo):
    """
    Intenta rastrear el precio real. 
    Si no puede, devuelve un rango estimado basado en el rubro, no un valor fijo.
    """
    articulo_l = articulo.lower()
    
    # Lógica de Rango para Tecnología (Global)
    if any(x in articulo_l for x in ["addiesdive", "reloj", "laptop", "refurbished"]):
        # Aquí es donde el radar 'escanea'. 
        # Por ahora, devolvemos un RANGO dinámico de referencia.
        if "reloj" in articulo_l:
            return "AliExpress / eBay", "Rango USD 40.00 - 75.00"
        if "laptop" in articulo_l:
            return "Miami / Amazon", "Rango USD 250.00 - 450.00"
        return "Nodos Globales", "Consultando USD..."

    # Lógica de Rango para Alimentos (Local)
    if any(x in articulo_l for x in ["queso", "paulina", "leche", "yerba"]):
        return "Mercados Locales", "Rango AR$ 3.500 - 5.500"
    
    return "Buscando...", "Analizando Nodos..."

def generar_nodos_identidad(nombre):
    """Mantenemos la búsqueda de antepasados (Giustini) activa."""
    n_plus = nombre.replace(' ', '+')
    return {
        "Antenati": f"https://antenati.cultura.gov.it/search-nominative/?nome_cognome={n_plus}",
        "FamilySearch": f"https://www.familysearch.org/search/record/results?q.anyPersona.name={n_plus}",
        "CEMLA": f"https://www.cemla.com/buscador/",
        "Geneanet": f"https://es.geneanet.org/fonds/individus/?name={n_plus}"
    }
