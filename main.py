#Ejercicio 10

#Cuando un huevo es hervido en agua, las proteínas comienzan a coagularse cuando la temperatura sobrepasa un punto crítico. A medida que la temperatura 
#aumenta, las reacciones se aceleran.

#En la clara, las proteínas comienzan a coagularse para temperaturas sobre 63°C, mientras que en la yema lo hacen para temperaturas sobre 70°C. 
#Para hacer un huevo a la copa, la clara debe haber sido calentada lo suficiente para coagularse a más de 63°C, pero la yema no debe sobrepasar los 
#70°C para evitar obtener un huevo duro.

#El tiempo en segundos que toma al centro de la yema alcanzar Ty, °C está dado por la fórmula:

#t=M2/3cρ1/3Kπ2(4π/3)2/3ln[0.76To−TwTy−Tw], donde M es la masa del huevo, ρ su densidad, c su capacidad calorífica específica 
#y K su conductividad térmica. Algunos valores típicos son:

#M=47[g] para un huevo pequeño y M=67[g] para uno grande,
#ρ=1.038[gcm−3],
#c=3.7[Jg−1K−1], y
#K=5.4⋅10−3[Wcm−1K−1].
#Tw es la temperatura de ebullición del agua y To la temperatura original del huevo antes de meterlo al agua, ambos en grados Celsius.

#Escriba un programa que reciba como entrada la temperatura original del huevo y muestre como salida el tiempo en segundos que le toma alcanzar la temperatura máxima para prepararlo a la copa.

import math

original_temp_egg = float(input("Original temperature from the egg\n"))
boiling_temp_wat= 100 
yolk_temp_coagulate = 70 
egg_mass= 67 
density_from_egg= 1.038 
cap_cal_egg= 3.7 
cond_term_egg = 5.4 * math.pow(10, -3) 
dividing = math.pow(egg_mass, (2/3)) * (cap_cal_egg * (math.pow(density_from_egg, (1/3))))
divider = (cond_term_egg * math.pow(math.pi, 2)) * math.pow((4*math.pi) / 3, (2/3))
result = dividing / divider

second_result = math.log(0.76 * ((original_temp_egg - boiling_temp_wat) / (yolk_temp_coagulate - boiling_temp_wat)))

seconds = result * second_result


print(f"The max time to prepare the egg is {seconds :.2f} seconds")