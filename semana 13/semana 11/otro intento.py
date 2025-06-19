#ejemplo 6..
#nombre completo

def nom_comp(nom, ape):
    print("tu nombre completo es: ",nom.title(),ape.title())

def main():
    print("dime tu nombre: ")
    nombre=input()
    print("dime tu apellido: ")
    apellido=input()
    nom_comp(nombre,apellido)
main()