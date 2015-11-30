import math

print ("P= ((n!/r!(n-r)!)(p)^r*(q)^n-r)")

print("n = Población o número de ensayos")
print("r = número de exito buscado")
print("p = probabilidad de exito")
print("q = probabilidad de fracaso")

print ("Ingresa el valor de n")
n1 = float(input())
n = (math.factorial(n1))

print ("Ingresa el valor de r")
r1 = float(input())
r = (math.factorial(r1))

print ("Ingresa el valor de p")
p = float(input())

print ("Ingresa el valor de q")
q = float(input())

rn = int(n1-r1)
print(rn)

nr = (math.factorial(rn))

bi = ((n/(r*nr))*(p**r)*(q**rn))
print (bi*100,"%")
