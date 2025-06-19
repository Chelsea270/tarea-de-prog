#programa principal
import Modulo as md #importar modulo

#otra forma de importar modulos
from Modulo import Texto 

print("calcula las operaciones basicas con módulos. ")
n1=int(input("ingrese un numero: "))
n2=int(input("ingrese otro numero: "))
print(f"el producto es: {md.producto(n1,n2)}") 

resp=md.resta(n1,n2)
print(f"la resta de los dos numeros es: {resp} ")

respu=md.div(n1,n2)
print(F"la division es {respu}")

print(Texto)

#alias: sinonimos de un elemento

print(f"la suma es: {md.suma(n1,n2)}")