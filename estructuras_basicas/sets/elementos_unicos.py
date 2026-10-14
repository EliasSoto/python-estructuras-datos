
# Elementos únicos

def elementos_unicos(numeros):
    numeros = set(numeros)
    return numeros

numeros = [4, 2, 7, 4, 2, 9, 7, 1, 4]

resultado = elementos_unicos(numeros)

print(resultado)
print(len(resultado))
