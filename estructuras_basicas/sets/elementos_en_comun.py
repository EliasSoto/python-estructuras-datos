
# Elementos en común

def elementos_comunes(lista1, lista2):
    # Para resolver ocupamos la operación de
    # conjuntos intersección en python  es &
    return set(lista1) & set(lista2)

lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

resultado = elementos_comunes(lista1, lista2)

# 4,5,6
print(resultado)
