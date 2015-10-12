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

#---------------------------------------------------------------------------------------------

import math
print ("MEDIA GEOMÉTRICA")
print ("La media geometrica de una cantidad finita de números(digamos N números)\nes la raíz enésima del producto de todos los números.")

print ("n√Σ x")
#Lo dejo del 1 al 5 mientras es que me dio sueño y me salio orita a las 3 am xD
#Yo creo que lo seguire hasta 10
numero = input("ingresa el numero de n del 1 al 5\n>")
num = int(numero)

if (num == 1):
    print ("Haz seleccionado 1")
    x = input("Ingresa el numero que desees calcular\n")
    x1 = float(x)
    raiz = (x1 ** (1/1))
    print (raiz)

elif (num == 2):
    print ("Haz seleccionado 2")
    x = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x_ = float (x)
    x_2=float (x2)
    mult = (x_ * x_2)
    print ("=2√",x,"x",x2)
    print ("=2√",mult)
    raiz = (mult ** (1/2))
    print ("El resultado es:",raiz)

elif (num == 3):
    print ("Haz seleccionado 3")
    x  = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x3 = input ("Ingresa el tercer numero\n>")
    x_= float (x)
    x_2 = float (x2)
    x_3 = float (x3)
    mult = (x_ * x_2 * x_3)
    print ("=3√",x,"x",x2,"x",x3)
    print ("=3√",mult)
    raiz = (mult ** (1/3))
    print ("El resultado es:",raiz)

elif (num == 4):
    print ("Haz seleccionado 4")
    x  = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x3 = input ("Ingresa el tercer numero\n>")
    x4 = input ("Ingresa el cuarto numero\n>")
    x_= float (x)
    x_2 = float (x2)
    x_3 = float (x3)
    x_4 = float (x4)
    mult = (x_ * x_2 * x_3 * x_4)
    print ("=4√",x,"x",x2,"x",x3,"x",x4)
    print ("=4√",mult)
    raiz = (mult ** (1/4))
    print ("El resultado es:",raiz)

elif (num == 5):
    print ("Haz seleccionado 5")
    x  = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x3 = input ("Ingresa el tercer numero\n>")
    x4 = input ("Ingresa el cuarto numero\n>")
    x5 = input ("Ingresa el quinto numero\n>")
    x_= float (x)
    x_2 = float (x2)
    x_3 = float (x3)
    x_4 = float (x4)
    x_5 = float (x5)
    mult = (x_ * x_2 * x_3 * x_4 * x_4)
    print ("=5√",x,"x",x2,"x",x3,"x",x4,"x",x5)
    print ("=5√",mult)
    raiz = (mult ** (1/5))
    print ("El resultado es:",raiz)

else:
    print ("Caracter no valido")



