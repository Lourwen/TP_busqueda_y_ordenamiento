# BUSQUEDA LINEAL
def buscar_por_direccion_lineal(arboles, direccion_objetivo):
    for i in range(len(arboles)):
        if arboles[i]['direccion'] == direccion_objetivo:
            return i
    return -1

import time
import random

# Generar una lista de diccionarios simulando árboles
tamaño_lista = 1000000   # valores mayores 1.000.000 generan error
arboles = [{'direccion': f'Calle {i}'} for i in range(tamaño_lista)]

# Elegir una dirección objetivo aleatoria
direccion_objetivo = f'Calle {random.randint(0, tamaño_lista - 1)}'

# Funcion de búsqueda por dirección lineal
def buscar_por_direccion_lineal(arboles, direccion_objetivo):
    for i in range(len(arboles)):
        if arboles[i]['direccion'] == direccion_objetivo:
            return i
    return -1

# Medicion tiempo de búsqueda lineal
inicio = time.time()
resultado_lineal = buscar_por_direccion_lineal(arboles, direccion_objetivo)
fin = time.time()
tiempo = fin - inicio

#-----------------------------------------------------

# Lista de árboles

# arboles = [
#    {"id": 1, "direccion": "Av. Callao 800", "tareas": ["poda", "extraccion"]},
#    {"id": 2, "direccion": "Av. Corrientes 1200", "tareas": ["corte de raiz"]},
#    {"id": 3, "direccion": "Av. Rivadavia 1500", "tareas": ["reparacion de vereda"]},
#    {"id": 4, "direccion": "Av. Córdoba 900", "tareas": ["poda"]},
#]

#BUSQUEDA BINARIA
# Función para obtener la dirección del árbol
def obtener_direccion(arbol):
    return arbol["direccion"]

# Ordenar la lista de árboles por dirección (requisito para búsqueda binaria)
arboles_ordenados = sorted(arboles, key=obtener_direccion)

# Función de búsqueda binaria adaptada para buscar por dirección
def busqueda_binaria_por_direccion(arboles_ordenados, direccion_objetivo):
    izquierda, derecha = 0, len(arboles_ordenados) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        direccion_actual = arboles_ordenados[medio]["direccion"]
        if direccion_actual == direccion_objetivo:
            return medio
        elif direccion_actual < direccion_objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

##direccion_objetivo = "Av. Córdoba 900"
import time
# Medir el tiempo de ejecución de la búsqueda binaria
inicio_binaria = time.time()
resultado_binaria = busqueda_binaria_por_direccion(arboles_ordenados, direccion_objetivo)
fin_binaria = time.time()
tiempo_binaria = fin_binaria - inicio_binaria

# BUSQUEDA POR INDICE HASH

indice_direccion = {arbol["direccion"]: arbol for arbol in arboles}
arbol = indice_direccion.get(direccion_objetivo)

import time

# Creacion de  índice hash por dirección
inicio_hash = time.time()
indice_direccion = {arbol["direccion"]: arbol for arbol in arboles}
arbol = indice_direccion.get(direccion_objetivo)
fin_hash = time.time()
tiempo_hash = fin_hash - inicio_hash

#RESULTADOS

# Mostrar resultado lineal
print(f"Búsqueda Lineal: Resultado = {resultado_lineal}, Tiempo = {tiempo:.6f} segundos")

# Mostrar resultados busqeuda binaria
print(f"Búsqueda Binaria: Resultado = {resultado_binaria}, Tiempo = {tiempo_binaria:.6f} segundos")


# Mostrar resultados hash
if arbol:
    print(f"Búsqueda Hash: Árbol encontrado = {arbol}, Tiempo = {tiempo_hash:.6f} segundos")
else:
    print(f"Búsqueda Hash: Dirección no encontrada. Tiempo = {tiempo_hash:.6f} segundos")

# ANEXO : INDIDE HUSH SIN MEDICION DE TIEMPO EN CONSTRUCCION DEL INDICE
# Construir índice (solo una vez)
indice_direccion = {arbol["direccion"]: arbol for arbol in arboles}

# Medir solo la búsqueda
inicio_hash = time.time()
arbol = indice_direccion.get(direccion_objetivo)
fin_hash = time.time()

tiempo_hash2 = fin_hash - inicio_hash

# Mostrar resultados hash2
if arbol:
    print(f"Búsqueda Hash2: Árbol encontrado = {arbol}, Tiempo = {tiempo_hash2:.6f} segundos")
else:
    print(f"Búsqueda Hash2: Dirección no encontrada. Tiempo = {tiempo_hash2:.6f} segundos")
