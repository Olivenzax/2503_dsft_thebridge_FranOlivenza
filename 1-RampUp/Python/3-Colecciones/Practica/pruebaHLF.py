import os
import time
import pprint

tablero = [[" " for _ in range(10)] for _ in range(10)]

class Barco:
    def __init__(self, nombre:str, num_casillas:int):
        self.nombre = nombre
        self.num_casillas = num_casillas
        

fragata = Barco("Fragata", 1)
destructor = Barco("Destructor", 2)
acorazado = Barco("Acorazado", 3)
portaaviones = Barco("Portaaviones", 4)

x = 1
y = 3

#horizontal
if y + portaaviones.num_casillas <= len(tablero[0]):
    for j in range(portaaviones.num_casillas):
        if tablero[x][y+j] == "B":
            print("Hay un barco en esta posición.")
            False
    for j in range(portaaviones.num_casillas):
        tablero[x][y + j] = "B"
    True
else:
    print("El barco no cabe en el tablero en esta posición.")
    False

time.sleep(1)
os.system("cls")

pprint.pprint(tablero)
time.sleep(2)


x = 1
y = 5


# vertical
if x + portaaviones.num_casillas <= len(tablero):
    for i in range(portaaviones.num_casillas):
        if tablero[x+i][y] == "B":
            print("Barco en esa posición. Escribe una nueva")
            False
    for i in range(portaaviones.num_casillas):
        tablero[x+i][y] = "B"
    True
else:
    print("El barco no cabe en el tablero en esta posición.")
    False

pprint.pprint(tablero)

time.sleep(1)
os.system("cls")

range(portaaviones.num_casillas)