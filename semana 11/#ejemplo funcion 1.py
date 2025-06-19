#ejemplo funcion 1
#identificando funciones por el usuario.
#definir la funcion suma

def suma(a,b):
    resultado=a+b
    return resultado #se cierra la funcion

#principal
print(f"programa usando funciones en python")
num1=int(input("ingrese el primer digito: "))
num2=int(input("ingrese el segundo numero: "))
resp=suma(num1,num2)
print("la suma es: ",resp)
