
# Recorre los almacenes, sus productos y las cantidades disponibles. 
# Guarda en un nuevo diccionario el nombre de cada almacén y una lista 
# con los productos cuyo stock sea inferior al promedio de stock de todos 
# los productos de ese almacén.

almacenes = {
    "Norte": {
        "Teclado": [10, 5, 8],
        "Mouse": [4, 6, 5],
        "Monitor": [12, 10, 14]
    },
    "Sur": {
        "Teclado": [3, 5, 4],
        "Mouse": [8, 10, 12],
        "Monitor": [6, 5, 7]
    }
}

promedios = {}

for nombre, almacen in almacenes.items():
    promedio_producto = []
    dicc_aux = {}
    for producto, stocks in almacen.items():
        promedio_producto.append(sum(stocks)/len(stocks))
        dicc_aux[producto] = sum(stocks)/len(stocks)

    promedio_almacen = sum(promedio_producto)/len(almacen)
    dicc_aux["promedio_almacen"] = promedio_almacen
    promedios[nombre] = dicc_aux

resultado = {}

for almacen, productos in promedios.items():
    promedio_almacen_actual = productos["promedio_almacen"]
    lista_aux = []
    for producto, promedio in productos.items():        
        if promedio < promedio_almacen_actual:
            lista_aux.append(producto)
    resultado[almacen] = lista_aux

print(resultado)


# Resultado esperado:
# {
#     "Norte": ["Teclado", "Mouse"],
#     "Sur": ["Teclado", "Monitor"]
# }

