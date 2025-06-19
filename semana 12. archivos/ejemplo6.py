#se le solicitan los datos al usuario
nombre=input("ingrese el nombre del usuario: ")
apellido=input("ingrese el apellido del usuario: ")
edad=int(input("ingrese la edad del usuario: "))
salario=float(input("ingrese el salario del usuario: "))

linea=f"{nombre} {apellido} tiene {edad} y cuenta con un salario de {salario}"

with open("datos_usuario.txt","a") as archivo:
    archivo.write(linea)

print("datos guardados correctamente en 'datos_usuario.txt'. ")


#trabajar con archivos en python 
#1. abrir el archivo en modo 'creacion'
#solicita el nombre del archivo

ruta=input("se le solicita al usuario ingresar el nomnre del archivo: ")
arch1=open(ruta,"a")

arch1.write("primera linea\n")
arch1.write("segunda linea\n")
arch1.close()

print("se cerró el archivo")    