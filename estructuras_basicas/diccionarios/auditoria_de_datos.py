
# Una empresa mantiene un diccionario de empleados y otro de departamentos. 
# Cada empleado tiene un identificador y un registro con su nombre y el código 
# de su departamento.
# Crea una función que audite los registros y detecte:
# 1. Empleados cuyo departamento no existe.
# 2. Departamentos que no tienen empleados asignados.
# 3. Cantidad de empleados por departamento existente.
# 4. Si todos los empleados están correctamente asociados a un departamento válido.

def auditar_empleados(empleados, departamentos):

    return 


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



# Resultado esperado:
# Empleados con departamento inexistente: {104: 'Elena'}
# Departamentos sin empleados: {'MARKETING'}
# Cantidad por departamento: {'TI': 2, 'RRHH': 2, 'FINANZAS': 1, 'MARKETING': 0}
# ¿Datos consistentes?: False