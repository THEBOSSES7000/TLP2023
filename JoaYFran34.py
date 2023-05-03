contador=0
num=int(input("ingrese un numero "))
for x in range (num):
    num2=int(input("ingrese un numero "))
    if num2>=1000:
        contador=contador+1
print ("La cantidad de numeros mayores o igual a 1000 son ", contador)
