sueldos_manana = []
sueldos_tarde = []

print("Ingrese los sueldos de los empleados del turno de mañana:")
for i in range(4):
    sueldo = float(input("Sueldo del empleado {}: ".format(i + 1)))
    sueldos_manana.append(sueldo)

print("\nIngrese los sueldos de los empleados del turno de tarde:")
for i in range(4):
    sueldo = float(input("Sueldo del empleado {}: ".format(i + 1)))
    sueldos_tarde.append(sueldo)

print("\nLista de sueldos del turno de mañana:", sueldos_manana)
print("Lista de sueldos del turno de tarde:", sueldos_tarde)
