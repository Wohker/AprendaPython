#Entrada.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
entrada=input()
print(type(entrada))
#En este apartado  tendremos que utilizar una función 
#la cual se guiara si es de tipo entero o no lo es en este
#caso utilizaremos booleano que al usarlo veremos que 
#si el numero que introduzcamos  es un entero será verdad
#y si contiene una decimal será falso.
esEntero=(entrada.isdigit() and entrada.find(“.”)==-1)
if (esEntero):
    #Si en al introducir el numero es entero nos arrojara en
    #la pantalla la frase muy bien.
    print('Dato entero.  ¡Muy bien! '')
else:
    #En esta parte si la condición no se cumple por ejemplo 
    #introducen 3.5 el programa arrojara que es falso.
    print('Dato no es entero. Intente nuevamente”)  
