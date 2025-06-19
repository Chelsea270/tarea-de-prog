#ejemplo 5 
def prod(num1, num2):
    return num1*num2

numero1=int(input("ingrese un numero: "))
numero2=int(input("ingrese un numero: "))
resp=prod(numero1,numero2)
print(numero1," * ",numero2," = ",resp)

print("tabla de multiplicar del numero")

num=int(input("ingrese un numero: "))
for i in range(1,13):
    r=prod(num,i)
    print(num," * ",i," = ",r)
