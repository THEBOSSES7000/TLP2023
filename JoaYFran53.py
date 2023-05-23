oracion = input("Ingrese una oración: ")

vocales = 0
for caracter in oracion:
    if caracter.lower() in 'aeiouáéíóú':
        vocales += 1

oracion_mayusculas = oracion.upper()

cantidad_caracteres = len(oracion)

print("Cantidad de vocales:", vocales)
print("Oración en mayúsculas:", oracion_mayusculas)
print("Cantidad de caracteres:", cantidad_caracteres)
