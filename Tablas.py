#Tablas.py
# Autor: Daniel Isai Saldaña Rodríguez
#Fecha de creación: 25/09/2019
for i  in range(1,11):
    encabezado='tabla del {}”
    print(encabezado.format(i))
    #El print  sin nada dentro de  el hace un salto de linea
    print()
    #También dentro de un for se puede poner otro for.
    for j in range(1,11):
        #Vemos que ’i’  contiene el numero de base de
        #la tabla y ‘j’ el elemento de la tabla.
        salida='{} x {} = {}”
        print(salida.format(i,ji*j))
    else:
       #Ya terminando las interacion  indicadas se procede
       #a ejecutar el código  y se produce el salto de línea.
print()
