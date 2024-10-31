#Ejercicio 9

#Un alumno desea saber que nota necesita en el tercer certamen para aprobar un ramo.

#El promedio del ramo se calcula con la siguiente formula.

#NC=(C1+C2+C3)3
#NF=NC⋅0.7+NL⋅0.3

#Donde NC es el promedio de certámenes, NL el promedio de laboratorio y NF la nota final.

#Escriba un programa que pregunte al usuario las notas de los dos primeros certamen y la nota de laboratorio, y muestre la nota que necesita el alumno para aprobar el ramo con nota final 60.

#Ingrese nota certamen 1: 45
#Ingrese nota certamen 2: 55
#Ingrese nota laboratorio: 65
#Necesita nota 72 en el certamen 3


grade_1 = float(input("What was your grade in the first contest?: "))
grade_2 = float(input("What was your grade in the second contest?: "))
lab_grade = float(input("What was your grade in the lab? :"))

final_note= 60

lb = lab_grade

grade_necesary = (final_note - lb * 0.3) / 0.7

grade_3 = grade_necesary * 3 - grade_1 - grade_2

print(f""" You need {grade_3 :.2f} in the third contest to pass""")