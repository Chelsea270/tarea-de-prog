#Se proporciona un archivo productos.csv donde cada línea contiene el nombre#
#de un producto, su precio y la cantidad en stock, separados por comas (ej: Laptop,1200,15).
#Escribe un programa que lea este archivo y muestre la información en un formato legible
#para el usuario, indicando el nombre, precio y stock de cada producto.
try:
    with open("productos.csv", "r", encoding="utf-8") as archivo:
        print("Lista de productos:\n")
        for linea in archivo:
            linea = linea.strip()
            if linea: 
                nombre, precio, stock = linea.split(",")
                print(f"Producto: {nombre}")
                print(f"Precio: ${precio}")
                print(f"Stock: {stock} unidades")
                print("-" * 30)
except FileNotFoundError:
    print("archivo no encontrado.")

