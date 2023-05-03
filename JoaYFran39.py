cuadrante_1 = 0
cuadrante_2 = 0
cuadrante_3 = 0
cuadrante_4 = 0

num_puntos = int(input("Ingrese el número de puntos a analizar: "))
for i in range(num_puntos):
    punto = input("Ingrese las coordenadas del punto (x,y): ")
    coordenadas = punto.split(",")
    x = int(coordenadas[0])
    y = int(coordenadas[1])
    
    if x > 0 and y > 0:
        cuadrante_1 += 1
    elif x < 0 and y > 0:
        cuadrante_2 += 1
    elif x < 0 and y < 0:
        cuadrante_3 += 1
    elif x > 0 and y < 0:
        cuadrante_4 += 1

print("Cantidad de puntos en el 1º cuadrante: ", cuadrante_1)
print("Cantidad de puntos en el 2º cuadrante: ", cuadrante_2)
print("Cantidad de puntos en el 3º cuadrante: ", cuadrante_3)
print("Cantidad de puntos en el 4º cuadrante: ", cuadrante_4)
