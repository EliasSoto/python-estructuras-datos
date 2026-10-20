# 🐍 Python Diccionarios

> **Repositorio de estudio y práctica de diccionarios en Python.**

> [!NOTE]
> El objetivo es comprender la lógica de los diccionarios, cómo almacenan información mediante pares clave-valor y cómo permiten consultar, modificar y administrar datos en Python mediante la práctica.

## ¿Qué son los diccionarios?

Los diccionarios (`dict`) son estructuras de datos que almacenan información mediante pares de **clave-valor**. Cada clave permite acceder al valor asociado.

```python
estudiante = {
    "nombre": "Elías",
    "edad": 22,
    "carrera": "Informática"
}

print(estudiante["nombre"])  # Elías
```

### Características

- Almacenan información mediante pares clave-valor.
- Las claves deben ser únicas.
- Son mutables: permiten agregar, modificar y eliminar elementos.
- Mantienen el orden de inserción.
- Permiten acceder a los valores mediante sus claves.
- Las claves deben ser de tipos inmutables, como cadenas, números o tuplas cuyos elementos también sean inmutables.

## ¿Para qué se utilizan?

Los diccionarios permiten representar información relacionada y acceder a ella mediante identificadores.

- Representar entidades, como estudiantes, productos o vehículos.
- Almacenar configuraciones y parámetros.
- Contabilizar frecuencias de elementos.
- Agrupar y organizar información relacionada.
- Consultar datos mediante identificadores, como códigos o nombres.

## Operadores

| Operador | Operación | Ejemplo/Resultado |
|---|---|---|
| `[]` | Acceder a un valor mediante su clave | `datos["nombre"]` → `"Elías"` |
| `in` | Comprobar si una clave existe | `"edad" in datos` → `True` |
| `not in` | Comprobar si una clave no existe | `"nota" not in datos` → `True` |
| `del` | Eliminar un elemento mediante su clave | `del datos["edad"]` |
| `len()` | Obtener la cantidad de pares clave-valor | `len(datos)` → `2` |

## Métodos principales

| Método | Función |
|---|---|
| `get(clave)` | Obtiene el valor de una clave sin generar un error si no existe. |
| `keys()` | Devuelve una vista de las claves. |
| `values()` | Devuelve una vista de los valores. |
| `items()` | Devuelve una vista de los pares clave-valor. |
| `update()` | Agrega o actualiza pares clave-valor. |
| `pop(clave)` | Elimina una clave y devuelve su valor. |
| `setdefault()` | Obtiene el valor de una clave o la crea si no existe. |
| `clear()` | Elimina todos los elementos del diccionario. |

## Ejemplo

```python
inventario = {
    "teclado": 10,
    "mouse": 15
}

# Consultar un valor
print(inventario["teclado"])  # 10

# Agregar un producto
inventario["monitor"] = 5

# Modificar un valor
inventario["mouse"] = 12

# Comprobar si existe una clave
print("monitor" in inventario)  # True

print(inventario)
```

> **Idea principal:** Un diccionario relaciona claves con valores, permitiendo organizar, consultar y modificar información mediante identificadores en lugar de depender de posiciones numéricas.

### Reglas importantes

1. Cada clave debe ser única; si se repite, prevalece el último valor asignado.
2. Acceder mediante `diccionario[clave]` genera un `KeyError` si la clave no existe.
3. Utilizar `get()` permite consultar una clave sin generar ese error.
4. Asignar un valor a una clave existente modifica su valor; asignarlo a una nueva clave agrega un elemento.
5. `in` comprueba la existencia de claves, no de valores. Para comprobar valores, se utiliza `values()`.
6. Los métodos `keys()`, `values()` e `items()` devuelven vistas, no listas independientes.


1. Diccionarios anidados
Un diccionario dentro de otro. Por ejemplo, estudiantes agrupados por curso, con sus notas y asistencia.

2. Listas de diccionarios
Una lista donde cada elemento es un diccionario. Es común en respuestas de API y resultados de modelos de IA.


3. Diccionarios con listas
Un diccionario cuyas claves guardan listas de valores relacionados, como textos reconocidos y sus puntuaciones.