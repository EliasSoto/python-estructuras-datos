
# Inventario de productos
# Crea una función que reciba un diccionario con productos y sus cantidades. 
# Debe devolver la cantidad total de unidades disponibles y la cantidad de 
# productos distintos registrados.

def analizar_inventario(inventario):
    cantidad_acumulada = 0

    for cantidad in inventario.values():
        cantidad_acumulada += cantidad

    productos_distintos = len(inventario)

    return cantidad_acumulada, productos_distintos

inventario = {
    "teclado": 5,
    "raton": 8,
    "monitor": 3,
    "audifonos": 4
}

total_unidades, productos_distintos = analizar_inventario(inventario)

print("Total de unidades:", total_unidades)
print("Productos distintos:", productos_distintos)

# Resultado esperado:
# Total de unidades: 20
# Productos distintos: 4