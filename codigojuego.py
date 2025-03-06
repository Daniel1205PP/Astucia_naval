import tkinter as tk
import random
from tkinter import messagebox, simpledialog, Toplevel
import pygame
import os
import TableroJugador1
import TableroJugador2
from PIL import Image, ImageTk

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Directorios de recursos
sound_dir = os.path.join(os.path.dirname(__file__), 'sonidos')  # Carpeta para sonidos
image_dir = os.path.join(os.path.dirname(__file__), 'imagenes')  # Carpeta para imágenes

# Cargar sonidos
sound_disparo = pygame.mixer.Sound(os.path.join(sound_dir, "disparo.wav"))
sound_fallido = pygame.mixer.Sound(os.path.join(sound_dir, "fallido.wav"))
sound_acertado = pygame.mixer.Sound(os.path.join(sound_dir, "acertado.wav"))

# Constantes
COLOR_FONDO = "lightblue"
CANTIDAD_BARCOS_INICIALES = 5
JUGADOR_1 = "Jugador 1"
JUGADOR_2 = "Jugador 2"
DISPARO_FALLADO = "-"
DISPARO_ACERTADO = "*"

# Configuración de la ventana
root = tk.Tk()
root.withdraw()

def mostrar_imagen(imagenes, mensaje):
    ruta = os.path.join(image_dir, imagenes)  # Usa el directorio correcto
    if not os.path.exists(ruta):
        print(f"⚠️ Error: La imagen '{imagenes}' no se encuentra en '{image_dir}'")
        return

    ventana = Toplevel(root)
    ventana.title("Mensaje")
    
    img = Image.open(ruta)
    img = img.resize((600, 500), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(img)
    
    label_img = tk.Label(ventana, image=img_tk)
    label_img.image = img_tk
    label_img.pack()
    
    label_texto = tk.Label(ventana, text=mensaje, font=("Arial", 12), wraplength=380)
    label_texto.pack()
    
    btn_cerrar = tk.Button(ventana, text="Cerrar", command=ventana.destroy)
    btn_cerrar.pack()
    
    ventana.grab_set()  # Evita que se abran múltiples ventanas

# Mostrar imagen inicial
mostrar_imagen("img1.jpg", "El ataque a Pearl Harbor fue un ataque sorpresa de la Armada Imperial de Japón contra la base naval de Estados Unidos en Hawái, el 7 de diciembre de 1941.")
root.deiconify()

root.title("Batalla Naval Pearl Harbor")
canvas = tk.Canvas(root, width=600, height=600, bg=COLOR_FONDO)
canvas.pack()

def manejar_turno(turno_actual, matriz_j1, matriz_j2, x, y):
    if turno_actual == JUGADOR_1:
        if matriz_j2[y][x] != TableroJugador2.MAR:
            matriz_j2[y][x] = DISPARO_ACERTADO
            sound_acertado.play()
            mostrar_imagen("img2.jpg", "Mayo de 1942: Batalla del Mar del Coral.Fue una de las batallas clave del Teatro Asiático en la Segunda Guerra Mundial y significó el primer fracaso de una ofensiva nipona")
        else:
            matriz_j2[y][x] = DISPARO_FALLADO
            sound_fallido.play()
        return JUGADOR_2
    else:
        if matriz_j1[y][x] != TableroJugador1.MAR:
            matriz_j1[y][x] = DISPARO_ACERTADO
            sound_acertado.play()
            mostrar_imagen("img3.jpg", "4 al 7 de junio de 1942: Batalla de Midway. La Armada de los Estados Unidos, bajo el comando de Chester Nimitz, aprovechó la información de inteligencia con que contaba, para emboscar a los japoneses y causar daños devastadores a su marina de guerra. La derrota japonesa detuvo la expansión del Imperio Japonés en la región del Asia-Pacífico")
        else:
            matriz_j1[y][x] = DISPARO_FALLADO
            sound_fallido.play()
        return JUGADOR_1

def dibujar_juego():
    canvas.delete("all")
    TableroJugador1.dibujar_tablero(canvas, matriz_j1, True, 0)
    TableroJugador2.dibujar_tablero(canvas, matriz_j2, False, 600)

def on_click(event):
    global turno_actual
    x, y = (event.x % 600) // 60, event.y // 60
    if event.x < 600 and turno_actual == JUGADOR_1:
        turno_actual = manejar_turno(turno_actual, matriz_j1, matriz_j2, x, y)
    elif event.x >= 600 and turno_actual == JUGADOR_2:
        turno_actual = manejar_turno(turno_actual, matriz_j1, matriz_j2, x, y)
    dibujar_juego()

def main():
    global matriz_j1, matriz_j2, turno_actual
    matriz_j1 = TableroJugador1.obtener_matriz_inicial()
    matriz_j2 = TableroJugador2.obtener_matriz_inicial()
    matriz_j1 = TableroJugador1.colocar_e_imprimir_barcos(matriz_j1, CANTIDAD_BARCOS_INICIALES)
    matriz_j2 = TableroJugador2.colocar_e_imprimir_barcos(matriz_j2, CANTIDAD_BARCOS_INICIALES)
    turno_actual = JUGADOR_1
    
    canvas.bind("<Button-1>", on_click)
    dibujar_juego()
    root.mainloop()
    
    mostrar_imagen("imgfin.jpg", "El juego ha terminado. Japón se rindió incondicionalmente el 15 de agosto de 1945, aunque la firma se produjo el 2 de septiembre de 1945.")
    messagebox.showinfo("Fin del juego", "El juego ha terminado.")

if __name__ == "__main__":
    main()


