clave = input("Ingrese una clave: ")

longitud = len(clave)

if longitud >= 10 and longitud <= 20:
    print("La clave es válida.")
else:
    print("La clave no cumple con los requisitos de longitud.")
