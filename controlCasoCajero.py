#Pasar uno de los casos a codigo - Cajero automatico 
#Qué variables necesito para llevar a cabo el funcionamiento de un cajero automático en el cual solo realizaré la acción de sacar dinero en efectivo.
#Clave de la cuenta del usuario
clave = 4444
#Cuanto dinero hay en el cajero disponible para ser retirado
saldoCajero = 5000000
#Cuanto dinero posee en la cuenta la persona que desea retirar
saldoCuenta = 1200000
#Cuanto dinero desea retirar esta persona de su cuenta
valorRetirar = int(input("Cuanto dinero deseas retirar?\n"))
#Que el usuario ingrese la clave de su cuenta
contrasena = int(input("Ingrese los 4 digitos de su contraseña\n"))


if valorRetirar > saldoCajero:
    print("El cajero no tiene esta cantidad de dinero, intente en otro")
elif valorRetirar > saldoCuenta:
    print("No tiene suficiente dinero en la cuenta")
elif valorRetirar < saldoCajero and valorRetirar < saldoCajero:
    if contrasena == clave:
        print("Retiro exitoso, vuelva pronto")
    else:
        print("Clave incorrecta, intentelo nuevamente")