proyecto=input("En que proyecto trabaja?\n")
if proyecto == "A":
    proyecto = 20000
elif proyecto == "B":
    proyecto = 10000
else:
    proyecto = 5000

# Mostrar por consola el valor de la hora día
print("El valor por hora de su día es de", proyecto)

#Calcular el sueldo mensual
sueldoMensual = (proyecto*8)*30
print("Su sueldo mensual es de",sueldoMensual)

if sueldoMensual > 1500000:
    print("Su salario es mayor al tope máximo")
else:
    horaExtra = (proyecto * 0.06) + proyecto
    sueldoMensual = sueldoMensual + (horaExtra*3)
    print("Su nuevo salario con horas extras es de", int(sueldoMensual))
