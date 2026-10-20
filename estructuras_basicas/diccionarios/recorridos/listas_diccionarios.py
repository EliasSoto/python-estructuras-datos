
# Recorre la lista de empleados y crea un diccionario que relacione cada departamento 
# con el nombre del empleado que tenga el sueldo más alto. Si dos empleados tienen 
# el mismo sueldo máximo, conserva el primero que aparezca.

empleados = [
    {"nombre": "Ana", "departamento": "TI", "sueldo": 1200000},
    {"nombre": "Luis", "departamento": "Ventas", "sueldo": 900000},
    {"nombre": "Pedro", "departamento": "TI", "sueldo": 1400000},
    {"nombre": "Marta", "departamento": "Ventas", "sueldo": 1100000},
    {"nombre": "Sofia", "departamento": "TI", "sueldo": 1400000}
]

dicc = {}
sueldos_maximos = {}

for empleado in empleados:
    depa = empleado["departamento"]
    nombre = empleado["nombre"]
    sueldo = empleado["sueldo"]

    if depa not in dicc:
        dicc[depa] = nombre
        sueldos_maximos[depa] = sueldo

    elif sueldo > sueldos_maximos[depa]:
        dicc[depa] = nombre
        sueldos_maximos[depa] = sueldo

print(dicc)
