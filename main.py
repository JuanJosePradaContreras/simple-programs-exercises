#Ejercicio 7

#Escriba un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará
#el reloj dentro de h horas:

#Hora actual: 3
#Cantidad de horas: 5
#En 5 horas, el reloj marcara las 8
#Hora actual: 11
#Cantidad de horas: 43
#En 43 horas, el reloj marcara las 6


localhour = int(input("What time is it?: "))
advancehour = int(input("How many hours do you wanna advance: "))

futurehour = (localhour + advancehour) % 24

print(f"""The future hour is going to be: {futurehour}""")