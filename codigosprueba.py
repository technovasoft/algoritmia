import numpy as np
h=int(input("cuantos filas son: "))
g=int(input("cuantos columnas son: "))

matriz=[]
for x in range(h):
    matriz.append([0]*g)
p=h*g
ordenada=[0]*p

for i in range(h):
    for j in range(g):
        matriz[i][j]=input("dato:")

c=0     
for i in range(h):
    for j in range(g):
        ordenada[c]=matriz[i][j]
        c=c+1
def bubblesort(lst):
    "Sorts lst in place and returns it."
    for passesLeft in range(len(lst)-1, 0, -1):
     for index in range(passesLeft):
         if lst[index] > lst[index + 1]:
            lst[index], lst[index + 1] = lst[index + 1], lst[index]
    return lst

print("Datos Desordenados")  
print(matriz)

bubblesort(ordenada)

c=0
for i in range(h):
    for j in range(g):
        matriz[i][j]=ordenada[c]
        c=c+1
print("Datos Ordenados") 
print(matriz)

#g=columnas
#clase=numero de clases
#marcaClase=el promedio de las clases
clase=int(input("cuantas clases crearas:"))

mclas=[]
for x in range(clase):
    mclas.append([0]*2)

for i in range(clase):
    print("Clase",i+1)
    for j in range(2):
        mclas[i][j]=int(input(":"))

for i in range(clase):
    de=mclas[i][0]
    a=mclas[i][1]
    
marc=[0]*clase

#marca declase
for x in range(clase)
    marc[x]=((mclas[x][0]+mclas[x][1])/2)


#observaciones
i=0
cuantos=[0]*clase
for x in range(h)
    for y in range(g)
        i
        if matriz[x][y] >= mclas[i][0] and matriz[x][y]<= maclas[i][1]
            cuantos[i]+=1    







        
