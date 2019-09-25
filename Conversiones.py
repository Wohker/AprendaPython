#Conversiones.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
#Hola_mundo.py     
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
#elaboramos un nuevo programa donde
#declararemos una variable str, con una cadena de varios numeros .
numero='1234'
#se indica el tipo  que tiene la variable num. Y con la salida type()
#sara el cambio de  dato y  se indica que no es un dato str, si no un dato type.
print(type(numero))
#ahora se prosedera a realizar la novercion :se convierte la cadena a su equivalencia int.
numero=int(numero).
#se muestra el tipo de cambio pero se sigue usando la misma variable.
print(type(numero))
# ahora se declarara una str con meta sustitucion (pisicion en la cual iran los
#valores proporcionados usando format).
Salida='el numero utilizado es{}''
#ahora se prosedera a mostrar el resultado. La meta susitucion hara que donde estan los las llaves {}
#se coloque el valor del numero que se indique.
print(salida.format(numero))
