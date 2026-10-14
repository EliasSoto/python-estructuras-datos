
# Dos sucursales de una empresa tienen inventarios representados 
# mediante conjuntos de códigos de productos.

# Crea una función que compare ambos inventarios y determine:
# Productos disponibles en ambas sucursales.
# Productos exclusivos de la primera sucursal.
# Productos exclusivos de la segunda sucursal.
# Todos los productos disponibles.
# Si ambos inventarios son exactamente iguales.

# No debes modificar los conjuntos originales.

def comparar_inventarios(inventario_a, inventario_b):
    ambas_sucursales = inventario_a & inventario_b
    solo_a = inventario_a - inventario_b
    solo_b = inventario_b - inventario_a
    todos = inventario_a | inventario_b
    iguales = inventario_a == inventario_b

    return ambas_sucursales, solo_a, solo_b, todos, iguales

inventario_a = {"P001", "P002", "P003", "P004", "P005"}
inventario_b = {"P003", "P004", "P005", "P006", "P007"}

ambas_sucursales, solo_a, solo_b, todos, iguales = (
    comparar_inventarios(inventario_a, inventario_b)
)

respuesta = f"""En ambas sucursales están: {ambas_sucursales}
Los que están solo en A: {solo_a}
Los que están solo en B: {solo_b}
Todos los productos de ambas sucursales: {todos}
¿Los inventarios son iguales?: {"Sí" if iguales else "No"}
"""

print(respuesta)

# Resultado esperado:
# Comunes: {'P003', 'P004', 'P005'}
# Solo A: {'P001', 'P002'}
# Solo B: {'P006', 'P007'}
# Todos: {'P001', 'P002', 'P003', 'P004', 'P005', 'P006', 'P007'}
# ¿Son iguales?: False