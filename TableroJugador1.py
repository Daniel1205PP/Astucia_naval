import tkinter as tk
import random

# Constantes
COLUMNAS = 10
FILAS = 10
MAR = " "
SUBMARINO = "S"
DESTRUCTOR = "D"
DESTRUCTOR_VERTICAL = "A"

def obtener_matriz_inicial():
    return [[MAR for _ in range(COLUMNAS)] for _ in range(FILAS)]

def colocar_e_imprimir_barcos(matriz, cantidad_barcos):
    barcos_una_celda = cantidad_barcos // 2
    barcos_dos_celdas_verticales = cantidad_barcos // 4
    barcos_dos_celdas_horizontales = cantidad_barcos // 4

    # Colocar barcos de una celda
    for _ in range(barcos_una_celda):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if matriz[y][x] == MAR:
                matriz[y][x] = SUBMARINO
                break

    # Colocar barcos de dos celdas horizontales
    for _ in range(barcos_dos_celdas_horizontales):
        while True:
            x = random.randint(0, 8)
            y = random.randint(0, 9)
            if matriz[y][x] == MAR and matriz[y][x + 1] == MAR:
                matriz[y][x] = DESTRUCTOR
                matriz[y][x + 1] = DESTRUCTOR
                break

    # Colocar barcos de dos celdas verticales
    for _ in range(barcos_dos_celdas_verticales):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 8)
            if matriz[y][x] == MAR and matriz[y + 1][x] == MAR:
                matriz[y][x] = DESTRUCTOR_VERTICAL
                matriz[y + 1][x] = DESTRUCTOR_VERTICAL
                break

    return matriz

def dibujar_tablero(canvas, matriz_juego, mostrar_barcos, offset_x=0):
    for i in range(len(matriz_juego)):
        for j in range(len(matriz_juego[i])):
            x1, y1 = j * 60 + offset_x, i * 60
            x2, y2 = x1 + 60, y1 + 60
            color = "gray" if mostrar_barcos and matriz_juego[i][j] != MAR else "lightblue"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)