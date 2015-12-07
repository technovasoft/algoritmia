
n = int(input("Dame P( A y B )"))
m = int(input("Dame P( B )"))
f=n/m
print("P(A|B): ",f)

#------------------------------------------------------------------------
import math as mt
m = float(input("Dame tamaño de la poblacion"))
z = float(input("Dame nivel de confiabilidad"))
p = float(input("Dame probabilidad de exito"))
q = float(input("Dame probabilidad de fracaso"))
e = float(input("Dame error de muestreo"))
arr=((mt.pow(z,2)*m)*(p*q))
down=(mt.pow(e,2)*(m-1))+(mt.pow(z,2)*(p*q))

n=arr/down
print("Tamaño de la muestra: ",n)
