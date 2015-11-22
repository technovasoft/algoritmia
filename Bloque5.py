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
#sigue en beta este codigo
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt # importando matplotlib
import seaborn as sns # importando seaborn
import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd # importando pandas

# Creando un DataFrame de pandas.
df = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/datasets/longley.csv', index_col=0)
df.head() # longley dataset

# utilizando la api de formula de statsmodels
est = smf.ols(formula='Employed ~ GNP', data=df).fit()
est.summary() # Employed se estima en base a GNP.



# grafico de regresion. que tanto se ajusta el modelo a los datos.
y = df.Employed  # Respuesta
X = df.GNP  # Predictor
X = sm.add_constant(X) # agrega constante

X_1 = pd.DataFrame({'GNP': np.linspace(X.GNP.min(), X.GNP.max(), 100)})
X_1 = sm.add_constant(X_1) 

y_reg = est.predict(X_1) # estimacion

plt.scatter(X.GNP, y, alpha=0.3)  # grafica los puntos de datos
plt.ylim(30, 100)  # limite de eje y
plt.xlabel("Producto bruto") # leyenda eje x
plt.ylabel("Empleo") # leyenda eje y
plt.title("Ajuste de regresion") # titulo del grafico
reg = plt.plot(X_1.GNP, y_reg, 'r', alpha=0.9)  # linea de regresion

plt.show()

#----------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------
