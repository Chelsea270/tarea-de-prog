#ejercicio 4 
#calcular el promedio de 3 calificaciones

def nota():
    nota1=int(input("ingrese la primera nota: "))
    nota2=int(input("ingrese la segunda nota: "))
    nota3=int(input("ingrese la tercera nota: "))
    resultado=(nota1+nota2+nota3)/3
    return resultado
print("el promedio es de: ",nota())

print("----------------------------------------------------")

def nota(a,b,c):
    resultado=(a+b+c)/3
    return resultado
 
not1=int(input("ingrese nota 1: "))
not2=int(input("ingrese nota 2: "))
not3=int(input("ingrese nota 3: "))

print("el promedio es de: ",nota(not1,not2,not3))
