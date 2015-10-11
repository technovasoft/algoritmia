#Media Aritmetica
def mediaAritmetica():
	print("Dama una lista de datos")
	data=[1,2,436,3,6,2,4]
	#falta que los datos de la lista los ingrese el usuario
	print (data)
	dOrder=sorted(data)
	
	n=len(dOrder) 
	print ('Mediana Aritmetica: ', round(sum(data)*1.0/n,2))

#--------------------------------------------------------------------------------------------

#Mediana 
def mediana():

	print ("Mediana")
	print ("Corresponde al número intermedio después de ordenar los datos en forma ascendente o descendente.\n")
	print ("Ingresa 5 numeros los cuales deseas ordenar")
	n1 = input("Ingresa el primer numero\n>")
	n2 = input("Ingresa el segundo numero\n>")
	n3 = input("Ingresa el tercer numero\n>")
	n4 = input("Ingresa el cuarto numero\n>")
	n5 = input("Ingresa el quinto numero\n>")

	n1_1 = int(n1)
	n2_2 = int(n2)
	n3_3 = int(n3)
	n4_4 = int(n4)
	n5_5 = int(n5)

	lista = [n1_1,n2_2,n3_3,n4_4,n5_5]
	for recorrido in range(1,len(lista)):
	  for posicion in range(len(lista) - recorrido):
	      if lista[posicion] > lista[posicion + 1]:
	          temp = lista[posicion]
	          lista[posicion] = lista[posicion + 1]
	          lista[posicion + 1] = temp
	print ("La lista ordenada es:", lista)
	print ("La mediana es:",lista[2])
#Esto pude ser reducido a esto 
#from statistics import median
#median([1, 3, 5])
#pero aun asi usaremos lo de cesar n.n

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




