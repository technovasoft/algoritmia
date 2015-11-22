def RegresionLine():
  #Regresion lineal
  import numpy as np
  import math as mt
  import pandas as pd
  
  a=int(input("Cuantos datos ingresaras:"))
  
  x=[0]*a
  y=[0]*a
  
  print("Ingresa los datos del primer grupo:")
  
  for i in range(a):
      x[i]=float(input(":"))
  
  print("Ingresa los datos del segundo grupo:")
  
  for i in range(a):
      y[i]=float(input(":"))
  
  x2=[0]*a
  y2=[0]*a
  for j in range(a):
      x2[j]=mt.pow(x[j],2)
      y2[j]=mt.pow(y[j],2)
      
  xy=[0]*a
  for p in range(a):
      xy[p]=x[p]*y[p]
  
  print("X\t\tY\t\tX^2\t\tXY\t\tY^2")
  for k in range(a):
      print(x[k],"\t\t",y[k],"\t\t",x2[k],"\t\t",xy[k],"\t",y2[k])
      
  print("Suma de X\tSuma de Y\tSuma de X^2\tSuma de XY\tSuma de y^2")
  sx=0
  sy=0
  sx2=0
  sy2=0
  sxy=0
  for f in range(a):
      sx+=x[f]
      sy+=y[f]
      sx2+=x2[f]
      sy2+=y2[f]
      sxy+=xy[f]
  print(sx,"\t\t",sy,"\t\t",sx2,"\t\t",sxy,"\t",sy2)

#---------------------------------------------------------------------------------
#---------------------------------------------------------------------------------
