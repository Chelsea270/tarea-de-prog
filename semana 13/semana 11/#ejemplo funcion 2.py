#ejemplo funcion 2
#identificando funciones por el usuario.
#definir la funcion suma

def suma():
    a=int(input("ingrese el primer digito: "))
    b=int(input("ingrese el segundo numero: "))
    resultado=a+b
    return resultado #se cierra la funcion

#principal
print(f"programa usando funciones en python")
resp=suma()
print("la suma es: ",resp)
