import json
import difflib
import tkinter as tk

# Cargar el archivo JSON
with open('knowledge_base.json') as archivo:
    datos = json.load(archivo)

preguntas = datos["preguntas"]
respuestas = datos["respuestas"]
palabras_prohibidas = datos.get("palabras_prohibidas", [])  # Lista de palabras prohibidas

# Función para encontrar la pregunta más cercana
def encontrar_pregunta_cercana(mensaje):
    print("Palabras prohibidas:", palabras_prohibidas)  
    # Filtrar palabras prohibidas
    for palabra_prohibida in palabras_prohibidas:
        print("Verificando palabra prohibida:", palabra_prohibida) 
        if palabra_prohibida in mensaje.lower():
            return "Tu mensaje contiene palabras prohibidas. Por favor, reformula tu pregunta."

    # Verificar si el mensaje contiene operaciones matemáticas
    if any(char in mensaje for char in ['+', '-', '*', '/', '%']):
        try:
            resultado = eval(mensaje) 
            return f"El resultado es: {resultado}"
        except Exception as e:
            return "Hubo un error al calcular. Por favor, verifica la expresión matemática."

    coincidencias = difflib.get_close_matches(mensaje, preguntas)
    if coincidencias:
        return respuestas[preguntas.index(coincidencias[0])]
    else:
        return "Lo siento, no entiendo. ¿Puedes ser más claro?"

# Función para manejar la entrada del usuario
def obtener_respuesta():
    mensaje = entrada_usuario.get()
    respuesta = encontrar_pregunta_cercana(mensaje)
    texto_respuesta.config(text=respuesta)

# Función para cerrar la aplicación
def cerrar_aplicacion():
    ventana.destroy()

# Configuración de la GUI
ventana = tk.Tk()
ventana.title("Chatbot")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Tú:")
etiqueta.pack()

entrada_usuario = tk.Entry(ventana)
entrada_usuario.pack()

boton = tk.Button(ventana, text="Enviar", command=obtener_respuesta)
boton.pack()

texto_respuesta = tk.Label(ventana, text="")
texto_respuesta.pack()

# Botón para cerrar la aplicación
boton_cerrar = tk.Button(ventana, text="Cerrar", command=cerrar_aplicacion)
boton_cerrar.pack()

# Bucle de la GUI
ventana.mainloop()