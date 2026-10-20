
# Análisis de calificaciones
# Una institución almacena las calificaciones de sus estudiantes en un diccionario. 
# Crea una función que identifique a los estudiantes aprobados, los reprobados y 
# el promedio general. Una calificación igual o superior a 4.0 se considera aprobada. 
# La función debe devolver los nombres de ambos grupos y el promedio de todas las 
# calificaciones.

def analizar_calificaciones(calificaciones):
    aprobados = []
    reprobados = []
    suma = 0
    contador = 0

    for nombre, nota in calificaciones.items():
        suma += nota
        contador += 1

        if nota >= 4:
            aprobados.append(nombre)
        else:
            reprobados.append(nombre)

    promedio_general = suma/contador
    return aprobados, reprobados, round(promedio_general, 2)

calificaciones = {
    "Ana": 6.5,
    "Carlos": 3.8,
    "Diego": 5.2,
    "Elena": 3.9,
    "Felipe": 4.0,
    "Gabriela": 6.0
}

aprobados, reprobados, promedio = analizar_calificaciones(calificaciones)

print("Aprobados:", aprobados)
print("Reprobados:", reprobados)
print("Promedio:", round(promedio, 2))

# Resultado esperado:
# Aprobados: {'Ana', 'Diego', 'Felipe', 'Gabriela'}
# Reprobados: {'Carlos', 'Elena'}
# Promedio: 4.9