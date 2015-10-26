#!/usr/bin/python
#hacen paro de correr esta mierda plox?
import math
#tabla de distribucion de frecuencias
print("***********TABLA DE DISTRIBUCION DE FRECUENCIAS**************")
#obtenemos el tamaño del vector
tama = int(input("digite la cantidad de datos que va a ingresar"))
datos = [0]*tama #creamos el vector de la cantidad que tiene la variable tama	
i= 0
print ("ingrese sus datos")
while i < tama:
	datos[i]=int (input ("dato: "))
	i+=1
#comienza metodo de ordenacion por seleccion
i=0
while i < tama:
	mayor= i
	j=i+1
	y=0
	while j < tama:
	    if datos[mayor]<datos[j]:
	        mayor = j
	    j+=1
	aux = datos[mayor]
	datos[mayor]=datos[i]
	datos[i]=aux
	i+=1
	  
print("estos son sus datos ordenados decendentemente")
print(datos)
m = ceil(1 + 3.3*log10(tama))
r = datos[0]-datos[tama-1]
a= ceil(r/m)-0.1
print("------------------------------------------")
print("------------------------------------------")
print("---------------Respuestas-----------------")


print("m = ",m," R= ",r," A = ",a)
