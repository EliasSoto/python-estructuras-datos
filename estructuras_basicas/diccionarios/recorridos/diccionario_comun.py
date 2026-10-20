
# Dado el siguiente diccionario, recorre los departamentos y calcula el nombre 
# del empleado con el sueldo más alto de cada departamento.

empresa = {
    "Informatica": {
        "Ana": 950000,
        "Luis": 1200000,
        "Pedro": 870000
    },
    "Finanzas": {
        "Marta": 1100000,
        "Carlos": 980000,
        "Sofia": 1300000
    }
}

dicc = {}

for depa, datos in empresa.items():
    #Reiniciamos valores luego de cada departamento
    sueldo_mayor = 0
    nombre_sueldo_mayor = ""
    for nombre, sueldos in datos.items():
        if sueldo_mayor < sueldos:
            sueldo_mayor = sueldos
            nombre_sueldo_mayor = nombre

    #Guardamos en el diccionario
    dicc[depa] = nombre_sueldo_mayor

print(dicc)