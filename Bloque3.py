def rangoDatosNA():
  ##rango para datos no agrupados
d=int(input("Cuantos datos ingresaras: "))
datos=[0]*d

for x in range(0,d):
    datos[x]=int(input("dato: "))

mayor=0
menor=999999999999
for x in range(0,d):
    if datos[x] > mayor:
        mayor=datos[x]
    if datos[x] < menor:
        menor=datos[x]

rango = mayor - menor
print("EL RANGO")
print("De este grupo de datos es:",rango)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#Desciacion media para datos no agrupados
def ValorAbsoluto(X):
    if X < 0:
        return X * -1
    elif X > 0:
        return X
    else:
        return 0
    
d=int(input("cuantos datos entraran: "))
datos=[0]*d
for x in range(0,d):
    datos[x]=int(input("dato:"))

j=np.mean(datos)
suma=0

for x in range(0,d):
    i=datos[x]
    suma+=ValorAbsoluto(i-j)


desviacion=suma/d

print("La desviacion es:",desviacion)



#--------------------------------------------------------------------
#--------------------------------------------------------------------
