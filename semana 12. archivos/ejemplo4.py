#readline en una lista de archivos 
arch1=open("datos.txt","r")
lineas=arch1.readline()
print("el archivo tiene",len(lineas)," lineas")
print("el contenido del archivo")
for linea in lineas:
    print(lineas,end='')
arch1.close()
