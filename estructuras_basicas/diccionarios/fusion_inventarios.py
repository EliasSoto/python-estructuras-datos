
# Fusionador de inventarios
# Dos sucursales administran sus inventarios mediante diccionarios. 
# Las claves son los códigos de productos y los valores, sus cantidades.
# Crea una función que combine ambos inventarios. Si un producto aparece 
# en las dos sucursales, sus cantidades deben sumarse. Si aparece solo en una, 
# su cantidad debe conservarse.

def fusionar_inventarios(inventario_a, inventario_b):
    inventario_fusionado = inventario_a.copy()

    for codigo_producto, cantidad in inventario_b.items():
        if codigo_producto in inventario_fusionado:
            inventario_fusionado[codigo_producto] += cantidad
        else:
            inventario_fusionado[codigo_producto] = cantidad

    return inventario_fusionado

inventario_a = {
    "P001": 10,
    "P002": 5,
    "P003": 8,
    "P005": 2
}

inventario_b = {
    "P002": 7,
    "P003": 4,
    "P004": 6
}

resultado = fusionar_inventarios(inventario_a, inventario_b)

print(resultado)
print("Inventario A original:", inventario_a)
print("Inventario B original:", inventario_b)


# Resultado esperado:
# {'P001': 10, 'P002': 12, 'P003': 12, 'P005': 2, 'P004': 6}
# Inventario A original: {'P001': 10, 'P002': 5, 'P003': 8, 'P005': 2}
# Inventario B original: {'P002': 7, 'P003': 4, 'P004': 6}