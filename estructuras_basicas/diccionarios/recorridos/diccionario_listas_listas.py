
# Cada departamento contiene una lista de empleados. Guarda en un 
# diccionario el nombre del empleado con el promedio de notas más 
# alto de cada departamento.

empresa = {
    "TI": [
        {"nombre": "Ana", "notas": [6.0, 5.5, 6.5]},
        {"nombre": "Luis", "notas": [5.0, 6.0, 5.5]}
    ],
    "Ventas": [
        {"nombre": "Pedro", "notas": [4.0, 5.0, 6.0]},
        {"nombre": "Marta", "notas": [6.5, 6.0, 7.0]}
    ]
}

dicc = {}

for depa, alumnos in empresa.items():
    promedio = 0
    nombre_mejor_promedio = ""
    for alumno in alumnos:
        suma = 0
        for nota in alumno["notas"]:
            suma += nota
        promedio_actual = suma/len(alumno["notas"])

        if promedio < promedio_actual:
            promedio = promedio_actual
            nombre_mejor_promedio = alumno["nombre"]

    dicc[depa] = nombre_mejor_promedio

print(dicc)

