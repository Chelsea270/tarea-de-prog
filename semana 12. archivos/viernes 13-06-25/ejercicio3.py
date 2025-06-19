#: Crea un programa que permita al usuario crear una lista de compras. El programa
#solicitará al usuario que ingrese productos uno por uno y los guardará en un archivo llamado
#compras.txt. El usuario indicará que ha terminado de añadir productos introduciendo la
#palabra "fin".

with open("compras.txt","a") as archivo:
    while True:
        producto=input("ingrese una producto: ")
        if producto.lower()== 'fin':
           break
        archivo.write(producto + "\n")