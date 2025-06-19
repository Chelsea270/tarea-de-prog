# identificando archivos de texto en python.
#creando el archivo datos.txt

arch1=open("datos.txt","w",encoding="utf-8")   #nombre del archivo. se abrira en escritura por "w"
arch1.write("primera línea\n")
arch1.write("segunda línea\n")
arch1.write("tercera línea\n")
arch1.close()
print("fin del programa")
