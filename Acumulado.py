#Acumulado.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
#Primero declararemos las variables de trabajo, con tipo explicito.
acumulado=int(0)
numero=str("")
#Colocaremos true como la condicional de while de este modo se crea
#un ciclo infinito  que correrá hasta que  de forma explicita
#se utilice  la instrucción break.
while True:
    numero=input('Dame un numero entero:”)
    if  numero=="":
        #En dado caso del que numero sea vacio se reporta el caso y sale.
        print("vacio. Salir del programa.")
        break
    else: 
        #en dado caso si se proporciona un valor acumulado= acumulado + numero se
        #procede a realizar el calculo usando suma incluyente(+=).
        Acumulado+)int(numero)
        Salida=“Monto acumulado {}”  
        print(salida.format(acumulado))
