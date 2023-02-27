#If - Estructura de decisión
'''
edad = 19
edadRequerida = 18
boleta = True
'''
#Condicional simple
'''
if edad >= edadRequerida and boleta:
    print("Ingresa al evento")
'''
#Condicional compuesto
'''
if edad >= edadRequerida and boleta:
    print("Ingresa al evento")
else:
    print("No ingresa al evento")
'''
#Condicional anidado
'''
if edad >= edadRequerida and boleta:
    print("Ingresa al evento")
else:
    print("No ingresa al evento")
'''

#Ejercicio switches(case)
edad = int(input("Digite su edad\n"))
saldo = int(input("Que presupuesto tiene para su boleta?\n"))
print("Que tipo de boleta desea?\n1-Boleta VIP - Precio:500\n2-Boleta Preferencial - Precio:400\n3-Boleta General - Precio:200\n4-Boleta Baja - Precio:100\nIngrese 0 para salir")
opcion = int(input("Digite el numero de la opcion que desea adquirir\n"))

if saldo >= 500 and opcion == 1:
    boleta = "Boleta VIP"
elif saldo >= 400 and opcion == 2:
    boleta = "Boleta Preferencial" 
elif saldo >= 200 and opcion == 3:
    boleta = "Boleta General"
elif saldo >= 100 and opcion == 4:
    boleta = "Boleta Baja"
elif opcion == 0:
    boleta = "No tiene"
    print("Regrese pronto!")
else:
    boleta = "No tiene"
    print("No se ha podido comprar la boleta, elige una opción válida y que se ajuste a tu presupuesto")

if edad < 18 or boleta == "No tiene":
    print("Lo sentimos, no puedes ingresar al evento, no tienes la edad necesaria o has olvidado comprar tu boleta")
else:
    print("Bienvenid@ al evento, tienes una", boleta, "disfruta tu estadía")





