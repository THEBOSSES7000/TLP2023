suma = 0
while True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        suma += num1 + num2
        opc = input("¿Desea agregar otro número? (S/N): ").lower()
        if opc != 's':
            break
    except ValueError:
        print("Error: Debe ingresar un número válido")

print("La suma total de los números ingresados es:", suma)
