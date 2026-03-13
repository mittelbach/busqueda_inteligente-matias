import requests

def obtener_precio_mas_bajo(articulo):
    """Detecta rubro y devuelve el mejor precio con su moneda clara."""
    articulo_l = articulo.lower()
    
    # Filtro de Tecnología / Global
    tecnologia = ["laptop", "pc", "refurbished", "notebook", "ssd", "tablet", "iphone", "resina"]
    
    if any(x in articulo_l for x in tecnologia):
        # Para global, usamos USD como referencia base
        return "AliExpress", "USD 950.00"
    
    # Filtro de Consumo Masivo (Alimentos)
    if any(x in articulo_l for x in ["queso", "paulina", "leche", "yerba"]):
        return "Distribuidor Directo", "$ 3.950,00" # Pesos AR
    
    return "Mercado Libre", "$ 5.200,00"

def generar_nodos_genealogia(nombre):
    """Mantiene la búsqueda de antepasados (Maria Cesira Giustini) universal."""
    n_plus = nombre.replace(' ', '+')
    return {
        "Antenati": f"https://antenati.cultura.gov.it/search-nominative/?nome_cognome={n_plus}",
        "FamilySearch": f"https://www.familysearch.org/search/record/results?q.anyPersona.name={n_plus}",
        "CEMLA": f"https://www.cemla.com/buscador/",
        "Geneanet": f"https://es.geneanet.org/fonds/individus/?name={n_plus}",
        "MyHeritage": f"https://www.myheritage.es/research?action=query&formId=master&qname=Name.{n_plus}",
        "PARES": f"http://pares.mcu.es/ParesBusquedas20/catalogo/search?q={n_plus}"
    }
