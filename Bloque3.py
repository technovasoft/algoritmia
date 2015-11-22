def rangoDatosNO():
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
def DesviacionMedia():
  import math as mt
  import numpy as np
  d=int(input("cuantos datos entraran: "))
  datos=[0]*d
  for x in range(0,d):
      datos[x]=int(input("dato:"))
  
  j=np.mean(datos)
  suma=0
  
  for x in range(0,d):
      i=datos[x]
      suma+=mt.fabs(i-j)
  
  
  desviacion=suma/d
  
  print("La desviacion es:",desviacion)



#--------------------------------------------------------------------
#--------------------------------------------------------------------

def DesviacionEstandar():
  ##DESVIACION ESTANDAR
  import numpy as np
  import math as mt
  
  ##raiz=mt.sqrt(numero)
  ##cuadrado=mt.pow(x,2)
  ##media=np.mean(arreglo)
  
  d=int(input("cuantos datos entraran: "))
  datos=[0]*d
  for x in range(0,d):
    datos[x]=int(input("dato:"))
  
  j=np.mean(datos)
  suma=0
  
  for x in range(0,d):
    i=datos[x]
    suma+=mt.pow(i-j,2)
  
  
  desviacion=mt.sqrt(suma/d-1)
  round(desviacion,2)
  print("La desviacion estandar es:",desviacion)

  
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
def Varianza():
  ##varianza para datos no agrupados
  
  import numpy as np
  import math as mt
  
  d=int(input("cuantos datos entraran: "))
  datos=[0]*d
  for x in range(0,d):
    datos[x]=int(input("dato:"))
  
  j=np.mean(datos)
  suma=0
  
  for x in range(0,d):
    i=datos[x]
    suma+=mt.pow(i-j,2)
  
  
  varianza=(suma/(d-1))
  
  print("La varianza es:",varianza)

#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
