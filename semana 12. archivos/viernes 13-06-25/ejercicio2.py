#Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El
#programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene.
#Debe manejar el error en caso de que el archivo no exista.

ruta = input("Inserte el nombre del archivo: ")

try:
    with open(ruta, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
        print("El archivo contiene", len(lineas), "líneas.")

except FileNotFoundError:
    print(f"Error: El archivo '{ruta}' no existe.")

