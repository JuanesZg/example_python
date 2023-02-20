"""
#Ejemplo de casting (Convertir a una variable de un tipo de dato a otro)
variable = 5
variableOne = float(variable)
variableTwo = str(variableOne)

#print(variableTwo + " Hola")
print(variable, variableOne, variableTwo)

# suma = variable + variableTwo (Validar a traves de una prueba que el dato si se encuentre como string)
print(type(variableTwo)) #(Imprime el tipo de dato de la variable)
print(type(variableOne))
print(type(variable))
#tipo = type(variableTwo)
#print(type(tipo))
"""

#Tipos de datos
variable1="Hola" #str - String
variable2=20 #int - Entero
variable3=20,8 #float - decimal
#print(variable3)
#print(type(variable3))
variable4=1j 
variable5 = ["Cantar","Jugar","Estudiar"] #Lista - List
variable6 = ("Cantar","Jugar","Estudiar") #Tupla - Tuple
carro = {"Color":'Rojo',"Velocidad":300, "Modelo":'GTR36'} #Diccionario - Dict
print(variable5)
print(variable6)
print(carro)

variable7 = True #Booleano - Bool
print(variable7)