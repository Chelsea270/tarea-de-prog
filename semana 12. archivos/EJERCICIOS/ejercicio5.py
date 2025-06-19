#escribir un programa que lea y muestre en pantalla el archivo 

arch1=open("JOTACE","r")
linea=arch1.readline()
while linea!='':
    print(linea,end='')
    linea=arch1.readline()
arch1.close()
