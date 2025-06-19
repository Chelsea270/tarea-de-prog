 #leer el contenido del archivo de texto linea por linea
arch1=open("datos.txt","r")
linea=arch1.readline()
while linea!='':
    print(linea,end='')
    linea=arch1.readline()
arch1.close()

#for 
arch1=open("datos.txt","r")
for linea in arch1:
    print(linea,end='')
arch1.close()