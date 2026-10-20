
# Cada departamento tiene una lista de sueldos. Recorre las listas y guarda 
# en un diccionario el sueldo más alto de cada departamento, 
# sin ordenar las listas originales.

sueldos = {
    "Informatica": [950000, 1200000, 870000, 1500000],
    "Finanzas": [1100000, 980000, 1300000, 1050000],
    "Ventas": [800000, 900000, 900000, 750000]
}

dicc = {}

for depa, sueldo in sueldos.items():
    sueldo_mayor = 0
    for valor in sueldo:
        if valor > sueldo_mayor:
            sueldo_mayor = valor

    dicc[depa] = sueldo_mayor

print(dicc)