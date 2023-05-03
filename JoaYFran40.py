# Definir variables para contadores y acumuladores
num_positivos = 0
num_negativos = 0
num_multiplos_15 = 0
acum_pares = 0

# Pedir al usuario que ingrese los 10 números enteros
for i in range(10):
    num = int(input("Ingrese un número entero: "))
    
    # Verificar si es positivo o negativo
    if num > 0:
        num_positivos += 1
    elif num < 0:
        num_negativos += 1
    
    # Verificar si es múltiplo de 15
    if num % 15 == 0:
        num_multiplos_15 += 1
    
    # Verificar si es par y sumar al acumulador
    if num % 2 == 0:
        acum_pares += num

# Mostrar resultados
print("Cantidad de valores positivos ingresados: ", num_positivos)
print("Cantidad de valores negativos ingresados: ", num_negativos)
print("Cantidad de múltiplos de 15 ingresados: ", num_multiplos_15)
print("Valor acumulado de números pares ingresados: ", acum_pares)
