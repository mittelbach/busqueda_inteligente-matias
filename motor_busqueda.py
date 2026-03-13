import requests

def obtener_precio_mas_bajo(articulo):
    """
    Ya no usa valores fijos. Detecta rubro y sugiere el mejor nodo 
    para confirmar el precio real en la pestaña que se abre.
    """
    articulo_l = articulo.lower()
    
    # Tecnología / Global
    if any(x in articulo_l for x in ["addiesdive", "reloj", "laptop", "refurbished", "resina"]):
        return "Nodos Globales (eBay/AliExpress)", "Confirmar USD en Radar"
    
    # Consumo / Local
    if any(x in articulo_l for x in ["queso", "paulina", "leche", "yerba"]):
        return "Supermercados (AR)", "Confirmar AR$ en Radar"
    
    return "Analizando...", "Consultando..."

def generar_nodos_identidad(nombre):
    """Mantenemos la búsqueda de antepasados (Giustini) activa."""
    n_plus = nombre.replace(' ', '+')
    return {
        "Antenati": f"https://antenati.cultura.gov.it/search-nominative/?nome_cognome={n_plus}",
        "FamilySearch": f"https://www.familysearch.org/search/record/results?q.anyPersona.name={n_plus}",
        "CEMLA": f"https://www.cemla.com/buscador/",
        "Geneanet": f"https://es.geneanet.org/fonds/individus/?name={n_plus}"
    }
