# 🐍 Python Sets

> **Repositorio de estudio y práctica de conjuntos (`set`) en Python.**

> [!NOTE]
> El objetivo es comprender la lógica de los `set`, sus características y su funcionamiento en Python mediante la práctica.

## ¿Qué es un Set?

Un `set` es una estructura de datos que almacena **elementos únicos y sin un orden definido**.

```python
numeros = {1, 2, 3, 4}
```

### Características

* No permite elementos duplicados.
* No mantiene un orden definido.
* Es mutable.
* No utiliza índices.
* Permite comprobar pertenencia de elementos.

## ¿Para qué se utilizan?

Los `set` son útiles principalmente para:

* Eliminar elementos duplicados.
* Comprobar si un elemento pertenece a un conjunto.
* Comparar conjuntos.
* Encontrar elementos comunes o diferentes.

## Operadores

Dados los siguientes conjuntos:

```python
A = {1, 2, 3}
B = {3, 4, 5}
```

| Operador | Operación            | Resultado         |
| -------- | -------------------- | ----------------- |
| `\|`     | Unión                | `{1, 2, 3, 4, 5}` |
| `&`      | Intersección         | `{3}`             |
| `-`      | Diferencia           | `{1, 2}`          |
| `^`      | Diferencia simétrica | `{1, 2, 4, 5}`    |
| `in`     | Pertenencia          | `True`            |
| `not in` | No pertenencia       | `False`           |

## Métodos principales

| Método         | Función                                   |
| -------------- | ----------------------------------------- |
| `add()`        | Agrega un elemento                        |
| `remove()`     | Elimina un elemento                       |
| `discard()`    | Elimina un elemento si existe             |
| `pop()`        | Elimina un elemento arbitrario            |
| `clear()`      | Vacía el conjunto                         |
| `len()`        | Obtiene la cantidad de elementos          |
| `issubset()`   | Comprueba si es subconjunto               |
| `issuperset()` | Comprueba si es superconjunto             |
| `isdisjoint()` | Comprueba si no tienen elementos en común |

## Ejemplo

```python
A = {1, 2, 3}
B = {3, 4, 5}

print(A & B)
print(A | B)
print(2 in A)
```

> **Idea principal:** Los `set` se utilizan cuando importa la **unicidad de los elementos y las relaciones entre conjuntos**, pero no su posición.
