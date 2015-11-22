def DatosOrdenados():

	h=int(input("cuantos filas son: "))
	g=int(input("cuantos columnas son: "))

	datos = [[0 for x in range(h)] for x in range(g)] 
	print("ingresa los datos: ")
	for x in range(0,h):
		for j in range(0,g):
           	s=h+1
            r=s+1
			datos[0][j]=int(input("fila",s,"columna",r," : ")

    
	print("matriz: ")
	for x in range(0,h):
		print(datos[h][g])
		for j in range(0,g):
			print(datos[h][g])


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


#para hacer los algoritmos que faltan utilizaremos este pedo?
#necesito que alguien de grafico lo revise y me diga 
#http://unamatematicaseltigre.blogspot.mx/2014/05/tecnicas-de-visualizacion-de-datos-ser.html














