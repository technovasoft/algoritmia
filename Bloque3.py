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

