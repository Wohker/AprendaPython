#Compra.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
numero1=input('Numero 1:”)
numero2=input('Numero 2:”)
Salida='Números proporcionados: {} y {}. {}.”
if(numero1==numero2):
   #En dado caso de que los números introducidos son iguales
   #se mostrara lo siguiente:.
   print(salida.format(numero1, numero2, 'Los números son iguales”))
else: 
    #En este apartado se hacen notar las condicionales anidadas
    #if dentro de otro if.
    #En dado caso si los números no son iguales.
    if numero1>numero2:
        #En este apartado se reporta si el numero es mayo que el segunda.
        print(salida.format(numero1, numero2,'El mayor es el primero”))
    else:
        # si es 0 de lo contrario, si el primero es mayor que el segundo.
        print(salida.format(numero1, numero2'El mayor es el segundo”))
