#-------------------7.1----------------------------------------------

x = int(input("cuantos datos ingresaras:"))
datos=[0]*x
suma = 0
for i in range(x):
	datos[i] = int(input("Dato: "))
	suma+=datos[i]

print("Tienes ",suma," Opciones")

#------------------------------------------------------------------
