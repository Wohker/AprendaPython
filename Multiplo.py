#Multiplo.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
#Al principio debemos de capturar un numero y se almacenara una ves que 
#es convertido a int
numero=int(input('Dame un numero entero ”))
#Se almacenara en fomra  de valor booleano la evaluación de residuales
#de ser 0 el residual quiere decir que el numero si es múltiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
#Al usar and  se revisa si es verdadero  si es que todas las condiciones son verdaderas
#al  usar el or se revisa si al menos una condición es verdadera. Al usar los paréntesis
#le indican a python que  las primeras 2 condicionales son juntas y la 3 es independiente
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
   print('Correcto”)
else:
    print('Incorrecto”)
