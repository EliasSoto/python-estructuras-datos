
# Una empresa mantiene un diccionario de empleados y otro de departamentos. 
# Cada empleado tiene un identificador y un registro con su nombre y el código 
# de su departamento.
# Crea una función que audite los registros y detecte:
# 1. Empleados cuyo departamento no existe.
# 2. Departamentos que no tienen empleados asignados.
# 3. Cantidad de empleados por departamento existente.
# 4. Si todos los empleados están correctamente asociados a un departamento válido.

def auditar_empleados(empleados, departamentos):
    
    # Inicializamos en 0 la cantidad de empleados por cada departamento existente.
    # Comprensión de diccionarios
    cantidad_empleado_depa = {depto: 0 for depto in departamentos}
    depas_personas = set()
    empleado_depa_inexistente = {}
    depas_sin_empleados = set()
    datos_consistente = True

    for id, empleado in empleados.items():
        depto = empleado["departamento"]

        if depto not in departamentos:
            empleado_depa_inexistente[id] = empleado["nombre"]

        # Contar cuántos empleados están asociados a cada departamento
        if depto in cantidad_empleado_depa:
            cantidad_empleado_depa[depto] += 1

        # Guarda los depas asociados a personas para comparar despues
        depas_personas.add(depto)

    # Buscar deptos y compoarar con los de los empleados
    for nombre_depto in departamentos:
        if nombre_depto not in depas_personas:
            depas_sin_empleados.add(nombre_depto)

    if empleado_depa_inexistente:
        datos_consistente = False

    return (empleado_depa_inexistente, depas_sin_empleados, 
    cantidad_empleado_depa, datos_consistente)


empleados = {
    101: {"nombre": "Ana", "departamento": "TI"},
    102: {"nombre": "Carlos", "departamento": "RRHH"},
    103: {"nombre": "Diego", "departamento": "TI"},
    104: {"nombre": "Elena", "departamento": "VENTAS"},
    105: {"nombre": "Felipe", "departamento": "FINANZAS"},
    106: {"nombre": "Gabriela", "departamento": "RRHH"}
}

departamentos = {
    "TI": "Tecnología",
    "RRHH": "Recursos Humanos",
    "FINANZAS": "Finanzas",
    "MARKETING": "Marketing"
}

(empleado_depa_inexistente, depas_sin_empleados, 
cantidad_empleado_depa, datos_consistente) = auditar_empleados(empleados, departamentos)

respuesta = f"""
Empleados con departamento inexistente: {empleado_depa_inexistente}
Departamentos sin empleados: {depas_sin_empleados}
Cantidad de empleados por departamento: {cantidad_empleado_depa}
¿Los datos son consistentes? {"Sí" if datos_consistente else "No"}
"""

print(respuesta)

# Resultado esperado:
# Empleados con departamento inexistente: {104: 'Elena'}
# Departamentos sin empleados: {'MARKETING'}
# Cantidad por departamento: {'TI': 2, 'RRHH': 2, 'FINANZAS': 1, 'MARKETING': 0}
# ¿Datos consistentes?: False