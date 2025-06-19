#ejercicio 8
def calcPago(precio, cant): #definir funcion
    return precio * cant #cierre de la funcion

def main(): 
    productos = [] #lista de productos
    precios = [] #lista de precios
    cantidades = [] #lista de cantidades
    totales = [] #lista de totales
    resp = "SI" 

    while resp.upper() != "NO": #condicional while 
        producto = input("Producto ") #se ingresa el nombre del producto
        precio = float(input("Precio: ")) #precio en decimal
        cantidad = float(input("Cantidad: ")) #caltidad en decimal
        total = calcPago(precio, cantidad) 

        productos.append(producto) #agregar a lista de productos
        precios.append(precio) #agregar a lista de precios
        cantidades.append(cantidad) #agregar a lista de cantidad
        totales.append(total) #agregar a lista de totales 

        print("Desea agregar otro producto Si - No") #mandar a imprimir
        resp = input("Respuesta ") #ingresar respuesta

    print(f'\n {"Factura":^30}') #imprime factura
    print(f'{"Producto":<10}', f'{"Precio":>10}', f'{"Cantidad":>10}', f'{"Total":>10}')

    tam = len(productos) #cantidad de productos
    for i in range(tam):
        print(f'{productos[i]:<10} {precios[i]:10.2f} {cantidades[i]:10.2f} {totales[i]:10.2f}')

    monto = sum(totales) #total general
    print("Total a pagar C$: ", f"{monto:.2f}")

main()
