#Ejercicio 5

#Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los dígitos en orden inverso:

#Ingrese numero: 345
#543
#Ingrese numero: 241
#142

number = int(input("Enter a three-digit number: "))
number2 = str(number)[::-1]
print(f""" The invert number is: {number2}""")