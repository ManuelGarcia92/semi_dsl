def comprobar_matriz_vacia(matriz):
    if not matriz:
        return True
    return all(str(celda).strip() == "" for fila in matriz for celda in fila)

def formatear_matriz(matriz):
    matriz_formateada = ""
    if comprobar_matriz_vacia(matriz):
        return matriz_formateada
    for linea in matriz:
        matriz_formateada += "".join(linea)
        matriz_formateada += "|"
    return matriz_formateada[:-1]