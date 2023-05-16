nombre = input("Ingrese tu nombre en minúscula: ")

primer_caracter = nombre[0]

if primer_caracter in ['a', 'e', 'i', 'o', 'u']:
    print("¡Wow! Tu nombre comienza con una vocal.")
else:
    print("El nombre no comienza con una vocal.")
