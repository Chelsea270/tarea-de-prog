#realizar un programa que pida al usuario el nombre de un archivo de texto y,
#a continuacion añada texto en él hasta que el usuario lo decida

nomb=input("se le solicita ingresar el nombre del archivo: ")
archi=open(nomb,"a")

while True:
    text=input("agregue algun texto: ")
    archi.write(text+"\n")
    continuar=input("desea agregar mas texto?: ")

    if continuar.upper()=="NO":
        break

archi.close()
print("adios.")