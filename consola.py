from editor import Editor
from interprete import procesar_instrucciones
from auxiliares import formatear_matriz

def iniciar_consola() -> None:
    mensaje_salida = ""
    editor = Editor()
    while True:
        matriz = editor.salida(mensaje_inferior=mensaje_salida)
        texto = formatear_matriz(matriz)
        if not editor.procesar:
            break
        try:
            resultado = procesar_instrucciones(texto)
            if resultado != None:
                mensaje_salida = resultado
            else:
                mensaje_salida = ""
        except Exception as error:
            mensaje_salida = f"[ERROR : {error}]"
       