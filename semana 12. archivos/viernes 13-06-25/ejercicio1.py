# Escribe un programa que funcione como un diario simple. Cada vez que se
#ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora
#actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del
#archivo sin borrar las anteriores.

import datetime

entrada=input("inicie a escribir en su diario: ")

fecha_hora=datetime.datetime.now()
fecha_formateo=fecha_hora.strftime("%Y-%m-%d-%H:%m:%S")
with open("diario.txt","a",encoding="utf-8") as archivo:

    archivo.write(f"{fecha_formateo} - {entrada}\n")

print("entrada guardada exitosamente.")