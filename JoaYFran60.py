nombres = []

for i in range(5):
    nombre = input("Ingrese el nombre #" + str(i+1) + ": ")
    nombres.append(nombre)

contador = 0

for nombre in nombres:
    if len(nombre) > 5:
        contador += 1

print("Cantidad de nombres con más de 5 caracteres:", contador)
