#-------------------7.1----------------------------------------------

x = int(input("cuantos datos ingresaras:"))
datos=[0]*x
suma = 0
for i in range(x):
	datos[i] = int(input("Dato: "))
	suma+=datos[i]

print("Tienes ",suma," Opciones")

#------------------------------------------------------------------
#-------------------------7.3--------------------------------------
x = int(input("Cuantos datos ingresaras: "))
multi = 1

for i in range(x):
	multi*=int(input("Datos: ")
		
print("Tienes ",multi," Opciones")

#------------------------------------------------------------------
#------------------------------7.4---------------------------------
import math as mt
r = int(input("Dame r: "))
n = int(input("Dame n: "))
b = mt.factorial(r)*mt.factorial(n-r)
c = (mt.factorial(n)/ b)
print("El numero de Combinaciones es: ",c)

#------------------------------------------------------------------
#--------------------7.5-------------------------------------------
