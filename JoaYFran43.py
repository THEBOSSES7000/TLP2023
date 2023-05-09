nombre1 = input("Ingrese el nombre de la primera persona: ")
edad1 = int(input("Ingrese la edad de la primera persona: "))
altura1 = float(input("Ingrese la altura de la primera persona: "))
nombre2 = input("Ingrese el nombre de la segunda persona: ")
edad2 = int(input("Ingrese la edad de la segunda persona: "))
altura2 = float(input("Ingrese la altura de la segunda persona: "))

print("\nDatos de la primera persona:")
print("Nombre:", nombre1)
print("Edad:", edad1)
print("Altura:", altura1)

print("\nDatos de la segunda persona:")
print("Nombre:", nombre2)
print("Edad:", edad2)
print("Altura:", altura2)

if altura1 > altura2:
    print("\nLa persona más alta es", nombre1, "con una altura de", altura1)
elif altura2 > altura1:
    print("\nLa persona más alta es", nombre2, "con una altura de", altura2)
else:
    print("\nAmbas personas tienen la misma altura.")
