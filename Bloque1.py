def DatosOrdenados():
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
	        matriz[i][j]=int(input("dato:"))
	
	c=0     
	for i in range(h):
	    for j in range(g):
	        ordenada[c]=matriz[i][j]
	        c=c+1
	def bubblesort( A ):
	  for i in range( len( A ) ):
	    for k in range( len( A ) - 1, i, -1 ):
	      if ( A[k] < A[k - 1] ):
	        swap( A, k, k - 1 )
	 
	def swap( A, x, y ):
	  tmp = A[x]
	  A[x] = A[y]
	  A[y] = tmp
	
	print("Matriz")  
	print(matriz)
	
	bubblesort(ordenada)
	
	c=0
	for i in range(h):
	    for j in range(g):
	        matriz[i][j]=ordenada[c]
	        c=c+1
	print("Matriz Ordenada") 
	print(matriz)





#--------------------------------------------------------------------------------------------------

def DistribucionF():
	
	items=int(input("Dame le numero de items a ingresar"))
	datos=[0]*items
	tem_list=[]
	frecuencia=[0]*items
	suma=0

	i=0
	print("ingresa Los datos y la Frecuencia:")
	while i<items:
		tem_list.append(input("Dato: "))
		frecuencia[i]=int(input("Frecuencia: "))
		i+=1

	i=0
	
	for x in range(0,len(frecuencia)):
		suma+=frecuencia[i]
		i+=1

	print("\tTabla de Frecuencia\n Dato\t\tFrecuencia\tPorcentaje")
	i=0
	while i<items:
		porcentaje=((frecuencia[i]*100)/suma)
		
		print(tem_list[i],"\t\t",frecuencia[i],"\t\t",porcentaje,"%")

		i+=1
	print("Total","\t\t",suma,"\t\t","100%")
		
		
#-------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------
def GraficaPastel():
	import matplotlib.pyplot as plt
	import numpy as np
	
	datos=int(input("Cuantos datos ingresaras: "))
	impr=[0]*datos
	vol=[0]*datos
	expl=[0]*datos
	
	for x in range(0,datos):
		impr[x]=(input("Nombre: "))
		vol[x]=(int(input("Numero: ")))
	
	mayor=0
	for x in range(0,datos):
		if vol[x] > mayor:
			mayor = vol[x]
	
	for x in range(0,datos):
		if vol[x] == mayor:
			expl[x] = 0.05
	
	
	
	plt.pie(vol, explode=expl, labels=impr, autopct='%1.1f%%', shadow=True)
	plt.title("Pastel", bbox={"facecolor":"0.8", "pad":5})
	plt.legend()
	plt.show()
	
#---------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------
def GraficaBarra():
	import numpy as np
	import matplotlib.pyplot as plt
	
	
	grupos={"pene","jesus","gonorrea","penes","hitler"}
	
	datos = [[1, 2, 3, 4,5], [3, 5, 3, 5,6]]
	X = np.arange(5)
	plt.bar(X + 0.00, datos[0], color = "b", width = 0.25)
	plt.bar(X + 0.25, datos[1], color = "g", width = 0.25)
	
	plt.xticks(X+0.38, ["A","B","C","D","E"])
	
	plt.show()


#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
def PrototipoHistograma():
		"""
	Demo of the histogram (hist) function with a few features.
	
	In addition to the basic histogram, this demo shows a few optional features:
	
	    * Setting the number of data bins
	    * The ``normed`` flag, which normalizes bin heights so that the integral of
	      the histogram is 1. The resulting histogram is a probability density.
	    * Setting the face color of the bars
	    * Setting the opacity (alpha value).
	
	"""
	import numpy as np
	import matplotlib.mlab as mlab
	import matplotlib.pyplot as plt
	
	
	# example data
	mu = 100  # mean of distribution
	sigma = 15  # standard deviation of distribution
	x = mu + sigma * np.random.randn(10000)
	
	num_bins = 50
	# the histogram of the data
	n, bins, patches = plt.hist(x, num_bins, normed=1, facecolor='green', alpha=0.5)
	# add a 'best fit' line
	y = mlab.normpdf(bins, mu, sigma)
	plt.plot(bins, y, 'r--')
	plt.xlabel('Smarts')
	plt.ylabel('Probability')
	plt.title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
	
	# Tweak spacing to prevent clipping of ylabel
	plt.subplots_adjust(left=0.15)
	plt.show()

#para hacer los algoritmos que faltan utilizaremos este pedo?
#necesito que alguien de grafico lo revise y me diga 
#http://unamatematicaseltigre.blogspot.mx/2014/05/tecnicas-de-visualizacion-de-datos-ser.html














