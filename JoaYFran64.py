alturas = []

for i in range(5):
    altura = float(input("Ingrese la altura de la persona {}: ".format(i + 1)))
    alturas.append(altura)

promedio = sum(alturas) / len(alturas)

contador_mayores = 0
contador_menores = 0

for altura in alturas:
    if altura > promedio:
        contador_mayores += 1
    elif altura < promedio:
        contador_menores += 1

print("Promedio de alturas:", promedio)
print("Cantidad de personas más altas que el promedio:", contador_mayores)
print("Cantidad de personas más bajas que el promedio:", contador_menores)
