
# Analizador de ventas por producto
# Una tienda registra las ventas de distintos productos. 
# Cada venta contiene el código del producto, la cantidad vendida y el precio unitario.
# Crea una función que agrupe las ventas por código de producto y calcule para cada uno:
# - La cantidad total vendida.
# - El importe total vendido.
# - El número de operaciones de venta.
# El resultado debe ser un diccionario cuyos valores sean otros diccionarios. 
# Si un producto aparece en varias ventas, sus datos deben acumularse.

def analizar_ventas(ventas):

    productos_agrupados = {}

    for venta in ventas:
        producto = venta["producto"]
        cantidad = venta["cantidad"]
        precio = venta["precio"]

        if producto not in productos_agrupados:
            productos_agrupados[producto] = {
                "cantidad_total": cantidad,
                "importe_total": cantidad*precio,
                "ventas_hechas": 1
            }
        else:
            productos_agrupados[producto]["cantidad_total"] += cantidad
            productos_agrupados[producto]["importe_total"] += cantidad*precio
            productos_agrupados[producto]["ventas_hechas"] += 1
    
    return productos_agrupados


ventas = [
    {"producto": "P001", "cantidad": 2, "precio": 1000},
    {"producto": "P002", "cantidad": 1, "precio": 2500},
    {"producto": "P001", "cantidad": 3, "precio": 1000},
    {"producto": "P003", "cantidad": 4, "precio": 500},
    {"producto": "P002", "cantidad": 2, "precio": 2500},
    {"producto": "P001", "cantidad": 1, "precio": 1000}
]

resultado = analizar_ventas(ventas)

for codigo, datos in resultado.items():
    print(codigo, datos)

# Resultado esperado:
# P001 {'cantidad_total': 6, 'importe_total': 6000, 'operaciones': 3}
# P002 {'cantidad_total': 3, 'importe_total': 7500, 'operaciones': 2}
# P003 {'cantidad_total': 4, 'importe_total': 2000, 'operaciones': 1}
