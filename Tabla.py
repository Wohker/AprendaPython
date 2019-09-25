#Tabla.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
#Se le pedirá al usuario un numero entre el 1 y el 9.
numero=input('Dame un numero del 1 al 9”) 
numero=int(numero)
#A continuación escribiremos for que ejecutara un bloque de código
#un numero determinado de veces, cuando se pida que recorra
# un rango de valores.
for i in range (1,11):
    #Asi que i ira variando a cada iteración diferente.
    salida='{} x {} = {}”
    print(salida.format(numero,i,i*numero))
