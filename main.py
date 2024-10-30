#Ejercicio 6

#Escriba un programa que reciba como entrada las longitudes de los dos catetos a y b
#de un triángulo rectángulo, y que entregue como salida el largo de la hipotenusa c
#del triangulo, dado por el teorema de Pitágoras: c2=a2+b2.

#Ingrese cateto a: 7
#Ingrese cateto b: 5
#La hipotenusa es 8.6023252670426267

import math

cathethus1 = float(input("Enter the first lenght: "))
cathethus2 = float(input("Enter the second lenght: "))

hypotenuse = math.sqrt ( (cathethus1) ** 2 + (cathethus2) ** 2 )

print(f"""The hypotenuse is: {hypotenuse} """)