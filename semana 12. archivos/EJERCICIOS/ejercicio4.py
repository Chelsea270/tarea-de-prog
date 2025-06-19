#escribir un programa que escriba la lista de caracteres ASCII dentro de un archivo de texto

# Abrir (o crear) un archivo en modo escritura
with open("JOTACE", "w",encoding="utf-8") as archivo:
    # Recorremos los códigos ASCII imprimibles (del 32 al 126)
    for codigo in range(32, 127):
        # Convertimos el código a su carácter correspondiente
        caracter = chr(codigo)
        # Escribimos en el archivo el código y su carácter
        archivo.write(f"{codigo}: {caracter}\n")

print("La lista de caracteres ASCII se ha guardado en 'caracteres_ascii.txt'.")
