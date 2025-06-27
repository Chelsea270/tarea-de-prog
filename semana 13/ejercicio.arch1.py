#lectura de un archivo de texto simple
#escribir un programa que lea un archivo de texto simple llamado "poema.txt" e imprima su contenido linea por linea
arch1= open("poema.txt", "r")
contenido = arch1.readlines()
print(contenido)
arch1.close()
print("fin del codigo")
