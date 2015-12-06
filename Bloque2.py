#Media Aritmeritica
print ("Media Aritmetica:")
print("Ingresa el numero de datos que ingresaras")
x = int(input(">"))
datos = [0]*x
for i in range(x):
    datos[i]=float(input("dato >"))
suma=0
for i in range(x):
    suma+=datos[i]
ari = suma/x
print("Suma:",suma)
print ("La media aritmertica es:",ari)



#--------------------------------------------------------------------------------------------

#Mediana 
print ("Mediana")
print ("Corresponde al número intermedio después de ordenar los datos en forma ascendente o descendente.\n")
print ("Ingresa el numero de datos que ingresaras")
x = int(input(">"))
print("ingesa los datos para ordenar")
lista = [0]*x
for i in range(x):
  lista[i]=int(input(">"))
  for recorrido in range(1,len(lista)):
    for posicion in range(len(lista) - recorrido):
      if lista[posicion] > lista[posicion + 1]:
          temp = lista[posicion]
          lista[posicion] = lista[posicion + 1]
          lista[posicion + 1] = temp
print ("La lista ordenada es:", lista)
print ("La mediana es:",lista[2])


#--------------------------------------------------------------------------------------------
#Moda
def moda():
	import numpy as np #Se necesita esta libreria
	import scipy.stats #Esta tambien se descarga
	a = np.array([1,2,3,1,2,1,1,1,3,2,2,1])
	b = (3,4,5,6,7,8,5,5,6,2,3,1,2,5,5,1,3,2,2,1)
	print "La moda del set a es: ", scipy.stats.mode(a)[0][0], "y se repite",scipy.stats.mode(a)[1][0] ,"veces"
	print "La moda del set b es: ", scipy.stats.mode(b)[0][0], "y se repite",scipy.stats.mode(a)[1][0] ,"veces"
	#http://www.numpy.org/
	#en el link se bajan las dos librerias que se utiliza

#---------------------------------------------------------------------------------------------

import math
print ("Media Geometrica:")
print("Ingresa el numero de datos que ingresaras")
x = int(input(">"))
datos = [0]*x
for i in range(x):
    datos[i]=float(input("dato >"))
multi = 1
for i in range(x):
    multi*=datos[i]
geo = math.pow(multi,1/x)
print("√",multi)
print ("La media aritmertica es:",geo)
	   
#------------------------------------------------------------------------------------------------------------------------------

print("Ingresa el numero de datos que ingresaras")

x = int(input(">"))
datos = [0]*x

for i in range(x):
    datos[i]=float(input("dato >"))

suma = 0
for i in range(x):
    suma+=1/datos[i]

aro = x/suma

print ("Media Armónica: ", aro)
