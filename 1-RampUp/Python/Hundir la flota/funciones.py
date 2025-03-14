import random
import time
import os
import pprint
from clases import *

# Funciones:

def crear_tableros():
    tablero_oculto = [[" " for _ in range(10)] for _ in range(10)]
    tablero_visible = [[" " for _ in range(10)] for _ in range(10)]
    tablero_maquina = [[" " for _ in range(10)] for _ in range(10)]

def verificar_celdas_circundantes(tablero_maquina, x, y, h, l):
    # Verifica que las celdas que el barco ocupará y sus adyacentes estén libres.

    for i in range(x - 1, x + (l if h == "vertical" else 1) + 1):
        for j in range(y - 1, y + (y if h == "horizontal" else 1) + 1):
            if 0 <= i < len(tablero_maquina) and 0 <= j < len(tablero_maquina[0]):
                if tablero_maquina[i][j] == "B":
                    return False
    return True


def colocar_barco_aleatorio(tablero_oculto, x, y, orientacion, l):
    # Función para que la máquina coloque los barcos uno por uno, en orden de mayor a menor.

    barcos_colocar = [portaaviones.num_casillas, acorazado.num_casillas, acorazado.num_casillas, destructor.num_casillas, destructor.num_casillas, destructor.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas]
    for n in range(len(barcos_colocar)):
            l = barcos_colocar[n]
            while True:
                h = random.randint(0,1)
                x = random.randint(0,9)
                y = random.randint(0,9)

                if h == 1:
                #horizontal
                    if y + l <= len(tablero_oculto[0]):
                        colocacion_valida = True
                        for j in range(l):
                            if tablero_oculto[x][y+j] == "B":
                                colocacion_valida = False
                                #print("Hay un barco en esta posición.")
                                #break
                            if not verificar_celdas_circundantes(tablero_oculto, x, y, orientacion, l):
                                colocacion_valida = False
                        if colocacion_valida:
                            for j in range(l):
                                tablero_oculto[x][y+j] = "B"
                            break
                    else:
                        # print("El barco no cabe en el tablero_oculto en esta posición.")
                        False
                else:
                    # vertical
                    if x + l <= len(tablero_oculto):
                        colocacion_valida = True
                        for i in range(l):
                            if tablero_oculto[x+i][y] == "B":
                                colocacion_valida = False
                                #print("Barco en esa posición. Escribe una nueva")
                                #break
                            if not verificar_celdas_circundantes(tablero_oculto, x, y, orientacion, l):
                                colocacion_valida = False
                        if colocacion_valida:
                            for i in range(l):
                                tablero_oculto[x+i][y] = "B"
                            break
                    else:
                        # print("El barco no cabe en el tablero_oculto en esta posición.")
                        False
    return tablero_oculto


def colocar_barco_jugador(tablero_maquina, x, y, orientacion, l):
    # Función para colocar los barcos uno por uno, en orden de mayor a menor.

    barcos_colocar = [portaaviones.num_casillas, acorazado.num_casillas, acorazado.num_casillas, destructor.num_casillas, destructor.num_casillas, destructor.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas, fragata.num_casillas]
    for n in range(len(barcos_colocar)):
            l = barcos_colocar[n]
            while True:
                h = str(input("Introduce la dirección del barco (horizontal/vertical)"))
                while True:
                    x = int(input("Escoge la fila (Entre 0 y 9)"))
                    if x < 0 or x > 9:
                        print("Entre 0 y 10")
                    else:
                        break
                while True:
                    y = int(input("Escoge la fila (Entre 0 y 9)"))
                    if y < 0 or y > 9:
                        print("Entre 0 y 10")
                    else:
                        break
                print(f"Posición elegida: {x},{y}")
                if h == "horizontal":
                #horizontal
                    if y + l <= len(tablero_maquina[0]):
                        colocacion_valida = True
                        for j in range(l):
                            if tablero_maquina[x][y+j] == "B":
                                print("Hay un barco en esta posición.")
                                colocacion_valida = False
                                #break
                            if not verificar_celdas_circundantes(tablero_maquina, x, y, orientacion, l):
                                print(f"Barco cercano a posiciones cercanas. Escribe una nueva")
                                colocacion_valida = False
                        if colocacion_valida:
                            for j in range(l):
                                tablero_maquina[x][y+j] = "B"
                            pprint.pprint(tablero_maquina) 
                            break
                    else:
                        print("El barco no cabe en el tablero_maquina en esta posición.")
                        False
                elif h == "vertical":
                    # vertical
                    if x + l <= len(tablero_maquina):
                        colocacion_valida = True
                        for i in range(l):
                            if tablero_maquina[x+i][y] == "B":
                                print("Barco en esa posición. Escribe una nueva")
                                colocacion_valida = False
                                #break
                            if not verificar_celdas_circundantes(tablero_maquina, x, y, orientacion, l):
                                print(f"Barco cercano a posiciones cercanas. Escribe una nueva")
                                colocacion_valida = False
                        if colocacion_valida:
                            for i in range(l):
                                tablero_maquina[x+i][y] = "B"
                            pprint.pprint(tablero_maquina) 
                            break
                    else:
                        print("El barco no cabe en el tablero_maquina en esta posición.")
                        False
                else:
                    print("Orientación no válida, elige horizontal o vertical:")
    return tablero_maquina

def disparar_maquina(tablero_maquina):
    # Dispara de manera aleatoria, si acierta repite tirada
    tocado = True
    while tocado == True:
        i = random.randint(0,9)
        j = random.randint(0,9)
        print(f"Has disparado a la posición [{i},{j}] y el resultado es:")
        # Solicita coordenadas a la máquina
        if tablero_maquina[i][j] == "B":
            tablero_maquina[i][j] = "X" 
            print(f"Tocado en posición {i},{j}")
            tocado = True
        elif tablero_maquina[i][j] == " ":
            tablero_maquina[i][j] = "A" 
            print("Agua")
            tocado = False
        else:
            print("Ya has disparado en esta posición.")
            tocado = True
        print()
        # Imprimir la función de disparo para probar
        for fila in tablero_maquina:
            print("][".join(fila))
        print("\n")

def disparar(tablero_oculto, tablero_visible):
    # Dispara siguiendo las coordenadas pautadas
    i = int(input("Introduce la coordenada i (fila): "))
    j = int(input("Introduce la coordenada j (columna): "))
    print(f"Has disparado a la posición [{i},{j}] y el resultado es:")
    # Solicitar coordenadas al usuario
    if 0 <= i < 10 and 0 <= j < 10:
        if tablero_oculto[i][j] == "B":
            tablero_oculto[i][j] = "X" 
            tablero_visible[i][j] = "X" 
            print(f"Tocado en posición {i},{j}")
        elif tablero_oculto[i][j] == " ":
            tablero_oculto[i][j] = "A"
            tablero_visible[i][j] = "A"  
            print("Agua")
        else:
            print("Ya has disparado en esta posición.")
    else:
        print("Coordenadas fuera del rango del tablero.")
    print()
    # Imprimir la función de disparo para probar
    for fila in tablero_visible:
        print("\n")