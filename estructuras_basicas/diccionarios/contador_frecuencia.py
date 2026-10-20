
# Contador de frecuencias
# Crea una función que reciba una lista de palabras y devuelva un diccionario 
# donde cada palabra sea una clave y su valor indique cuántas veces aparece.
# Debes contar las apariciones sin distinguir entre mayúsculas y minúsculas.

def contar_palabras(palabras):
    diccionario = {}

    for palabra in palabras:
        palabra = palabra.lower()

        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1

    return diccionario


palabras = [
    "Python", "Java", "python", "C++",
    "Java", "PYTHON", "C++", "Python"
]

resultado = contar_palabras(palabras)

print(resultado)

# Resultado esperado:
# {'python': 4, 'java': 2, 'c++': 2}
