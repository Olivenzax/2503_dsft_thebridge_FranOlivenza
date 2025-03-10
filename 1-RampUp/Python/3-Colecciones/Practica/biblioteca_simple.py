# Menu
## Seis casos y salir
'''
* En caso de que pida el usuario elija visualizar se visualizarán todos los libros
* Buscar libro: búsqueda por título que introduce el usuario y se visualiza todos los campos del libro
* Añadir libro: se debe solicitar al usuario que introduzca título y autor para el nuevo libro y se añade el libro a la lista de libros
* Eliminar libro: se solicita al usuario el título del libro y éste debe ser eliminado de la lista de libros
* Alquilar libro: se solicita al usuario el título del libro y se debe pasar el campo "Alquilado" a True
* Devolver libro: se solicita al usuario el título del libro y se debe pasar el campo "Alquilado" a False
'''
# Cada caso tiene que tener una función, que corresponde a una entrada en el menú

# Instalar la variable time
import time
# Instalar la variable tabulate, para crear tablas
from tabulate import tabulate
# Instalar OS para que limpie la pantalla cuando haya una nueva consulta
import os


libros = [
    {"Titulo": "Python Data Science Handbook", "Autor": "Jake VanderPlas", "Alquilado": False},
    {"Titulo": "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow", "Autor": "Aurélien Géron", "Alquilado": True},
    {"Titulo": "Pattern Recognition and Machine Learning", "Autor": "Christopher M. Bishop", "Alquilado": False},
    {"Titulo": "Deep Learning", "Autor": "Ian Goodfellow, Yoshua Bengio, Aaron Courville", "Alquilado": True},
    {"Titulo": "The Elements of Statistical Learning", "Autor": "Trevor Hastie, Robert Tibshirani, Jerome Friedman", "Alquilado": False},
    {"Titulo": "Data Science for Business", "Autor": "Foster Provost, Tom Fawcett", "Alquilado": False},
    {"Titulo": "Bayesian Data Analysis", "Autor": "Andrew Gelman et al.", "Alquilado": True},
    {"Titulo": "Introduction to the Theory of Computation", "Autor": "Michael Sipser", "Alquilado": False},
    {"Titulo": "Artificial Intelligence: A Modern Approach", "Autor": "Stuart Russell, Peter Norvig", "Alquilado": True},
    {"Titulo": "Computer Vision: Algorithms and Applications", "Autor": "Richard Szeliski", "Alquilado": False},
    {"Titulo": "Data Science from Scratch", "Autor": "Joel Grus", "Alquilado": True},
    {"Titulo": "The Art of Statistics", "Autor": "David Spiegelhalter", "Alquilado": False},
    {"Titulo": "Python Machine Learning", "Autor": "Sebastian Raschka, Vahid Mirjalili", "Alquilado": True},
    {"Titulo": "An Introduction to Statistical Learning", "Autor": "Gareth James, Daniela Witten, Trevor Hastie, Robert Tibshirani", "Alquilado": False},
    {"Titulo": "Fundamentals of Data Engineering", "Autor": "Joe Reis, Matt Housley", "Alquilado": False},
    {"Titulo": "Storytelling with Data", "Autor": "Cole Nussbaumer Knaflic", "Alquilado": True},
    {"Titulo": "Building Machine Learning Powered Applications", "Autor": "Emmanuel Ameisen", "Alquilado": False},
    {"Titulo": "Practical Statistics for Data Scientists", "Autor": "Peter Bruce, Andrew Bruce", "Alquilado": True},
    {"Titulo": "SQL for Data Scientists", "Autor": "Renee M. P. Teate", "Alquilado": False},
    {"Titulo": "Data Engineering on Azure", "Autor": "Vlad Riscutia", "Alquilado": True}
]

# operaciones_bib = ["Visualizar", "Buscar", "Añadir", "Eliminar", "Alquilar", "Devolver", "Salir"]
def visualizar_libros(libros):
    print("\nHas elegido visualizar, aquí se muestran todos los libros, sus autores y su disponibilidad:\n")
    time.sleep(1)
    libros_mostrar = libros.copy()
    for libro in libros_mostrar:
        libro["Alquilado"] = "Sí" if libro["Alquilado"] else "No"
    tabla_libros = tabulate(libros_mostrar, headers="keys")
    print(tabla_libros)

def buscar_libros(libros):
    print("\nHas elegido buscar, introduce a continuación el título del libro:\n")
    time.sleep(1)
    titulo_buscar = input("Introduce el título del libro a buscar: ")
    for libro in libros:
        if libro["Titulo"].lower() == titulo_buscar.lower():
            estado = "Alquilado" if libro["Alquilado"] else "Disponible"
            print(f"--- Libro Encontrado ---\n")
            print(f" Título: {libro['Titulo']}\n Autor: {libro['Autor']}\n Estado: {estado}\n")
            return
    print(f"\nEl libro con título '{titulo_buscar}' no fue encontrado.\n")

def añadir_libros(libros):
    print("\nHas elegido añadir, introduce a continuación el título y el autor del libro que quieres añadir:")
    print()
    time.sleep(1)
    titulo = input("Introduce el título del nuevo libro: ")
    autor = input("Introduce el autor del nuevo libro: ")
    libros.append({"Titulo": titulo, "Autor": autor, "Alquilado": False})
    print(f"\nEl libro '{titulo}' ha sido añadido correctamente.\n")

def eliminar_libros(libros):
    print("\nHas elegido eliminar, introduce a continuación el título del libro que quieres eliminar:")
    print()
    time.sleep(1)
    titulo = input("Introduce el título del libro a eliminar: ")
    for libro in libros:
        if libro["Titulo"].lower() == titulo.lower():
            libros.remove(libro)
            print(f"\nEl libro con título '{titulo}' ha sido eliminado correctamente.\n")
            return
    print(f"\nEl libro con título '{titulo}' no fue encontrado.\n")

def alquilar_libros(libros):
    print("\nHas elegido alquilar, introduce a continuación el título del libro que quieres alquilar:")
    print()
    time.sleep(1)
    titulo = input("Introduce el título del libro a alquilar: ")
    for libro in libros:
        if libro["Titulo"].lower() == titulo.lower():
            if libro["Alquilado"]:
                print(f"\nEl libro '{titulo}' ya está alquilado.\n")
            else:
                libro["Alquilado"] = True
                print(f"\nEl libro '{titulo}' ha sido alquilado correctamente.\n")
            return
    print(f"\nEl libro con título '{titulo}' no fue encontrado.\n")

def devolver_libros(libros):
    print("\nHas elegido devolver, introduce a continuación el título del libro que quieres devolver:")
    print()
    time.sleep(1)
    titulo = input("Introduce el título del libro a devolver: ")
    for libro in libros:
        if libro["Titulo"].lower() == titulo.lower():
            if not libro["Alquilado"]:
                print(f"\nEl libro '{titulo}' no estaba alquilado.\n")
            else:
                libro["Alquilado"] = False
                print(f"\nEl libro '{titulo}' ha sido devuelto correctamente.\n")
            return
    print(f"\nEl libro con título '{titulo}' no fue encontrado.\n")

def main():
    while True:
        print("\nSelecciona el número de la acción que quieres realizar:\n")
        print("1. Visualizar todos los libros")
        print("2. Buscar libro por título")
        print("3. Añadir libro")
        print("4. Eliminar libro por título")
        print("5. Alquilar libro")
        print("6. Devolver libro")
        print("7. Salir")

        opcion = str(input("Selecciona el número de la acción que quieres realizar: "))

        if opcion == "1":
            visualizar_libros(libros)
        elif opcion == "2":
            buscar_libros(libros)
        elif opcion == "3":
            añadir_libros(libros)
        elif opcion == "4":
            eliminar_libros(libros)
        elif opcion == "5":
            alquilar_libros(libros)
        elif opcion == "6":
            devolver_libros(libros)
        elif opcion == "7":
            print("\n¡Muchas gracias por utilizar el gestor de la biblioteca!\n Esperamos verle pronto\n\n Saliendo del programa...")
            break
        else:
            print("\nOpción no válida. Por favor, selecciona una opción del 1 al 7.\n")
        # Espera 5 y limpia la pantalla
        time.sleep(5)
        os.system("cls")

print("\n¡Bienvenido a la Biblioteca de Data Science! ¿En qué le podemos ayudar hoy?\n")
time.sleep(1)
main()