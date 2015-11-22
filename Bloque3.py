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
def RangoDA():
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
          matriz[i][j]=float(input("dato:"))
  
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
          mclas[i][j]=float(input(":"))
  
  for i in range(clase):
      de=mclas[i][0]
      a=mclas[i][1]
      
  marc=[0]*clase
  
  #marca declase
  for x in range(clase):
      marc[x]=((mclas[x][0]+mclas[x][1])/2)
  
  
  #observaciones
  i=0
  cuantos=[0]*clase
  for i in range(clase):
      for x in range(h):
          for y in range(g):
              
              if matriz[x][y] >= mclas[i][0] and matriz[x][y]<= mclas[i][1]:
                  cuantos[i]+=1    
      i+1
  print(cuantos)
  
  #tabla
  print("\tTabla de Distribucion de Frecuencias")
  print("Tamaño de clase\t\t Marca clase\tobservaciones")
  
  for i in range(clase):
      print("De",mclas[i][0],"a",mclas[i][1],"\t\t",marc[i],"\t\t",cuantos[i])
          
          

#------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------
def MediaDA():
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
          matriz[i][j]=float(input("dato:"))
  
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
          mclas[i][j]=float(input(":"))
  
  for i in range(clase):
      de=mclas[i][0]
      a=mclas[i][1]
      
  marc=[0]*clase
  
  #marca declase
  for x in range(clase):
      marc[x]=((mclas[x][0]+mclas[x][1])/2)
  
  
  #observaciones
  i=0
  cuantos=[0]*clase
  for i in range(clase):
      for x in range(h):
          for y in range(g):
              
              if matriz[x][y] >= mclas[i][0] and matriz[x][y]<= mclas[i][1]:
                  cuantos[i]+=1    
      i+1
  
  #Media Aritmetica
  
  ma=0
  suma=0
  n=0
  for i in range(clase):
      suma+=(marc[i]*cuantos[i])
      n+=cuantos[i]
      
  ma=(suma/n)
  
  print("La media de datos agrupados es:",ma)
  
#----------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

def DesviacionMDA():
 import numpy as np
 import math as mt
 h=int(input("cuantos filas son: "))
 g=int(input("cuantos columnas son: "))
 
 matriz=[]
 for x in range(h):
     matriz.append([0]*g)
 p=h*g
 ordenada=[0]*p
 
 for i in range(h):
     for j in range(g):
         matriz[i][j]=float(input("dato:"))
 
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
         mclas[i][j]=float(input(":"))
 
 for i in range(clase):
     de=mclas[i][0]
     a=mclas[i][1]
     
 marc=[0]*clase
 
 #marca declase
 for x in range(clase):
     marc[x]=((mclas[x][0]+mclas[x][1])/2)
 
 
 #observaciones
 i=0
 cuantos=[0]*clase
 for i in range(clase):
     for x in range(h):
         for y in range(g):
             
             if matriz[x][y] >= mclas[i][0] and matriz[x][y]<= mclas[i][1]:
                 cuantos[i]+=1    
     i+1
 
 #Media Aritmetica
 
 ma=0
 suma=0
 n=0
 for i in range(clase):
     suma+=(marc[i]*cuantos[i])
     n+=cuantos[i]
     
 ma=(suma/n)
 
 #Desviacion Media
 Dm=0
 su=0
 j=ma
 for x in range(len(marc)):
     su+=(mt.fabs(marc[x]-j))
     
 Dm=(su/n)
 print("La desviacion media de datos agrupados es:",Dm)


#--------------------------------------------------------------------------------
#--------------------------------------------------------------------------------

def DesviacionEstdDA():
 import numpy as np
 import math as mt
 h=int(input("cuantos filas son: "))
 g=int(input("cuantos columnas son: "))
 
 matriz=[]
 for x in range(h):
     matriz.append([0]*g)
 p=h*g
 ordenada=[0]*p
 
 for i in range(h):
     for j in range(g):
         matriz[i][j]=float(input("dato:"))
 
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
         mclas[i][j]=float(input(":"))
 
 for i in range(clase):
     de=mclas[i][0]
     a=mclas[i][1]
     
 marc=[0]*clase
 
 #marca declase
 for x in range(clase):
     marc[x]=((mclas[x][0]+mclas[x][1])/2)
 
 
 #observaciones
 i=0
 cuantos=[0]*clase
 for i in range(clase):
     for x in range(h):
         for y in range(g):
             
             if matriz[x][y] >= mclas[i][0] and matriz[x][y]<= mclas[i][1]:
                 cuantos[i]+=1    
     i+1
 
 #Media Aritmetica
 
 ma=0
 suma=0
 n=0
 for i in range(clase):
     suma+=(marc[i]*cuantos[i])
     n+=cuantos[i]
     
 ma=(suma/n)
 
 su=0
 j=ma
 
 
 #Desviacion Estandar
 De=0
 
 for x in range(len(marc)):
     su+=(mt.pow(marc[x]-j,2))
     
 De=(mt.sqrt(su/n-1))
 print("La desviacion Estandar es:",De)

#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------

def VarianzaDA():
 import numpy as np
 import math as mt
 h=int(input("cuantos filas son: "))
 g=int(input("cuantos columnas son: "))
 
 matriz=[]
 for x in range(h):
     matriz.append([0]*g)
 p=h*g
 ordenada=[0]*p
 
 for i in range(h):
     for j in range(g):
         matriz[i][j]=float(input("dato:"))
 
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
         mclas[i][j]=float(input(":"))
 
 for i in range(clase):
     de=mclas[i][0]
     a=mclas[i][1]
     
 marc=[0]*clase
 
 #marca declase
 for x in range(clase):
     marc[x]=((mclas[x][0]+mclas[x][1])/2)
 
 
 #observaciones
 i=0
 cuantos=[0]*clase
 for i in range(clase):
     for x in range(h):
         for y in range(g):
             
             if matriz[x][y] >= mclas[i][0] and matriz[x][y]<= mclas[i][1]:
                 cuantos[i]+=1    
     i+1
 
 #Media Aritmetica
 
 ma=0
 suma=0
 n=0
 for i in range(clase):
     suma+=(marc[i]*cuantos[i])
     n+=cuantos[i]
     
 ma=(suma/n)
 
 su=0
 j=ma
 
 #Varianza de datos ordenados
 
 for x in range(len(marc)):
     su+=(mt.pow(marc[x]-j,2)*cuantos[x])
     
 Va=(su/n)
 print("La Varianza de datos agrupados es:",Va)




