#Ejercicio 3

#Escriba un programa que calcule el promedio de 4 notas ingresadas por el usuario:

#Primera nota: 55
#Segunda nota: 71
#Tercera nota: 46
#Cuarta nota: 87
#El promedio es: 64.75



grade1 = float(input("Enter the grade: "))
grade2 = float(input("Enter the grade: "))
grade3 = float(input("Enter the grade: "))
grade4 = float(input("Enter the grade: "))

average = ((grade1 + grade2 + grade3 + grade4) / 4)

print(f"""{average}""")