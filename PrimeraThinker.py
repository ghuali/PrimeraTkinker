import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os

root = tk.Tk()
root.resizable(False, False)
root.title("Adivina el Hiragana")


ejemplo_dir = '/home/alumno/PycharmProjects/PrimeraTkinter/hiragana'
contenido = os.listdir(ejemplo_dir)


imagenes = [img for img in contenido if img.endswith('.png')]


imagenesAnadidas = set()


puntos = 0

def cargar_imagen():
    global puntos
    resultadofinal = ""

    
    if len(imagenesAnadidas) == 10:
        messagebox.showinfo("Fin del juego", "Has adivinado todas las imágenes.")
        
        
        if puntos < 5:
            resultadofinal = "Suspendido"
        elif puntos == 5:
            resultadofinal = "Suficiente"
        elif puntos == 6:
            resultadofinal = "Bien"
        elif puntos == 7 or puntos == 8:
            resultadofinal = "Notable"
        elif puntos == 9 or puntos == 10:
            resultadofinal = "Sobresaliente"

        ttk.Label(root, text=f'Resultado final: {resultadofinal}', font=("Segoe UI", 14)).pack(pady=5)
        root.quit()
        return

    
    indice_random = random.choice([i for i in range(len(imagenes)) if i not in imagenesAnadidas])
    imagenesAnadidas.add(indice_random)

    
    ruta_imagen = os.path.join(ejemplo_dir, imagenes[indice_random])
    image = Image.open(ruta_imagen).resize((200, 200))  # Ajuste de tamaño si es necesario
    photo = ImageTk.PhotoImage(image)

    
    img_label.config(image=photo)
    img_label.image = photo

def validar_respuesta():
    global puntos

    
    respuesta = entrada.get().strip().lower()
    nombre_imagen = os.path.splitext(imagenes[list(imagenesAnadidas)[-1]])[0].lower()

    
    if respuesta == nombre_imagen:
        puntos += 1

    entrada.delete(0, tk.END)
    cargar_imagen()


img_label = ttk.Label(root)
img_label.pack(pady=10)

ttk.Label(root, text="Escribe el nombre del Hiragana:", font=("Segoe UI", 14)).pack(pady=5)
entrada = ttk.Entry(root, font=("Segoe UI", 14))
entrada.pack(pady=5)

ttk.Button(root, text="Validar", command=validar_respuesta).pack(pady=10)


cargar_imagen()

root.mainloop()
