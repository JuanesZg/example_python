tIndividual = 2500
tDoble = 4600
tFamiliar = 5200
controlCiclo = 1

while controlCiclo != "0":
    planEstadia = int(input("Digite el número del tipo de hábitación que desea?\n1. Individual - Precio : 2500 / noche\n2. Doble - Precio : 4600 / noche\n3. Familiar - Precio : 5200 / noche\n"))
    diasEstadia = int(input("¿Cuántos días planea hospedarse en el hotel?\n"))
    if planEstadia == 1:
        costoEstadia = (tIndividual * diasEstadia)
        costoEstadiaIVA = costoEstadia + (costoEstadia*0.19)
        costoEstadiaDescuento = costoEstadiaIVA - (costoEstadiaIVA*0.05)
        print("El costo de su estadia de", diasEstadia,"dias es de",int(costoEstadia),"Sin IVA,",int(costoEstadiaIVA),"con IVA y,",int(costoEstadiaDescuento),"con el descuento sobre el IVA del 5%\n")
    elif planEstadia == 2:
        costoEstadia = (tDoble * diasEstadia)
        costoEstadiaIVA = costoEstadia + (costoEstadia*0.19)
        costoEstadiaDescuento = costoEstadiaIVA - (costoEstadiaIVA*0.09)
        print("El costo de su estadia de", diasEstadia,"dias es de",int(costoEstadia),"Sin IVA,",int(costoEstadiaIVA),"con IVA y,",int(costoEstadiaDescuento),"con el descuento sobre el IVA del 9%\n")
    elif planEstadia == 3:
        costoEstadia = (tFamiliar * diasEstadia)
        costoEstadiaIVA = costoEstadia + (costoEstadia*0.19)
        costoEstadiaDescuento = costoEstadiaIVA - (costoEstadiaIVA*0.15)
        print("El costo de su estadia de", diasEstadia,"dias es de",int(costoEstadia),"Sin IVA,",int(costoEstadiaIVA),"con IVA y,",int(costoEstadiaDescuento),"con el descuento sobre el IVA del 15%\n")
    elif planEstadia == 4:
        controlCiclo = 1
        print("Vuelva pronto!")
    controlCiclo= input("Presione 0 para terminar el programa, o cualquier otra tecla para repetirlo\n")
        