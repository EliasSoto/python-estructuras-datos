
# Una empresa tiene dos grupos de trabajadores: los que 
# asistieron a una capacitación y los que estaban inscritos.

# Crea una función que reciba ambos conjuntos y determine:
# Quiénes estaban inscritos pero no asistieron.
# Quiénes asistieron pero no estaban inscritos.
# Quiénes estaban inscritos y sí asistieron.

def analizar_asistencia(inscritos, asistentes):
    inscritos = set(inscritos)
    asistentes = set(asistentes)

    # No asistieron
    no_asistieron = inscritos - asistentes

    # Asistentes no inscritos
    asistentes_no_inscritos = asistentes - inscritos

    # Inscritos y asisten
    inscritos_asistentes = asistentes & inscritos

    return no_asistieron, asistentes_no_inscritos, inscritos_asistentes

inscritos = ["Ana", "Carlos", "Diego", "Elena", "Felipe", "Gabriela"]
asistentes = ["Carlos", "Diego", "Felipe", "Hugo", "Ignacio"]

no_asistieron, asistentes_no_inscritos, inscritos_asistentes = analizar_asistencia(
    inscritos, asistentes
)

respuesta = f"""Los que no asistieron son: {no_asistieron}
Asistieron sin inscripción: {asistentes_no_inscritos}
Asistieron: {inscritos_asistentes}"""

print(respuesta)

# No asistieron: {'Ana', 'Elena', 'Gabriela'}
# Asistieron sin inscripción: {'Hugo', 'Ignacio'}
# Asistieron: {'Carlos', 'Diego', 'Felipe'}
