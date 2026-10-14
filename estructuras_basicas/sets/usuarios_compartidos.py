
# Una plataforma tiene registros de usuarios de tres sistemas diferentes.

# Crea una función que determine:
# Los usuarios que utilizan los tres sistemas.
# Los usuarios que utilizan exactamente dos sistemas (Si un 
# usuario está en los tres sistemas, no debe aparecer en este grupo)
# Los usuarios que utilizan solamente uno de los sistemas.

# Cada usuario debe aparecer una sola vez en cada resultado.

def analizar_usuarios(sistema_a, sistema_b, sistema_c):

    utilizan_tres_sistemas = sistema_a & sistema_b & sistema_c

    utilizan_dos_sistemas = (
      ((sistema_a & sistema_c) - sistema_b)
    | ((sistema_a & sistema_b) - sistema_c)
    | ((sistema_b & sistema_c) - sistema_a))

    utilizan_un_sistema = (
      (sistema_a - sistema_b - sistema_c)
    | (sistema_b - sistema_a - sistema_c)
    | (sistema_c - sistema_a - sistema_b))

    return utilizan_tres_sistemas, utilizan_dos_sistemas, utilizan_un_sistema

sistema_a = {"Ana", "Carlos", "Diego", "Elena", "Felipe"}
sistema_b = {"Carlos", "Diego", "Felipe", "Gabriela", "Hugo"}
sistema_c = {"Diego", "Felipe", "Hugo", "Ignacio", "Julia"}

utilizan_tres_sistemas, utilizan_dos_sistemas, utilizan_un_sistema = analizar_usuarios(
    sistema_a, sistema_b, sistema_c
)

respuesta = f"""Utilizan los tres sistemas: {utilizan_tres_sistemas}
Utilizan exactamente dos sistemas: {utilizan_dos_sistemas}
Utilizan solamente un sistema: {utilizan_un_sistema}"""

print(respuesta)

# Resultado esperado:
# Tres sistemas: {'Diego', 'Felipe'}
# Dos sistemas: {'Carlos', 'Hugo'}
# Un sistema: {'Ana', 'Elena', 'Gabriela', 'Ignacio', 'Julia'}