def calcPago(precio, cant):
    return precio * cant

def main():
    producto = input("Nombre del producto: ")
    precio = float(input("Precio C$: "))
    cantidad = float(input("Cantidad: "))
    total = calcPago(precio, cantidad)

    print("Producto: ", producto)

    print(f'\n{"Factura":^30}')
    print(f'{"Precio":>10}', f'{"Cantidad":>10}', f'{"Total":>10}')
    print(f'{precio:10.2f} {cantidad:10.2f} {total:10.2f}')

main()
