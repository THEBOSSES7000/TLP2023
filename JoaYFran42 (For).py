# Inicializamos la variable para almacenar la suma total
suma = 0

# Iteramos 10 veces con el ciclo for
for i in range(10):
    # Solicitamos el valor al usuario y lo convertimos a float
    valor = float(input("Ingrese un valor: "))
    
    # Sumamos el valor a la suma total
    suma += valor

# Calculamos el promedio
promedio = suma / 10

# Mostramos el resultado por pantalla
print("La suma total es:", suma)
print("El promedio es:", promedio)
