# Definir variables para las edades y promedios de cada turno
edades_manana = []
edades_tarde = []
edades_noche = []

promedio_manana = 0
promedio_tarde = 0
promedio_noche = 0

# Pedir al usuario que ingrese las edades de los alumnos de cada turno
for i in range(5):
    edad_manana = int(input("Ingrese la edad de un alumno del turno mañana: "))
    edades_manana.append(edad_manana)
    
    edad_tarde = int(input("Ingrese la edad de un alumno del turno tarde: "))
    edades_tarde.append(edad_tarde)
    
    edad_noche = int(input("Ingrese la edad de un alumno del turno noche: "))
    edades_noche.append(edad_noche)

# Calcular los promedios de cada turno
promedio_manana = sum(edades_manana) / len(edades_manana)
promedio_tarde = sum(edades_tarde) / len(edades_tarde)
promedio_noche = sum(edades_noche) / len(edades_noche)

# Mostrar los promedios de cada turno
print("El promedio de edades del turno mañana es:", promedio_manana)
print("El promedio de edades del turno tarde es:", promedio_tarde)
print("El promedio de edades del turno noche es:", promedio_noche)

# Determinar el turno con el mayor promedio de edades
mayor_promedio = max(promedio_manana, promedio_tarde, promedio_noche)

if mayor_promedio == promedio_manana:
    print("El turno con mayor promedio de edades es: mañana")
elif mayor_promedio == promedio_tarde:
    print("El turno con mayor promedio de edades es: tarde")
else:
    print("El turno con mayor promedio de edades es: noche")
