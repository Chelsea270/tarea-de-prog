#realizar un programa que pida al usuario el nombre de un archivo de texto
#y, a continuacion permita almacenar al usuario tantas frases como el usuario desee.

#pedir al usuario que ingrese el nombre del archivo
nom=input("se le solicita al usuario ingresar el nombre de su archivo: ")
arch1=open(nom,"a")
while True:
    frase=input("ingrese alguna frase, la que quiera: ")
    arch1.write(frase+"\n")

    conti=input("desea agregar otra frase??: ")
    if conti.upper()=="NO": 
        break

arch1.close

print("se cerró el archivo con las frases guardadas exitosamente.")