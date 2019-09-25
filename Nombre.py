#Nombre.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
nombre =input('Nombre:')
apellidos=input('Apellidos:'')
#en este caso se conectaran los valores de tipo str,
#junto con la literal ” ”.
nombreCompleto=nombre+' '+apellidos
#ahora le colocara a la variable la representación en 
#mayúscula de todo el  contenido
nombreCompleto=nombreCompleto.upper()
print(nombreCompleto)
