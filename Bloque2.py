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

import math
print ("MEDIA ARMÓNICA")
print ("La media armónica, denominada H, de una cantidad finita de numeros es igual al reciproco, o inverso, de la media aritmetica de los reciprocos de dichos valores\nAsi, dados los numeros X1,X2,...,Xi con sus respectivas frecuencias absolutas N1,N2m,...,Ni, siendo N el numero total de datos, la media armonica derá igual a:")

print ("H = N/n√Σ 1/x esto es H = N/1/x1 + 1/x2 + ... 1/Xn")

numero = input("Ingresa el numero de N del 1 al 6\n>")
num = int(numero)

if (num == 1):
    print ("Haz seleccionado 1")
    x = input("Ingresa el numero x que desees calcular\n")
    x1 = float(x)
    arm = (1/x1)
    print (arm)
    

elif (num == 2):
    print ("Haz seleccionado 2")
    x = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x_ = float (x)
    x_2=float (x2)
    suma = (1/x_ + 1/x_2)
    arm = (2/suma)
    print (arm)

elif (num == 3):
    print ("Haz seleccionado 3")
    x = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x3 = input ("Ingresa el tercer numero\n>")
    x_ = float (x)
    x_2 = float (x2)
    x_3 = float (x3)
    suma = (1/x_ + 1/x_2 + 1/x_3)
    arm = (3/suma)
    print (arm)

elif (num == 4):
    print ("Haz seleccionado 4")
    x = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x3 = input ("Ingresa el tercer numero\n>")
    x4 = input ("Ingresa el cuarto numero\n>")
    x_ = float (x)
    x_2 = float (x2)
    x_3 = float (x3)
    x_4 = float (x4)
    suma = (1/x_ + 1/x_2 + 1/x_3 + 1/x_4)
    arm = (4/suma)
    print (arm)

elif (num == 5):
    print ("Haz seleccionado 5")
    x = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x3 = input ("Ingresa el tercer numero\n>")
    x4 = input ("Ingresa el cuarto numero\n>")
    x5 = input ("Ingresa el quinto numero\n>")
    x_ = float (x)
    x_2 = float (x2)
    x_3 = float (x3)
    x_4 = float (x4)
    x_5 = float (x5)
    suma = (1/x_ + 1/x_2 + 1/x_3 + 1/x_4 + 1/x_5)
    arm = (5/suma)

elif (num == 6):
    print ("Haz seleccionado 6")
    x = input ("Ingresa el primer numero\n>")
    x2 = input ("Ingresa el segundo numero\n>")
    x3 = input ("Ingresa el tercer numero\n>")
    x4 = input ("Ingresa el cuarto numero\n>")
    x5 = input ("Ingresa el quinto numero\n>")
    x6 = input ("Ingresa el sexto numero\n>")
    x_ = float (x)
    x_2 = float (x2)
    x_3 = float (x3)
    x_4 = float (x4)
    x_5 = float (x5)
    x_6 = float (x6)
    suma = (1/x_ + 1/x_2 + 1/x_3 + 1/x_4 + 1/x_5 + 1/x_6)
    arm = (6/suma)
    print (arm)


else:
    print ("Caracter no valido")


	


