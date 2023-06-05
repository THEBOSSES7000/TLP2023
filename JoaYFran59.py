numeros = []

for i in range(5):
    numero = int(input("Ingrese un número entero: "))
    numeros.append(numero)

print("Elementos iguales o superiores a 7:")
for numero in numeros:
    if numero >= 7:
        print(numero)
