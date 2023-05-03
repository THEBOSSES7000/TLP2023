cantidad_triangulos=int(input("ingrese la cantidad de triangulos a calcular"))
contador=0
for i in range(cantidad_triangulos):
    base=int(input("ingrese la medidade la base del triangulo:")) 
    altura=int(input("ingrese la medida de la altura del triangulo:"))
    superficie=(base*altura)/2
    if superficie>=12:
        contador= contador + 1
print("cantidad de triangulos con superficie mayor a 12: ",contador)
