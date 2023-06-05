numeros = []

while True:
    valor = int(input("Ingrese un valor entero (0 para finalizar): "))
    if valor == 0:
        break
    numeros.append(valor)

print("Tamaño de la lista:", len(numeros))
