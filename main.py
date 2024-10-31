#Ejercicio 8

#Escriba un programa que entregue la parte decimal de un número real ingresado por el usuario.

#Ingrese un numero: 4.5
#0.5
#Ingrese un numero: -1.19
#0.19


number = float(input("Enter your number: "))

decimal_part =  number - int(number)

print(f"""The decimal part from your number is: {decimal_part :.2f}""")