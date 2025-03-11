#ejer1
def convertir_num(dia_text):
    for d in range(len(dia_text)):
        if dia_num == d+1:
            print(d+1,dia_text[d])

#ejer2
def piramide_invertida(c):
    for n in range(c, 0, -1):
        for v in range(n, 0, -1):
            print(v, end=" ")
        print()

#ejer3
def comparar_num(i,j):
    i = x
    j = y
    if i > j:
        print("El primero es mayor que el segundo.")
    elif i < j:
        print("El segundo es mayor que el primero.")
    else:
        print("Los dos números son iguales.")

#ejer4
def buscar_letra(texto_buscar):
    print(f"\nEl texto sobre el que quieres actuar es:\n {texto_buscar}")
    print(f"\nEl número de veces que aparece la letra {letra_txt} en el texto de arriba es {texto_buscar.count(letra_txt)}")
    return

#ejer5
def contar_letras(texto):
    # Diccionario para almacenar el conteo de cada carácter
    conteo = {}
    for letra in texto:
        # Si la letra ya está en el diccionario, incrementamos su conteo +1
        if letra in conteo:
            conteo[letra] += 1
        # Si no está, añadimos un conteo de 1
        else:
            conteo[letra] = 1
    return conteo

#ejer6
def modificar_lista(lista, comando, elemento=None):
    if comando == "añadir":
        elemento = input("¿Qué elemento quieres añadir?")
        if elemento is not None:
            lista.append(elemento)
        else:
            print("Error: Para 'añadir', debes proporcionar un elemento.")
    elif comando == "quitar":
        elemento = input("¿Qué elemento quieres eliminar?")
        if elemento is not None:
            if elemento in lista:
                lista.remove(elemento) 
            else:
                print(f"Error: El elemento '{elemento}' no está en la lista.")
        else:
            print("Error: Para 'quitar', debes proporcionar un algo.")
    else:
        print("Error: Comando no válido. Usa 'añadir' o 'quitar'.")
    return lista

#ejer7
def generar_frase(*palabras): # argumentos variables
    return ' '.join(palabras)

#ejer8

def fib_numbers(n):
    if n < 2:
        return n
    else:
        u = ((1+math.sqrt(5))/2)
        j = ((u**n-(1-u)**n)/math.sqrt(5))
        return round(j)

#ejer9
def area_cuadrado(lado):
    return lado ** 2

def area_triangulo(base,altura):
    return (base*altura)/2

def area_circulo(radio):
    return math.pi*(radio**2)

