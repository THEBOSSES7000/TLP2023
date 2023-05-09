nombre1 = input("Ingrese el primer nombre: ")
nombre2 = input("Ingrese el segundo nombre: ")

if max(nombre1, nombre2) == nombre1:
    print("El nombre", nombre1, "es mayor alfabéticamente")
else:
    print("El nombre", nombre2, "es mayor alfabéticamente")
