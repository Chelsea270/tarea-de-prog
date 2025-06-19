#Realizar un programa que pida al usuario el nombre o ubicacion de un archivo de texto y, 
#a continuacion de lectura a todo el archivo

nom1=input("se le solicita al usuario localizar un archivo: ")
arch1=open(nom1)

try:
    with open(nom1,"r") as archivo:
        cont=archivo.read()
        print("el contenido en cuestion: \n")
        print(cont)

except FileNotFoundError:
    print("se a producido un error")
