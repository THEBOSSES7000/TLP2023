suma = 0

contador = 0

while contador < 10:
    valor = float(input("Ingrese un valor: "))
    
    suma += valor
    
    contador += 1

promedio = suma / 10

print("La suma total es:", suma)
print("El promedio es:", promedio)
