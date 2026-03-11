import webbrowser

def ejecutar_radar(articulo): 
    url_meli = f"https://listado.mercadolibre.com.ar/{articulo.replace(' ', '-')}"
    url_google = f"https://www.google.com.ar/search?q=precio+{articulo.replace(' ', '+')}&tbm=shop"
    
    webbrowser.open(url_meli)
    webbrowser.open(url_google)