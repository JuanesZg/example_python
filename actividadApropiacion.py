'''
#Cajero Electronico
SaldoCajero= 500000
SaldoCuenta = 120000
ValorRetirar = 50000
Contraseña = 8765
NúmeroCuenta = 5000400030002000
TipoCuenta = "Corriente"
print("\n",SaldoCajero,"\n", SaldoCuenta,"\n", ValorRetirar,"\n", Contraseña,"\n", NúmeroCuenta,"\n", TipoCuenta)
'''
'''
#Usar un chat
EstadoAmigo = "Activo"
NombreUsuarios = "JeroToBe"
ContenidoMensaje = "Hola amigo, ¿Como estas?"
print("\n",EstadoAmigo,"\n", NombreUsuarios,"\n", ContenidoMensaje)
'''
'''
#Pagar con tarjeta de credito 
TasaInteres= "20%"
LímiteTarjeta=5000000
Contraseña=5634
NúmeroCuenta = 5000400030001000
NúmeroIdentificación = 30304040786
print("\n",TasaInteres,"\n", LímiteTarjeta,"\n", Contraseña,"\n", NúmeroCuenta,"\n", NúmeroIdentificación)
'''
'''
#Lavar la ropa
Método = "Lavadora"
AguaDisponible = "8L"
JabonesDisponibles = 3
DetergentesDisponibles = 2
CantidadCamisas = 6
CantidadPantalones = 3
CantidadMedias = 6
print("\n",Método,"\n", AguaDisponible,"\n", JabonesDisponibles,"\n", DetergentesDisponibles,"\n", CantidadCamisas,"\n", CantidadPantalones,"\n", CantidadMedias)
'''
'''
#Hablar por telefono
EstadoAmigo = "No disponible"
NumeroAmigo = 3015749865
SaldoTelefonico = 0
Dinero = 12000
CostoMinutero = 400
ModeloTelefono = "Motorola E20"
ValorRecarga = 3000
print("\n",EstadoAmigo,"\n", NumeroAmigo,"\n", SaldoTelefonico,"\n", Dinero,"\n", CostoMinutero,"\n", ModeloTelefono,"\n", ValorRecarga)
'''

#Caso 1. El almacén WC distribuye los siguientes artículos
Articulos = {
    "Articulo1":"Zapatos", "Precio1":350000, 
    "Articulo2":"Tenis", "Precio2":280000, 
    "Articulo3":"Camisetas", "Precio3":175000,
    "Articulo4":"Jeans", "Precio4":200000
    }

#Muestra en la consola los artículos y precios actuales
print(Articulos)

#También mostrar el costo total de los cuatro artículos
print("El precio total es $",Articulos["Precio1"]+Articulos["Precio2"]+Articulos["Precio3"]+Articulos["Precio4"])

#Además, el promedio de venta(precios)
print("El promedio de los precios es $",int((Articulos["Precio1"]+Articulos["Precio2"]+Articulos["Precio3"]+Articulos["Precio4"]) / 4))

#Subir el precio de los Jeans en un 6.2%
Articulos["NuevoPrecio4"] = int(Articulos["Precio4"]+(Articulos["Precio4"]*0.062))

#Disminuir el precio de los Zapatos en un 0.8%
Articulos["NuevoPrecio1"] = int(Articulos["Precio1"]-(Articulos["Precio1"]*0.008))

#Por último, mostrar el nuevo valor de los Zapatos y de los Jeans
print("El nuevo precio de los Jeans es", Articulos["NuevoPrecio4"], "y el nuevo precio de los Zapatos es", Articulos["NuevoPrecio1"])