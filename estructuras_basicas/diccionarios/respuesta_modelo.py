
# Recorre la lista resultado y obtén tres variables: texto_completo, 
# que contenga todos los textos reconocidos unidos por espacios; 
# confianza_promedio, que calcule el promedio de todas las puntuaciones 
# de confianza; y cantidad_textos, que indique el total de textos reconocidos. 
# Finalmente, muestra las tres variables por pantalla.

resultado = [
    {
        "rec_texts": ["FACTURA", "N°1052", "COMERCIAL SUR"],
        "rec_scores": [0.98, 0.95, 0.91]
    },
    {
        "rec_texts": ["TOTAL", "$45990", "PAGADO"],
        "rec_scores": [0.96, 0.89, 0.97]
    },
    {
        "rec_texts": ["FECHA", "19/10/2026"],
        "rec_scores": [0.93, 0.99]
    }
]

texto_reconocido = ""
contador_textos = 0
suma = 0

for datos in resultado:
    for texto in datos["rec_texts"]:
        contador_textos += 1
        texto_reconocido += texto + " "
    suma += sum(datos["rec_scores"])

confianza_promedio = suma/contador_textos

print(f"Texto reconocido: {texto_reconocido}")
print(f"La confianza promedio es: {confianza_promedio}")
print(f"Cantidad de textos: {contador_textos}")