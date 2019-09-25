#Aleatorio.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
#En el programa python tiene múltiples librerías que los usuarios 
#comparten entre si por ende es muy rica en información.
#A las librerías también se le conocen como módulos 
#Por ejemplo en este caso se procederá a utilizar un modulo
#primero la debemos importar, con la instrucción import.
import random
#en este caso se definirá una  variable float, y se le asignara un valor.
numero1=float(7.5)
#en el programa python una función(es un conjunto de instrucciones 
#que procesan  una tarea especifica, como unidad de ejecucion) 
#Se procede a declarar con def. El total del código posicionado a la
#derecha de la definición, formando parte de la función.
def miFuncion():
    #En este caso se convertirá a float el numero aleatorio  generado
    #por random.randrage(). Esta función solo esta disponible si se
    #esta utilizando la importación desde el modulo random. 
    numero2=float(random.randrange(1,10))
    #En este caso se utilizara meta sustituciones para mostrar el resultado.
    mensaje='la suma de {} y {} es {}''
    print(menasaje.format(numero1,numero2,numero1+numero2))
    #Al terminari prosederemos a ejecutar la funcion definida 
    #en el codigo que acabamos de realizar.
miFuncion()
 