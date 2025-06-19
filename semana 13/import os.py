import os

Archivo="estudiantes.txt"

def cargar_estudiantes():
    estudiantes = []

    if os.path.exists(Archivo):
        with open(Archivo, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")

                estudiantes.append({
                "codigo": codigo,
                "nombre": nombre,
                "apellido": apellido,
                "carrera": carrera
            })
    return estudiantes

def guardar_estudiantes(estudiantes):
    with open(Archivo,"w") as archivo:
        for est in estudiantes:
            linea = f"{es['codigo']},{est['nombre']},{est['apellido']},{est['carrera']}\n" 
            archivo.write(linea)

def crear_estudiante(estudiantes):
    codigo=input("codigo del estudiante: ")

    if any(est["codigo"]== codigo for est in estudiantes):
        print("el codigo ya existe\n")
        return

    nombre=input("nombre: ")
    apellido=input("apellido: ")
    carrera=input("carrera: ")

    estudiantes.append({
        "codigo": codigo,
        "nombre": nombre,
        "apellido": apellido,
        "carrera": carrera
    })
    guardar_estudiantes(estudiantes)
    print("estudiantes agregado correctamente\n")

def mostrar_estudiantes(estudiantes):
    if not estudiantes:
        print("no hay estudiantes registrados\n")
        return

    print("\nlista de estudiantes: ")
    for est in estudiantes: 
        print(f"codigo: {est['codigo']}, nombre: {est['nombre']} apellido: {est['apellido']}, carrera: {est['carrera']}")
    print()

def actualizar_estudiantes(estudiantes):
    codigo=input("ingrese el codigo del estudiante a actualizar: ")
    for est in estudiante: 
        if est["codigo"] == codigo: 
            import os

Archivo="estudiantes.txt"

def cargar_estudiantes():
    estudiantes = []

    if os.path.exists(Archivo):
        with open(Archivo, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")

                estudiantes.append({
                "codigo": codigo,
                "nombre": nombre,
                "apellido": apellido,
                "carrera": carrera
            })
    return estudiantes

def guardar_estudiantes(estudiantes):
    with open(Archivo,"w") as archivo:
        for est in estudiantes:
            linea = f"{es['codigo']},{est['nombre']},{est[apellido]}," 
            import os

Archivo="estudiantes.txt"

def cargar_estudiantes():
    estudiantes = []

    if os.path.exists(Archivo):
        with open(Archivo, "r") as archivo:
            for linea in archivo:
                codigo, nombre, apellido, carrera = linea.strip().split(",")

                estudiantes.append({
                "codigo": codigo,
                "nombre": nombre,
                "apellido": apellido,
                "carrera": carrera
            })
    return estudiantes

def guardar_estudiantes(estudiantes):
    with open(Archivo,"w") as archivo:
        for est in estudiantes:
            if est["codigo"] == codigo:
                est["nombre"] = input(f"nuevo nombre(actual {est['nombre']}): ") or est["nombre"]
                est["apellido"] = input(f"nuevo apellido(actual {est['apellido']}): ") or est["apellido"]
                est["carrera"] = input(f"nuevo carrera(actual {est['carrera']}): ") or est["carrera"]
                guardar_estudiante(estudiantes)

                print("estudiante actualizado\n")
                return
            print("no se encontro estudiante de este codigo")


def eliminar_estudiante(estudiante):
    codigo=input("ingrese el codigo del estudiante a eliminar: ")
    for est in estudiante:
        if est["codigo"]== codigo:
            estudiante.remove(est)
            guardar_estudiante(estudiantes)
            print("\nestudiante eliminado")
            return
    print("\n no se encontro un estudiante con este codigo")

def menu():
    estudiantes=cargar_estudiantes()
    while True: 
        print("====== MENU CRUD ESTUDIANTES ======")
        print("1. ingresar estudiante")
        print("2. mostrar estudiante")
        print("3. actualizar estudiante")
        print("4. eliminar estudiante")
        print("5. salir")
        opcion=input("selecciona opcion (1-5): ")
         if opcion==1: 
            crear_estudiante(estudiantes)
        elif opcion==2:
            mostrar_estudiante(estudiantes)
        elif opcion==3:
            actualizar_estudiante:
        elif opcion==4:
            eliminar_estudiante:
        elif opcion==5:
            print("saliendo del programa...")
            break
        else: 
            print("\nopcion no valida.")

menu()