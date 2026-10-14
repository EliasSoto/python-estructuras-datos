
# Una universidad tiene tres conjuntos:
# - estudiantes: todos los estudiantes registrados.
# - aprobados: estudiantes que aprobaron una asignatura.
# - certificados: estudiantes que recibieron certificado.

# Crea una función que valide la información y detecte inconsistencias.
# Debe determinar:
# 1. Estudiantes aprobados que no están registrados.
# 2. Estudiantes certificados que no aprobaron.
# 3. Estudiantes registrados que aprobaron pero no recibieron certificado.
# 4. Estudiantes que cumplen correctamente todo el proceso: 
# registrados, aprobados y certificados.
# 5. Si los datos son completamente consistentes.

def validar_estudiantes(estudiantes, aprobados, certificados):

    aprobados_no_registrados = aprobados - estudiantes
    certificados_no_aprobados = certificados - aprobados
    aprobados_sin_certificado = aprobados - certificados
    proceso_completo = estudiantes & aprobados & certificados

    # Son inconsistentes porque hay aprobados no registrados o certificados 
    # entregados a estudiantes que no aprobaron, por lo tanto, ambos conjuntos 
    # deben estar vacíos para que los datos sean consistentes.
    datos_consistentes = not aprobados_no_registrados and not certificados_no_aprobados

    return (aprobados_no_registrados, certificados_no_aprobados, 
    aprobados_sin_certificado, proceso_completo, datos_consistentes)

estudiantes = {
    "Ana",
    "Carlos",
    "Diego",
    "Elena",
    "Felipe",
    "Gabriela"
}

aprobados = {
    "Carlos",
    "Diego",
    "Felipe",
    "Hugo"
}

certificados = {
    "Diego",
    "Felipe",
    "Hugo",
    "Ignacio"
}

aprobados_no_registrados, certificados_no_aprobados, aprobados_sin_certificado, proceso_completo, datos_consistentes  = (
    validar_estudiantes(estudiantes, aprobados, certificados))

respuesta = f"""
Aprobados no registrados: {aprobados_no_registrados}
Certificados sin aprobar: {certificados_no_aprobados}
Aprobados sin certificado: {aprobados_sin_certificado}
Proceso completo: {proceso_completo}
¿Datos consistentes?: {datos_consistentes}
"""

print(respuesta)

# Resultado esperado:
# Aprobados no registrados: {'Hugo'}
# Certificados sin aprobar: {'Ignacio'}
# Aprobados sin certificado: {'Carlos'}
# Proceso completo: {'Diego', 'Felipe'}
# ¿Datos consistentes?: False