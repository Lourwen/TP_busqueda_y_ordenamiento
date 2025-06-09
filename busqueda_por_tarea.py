#BUSQUEDA LINEAL 

arboles = [
    {"id": 1, "direccion": "Av. Callao 800", "tareas": ["poda", "extraccion"]},
    {"id": 2, "direccion": "Av. Corrientes 1200", "tareas": ["corte de raiz"]},
    {"id": 3, "direccion": "Av. Rivadavia 1500", "tareas": ["reparacion de vereda"]},
    {"id": 4, "direccion": "Av. Córdoba 900", "tareas": ["poda"]},
]
# Buscar todos los árboles que tengan una tarea específica

tarea_objetivo ="poda" #si la tarea buscada fuera poda


def busqueda_lineal_por_tarea(arboles, tarea_objetivo):
    resultado = []
    for arbol in arboles:
        if tarea_objetivo in arbol["tareas"]:
            resultado.append(arbol)
    return resultado

import time
# Medir tiempo
inicio_lineal = time.time()
resultado_lineal = busqueda_lineal_por_tarea(arboles, tarea_objetivo)
fin_lineal = time.time()
tiempo_lineal = fin_lineal - inicio_lineal

#BUSQUEDA BINARIA 

# Crear una lista auxiliar de (tarea, árbol)
tareas_lista = []
for arbol in arboles:
    for tarea in arbol["tareas"]:
        tareas_lista.append({"tarea": tarea, "arbol": arbol})

# Ordenar por tarea
def obtener_tarea(item):
    return item["tarea"]

tareas_ordenadas = sorted(tareas_lista, key=obtener_tarea)
def busqueda_binaria_por_tarea(lista, tarea_objetivo):
    resultados = []
    izquierda, derecha = 0, len(lista) - 1

    # Encontrar una ocurrencia con búsqueda binaria clásica
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        tarea_actual = lista[medio]["tarea"]
        if tarea_actual == tarea_objetivo:
            # Buscar hacia ambos lados para encontrar todos los árboles con esa tarea
            i = medio
            while i >= 0 and lista[i]["tarea"] == tarea_objetivo:
                resultados.append(lista[i]["arbol"])
                i -= 1
            i = medio + 1
            while i < len(lista) and lista[i]["tarea"] == tarea_objetivo:
                resultados.append(lista[i]["arbol"])
                i += 1
            break
        elif tarea_actual < tarea_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return resultados
import time

tarea_objetivo = "poda"

inicio_binaria = time.time()
resultados_binarios = busqueda_binaria_por_tarea(tareas_ordenadas, tarea_objetivo)
fin_binaria = time.time()

tiempo_binaria = fin_binaria - inicio_binaria





# BUSQUEDA INDICE HASH
import time


# Construir el índice hash por tarea
indice_tareas = {}
for arbol in arboles:
    for tarea in arbol["tareas"]:
        if tarea not in indice_tareas:
            indice_tareas[tarea] = []
        indice_tareas[tarea].append(arbol)

# Tarea que se quiere buscar
tarea_objetivo = "poda"

# Medir tiempo de búsqueda por tarea en tabla hash
inicio_hash = time.time()
resultado_hash = indice_tareas.get(tarea_objetivo, [])
fin_hash = time.time()
tiempo_hash = fin_hash - inicio_hash

# Mostrar resultados lineal

print(f"Búsqueda Lineal por tarea: {len(resultado_lineal)} árboles encontrados. Tiempo = {tiempo_lineal:.6f} segundos")
for arbol in resultado_lineal:
    print(arbol)
# Mostrar resultados busqueda binaria
print(f"Búsqueda Binaria por Tarea:{len(resultados_binarios)} árboles encontrados. Tiempo = {tiempo_binaria:.6f} segundos.")
for arbol in resultados_binarios:
    print(arbol)

# Mostrar resultados hash
print(f"Búsqueda Hash por tarea '{tarea_objetivo}':{len(resultado_hash)} árboles encontrados .Tiempo = {tiempo_hash:.6f} segundos.")
for arbol in resultado_hash:
    print(arbol)





