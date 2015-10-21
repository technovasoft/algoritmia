print("BLOQUE 1")
print ("CONCEPTOS GENERALES\n")
print ("         EJERCICIOS DE REPRESENTACION E\nINTERPRETACION DE GRAFICAS PARA DATOS NO AGRUPADOS\n") 
print ("Hola :D")
#######ALGORITMO
print ("Ingresa el nombre de los equipos y los campeonatos ganados a continuacion:")
n1 = input ("Primer equipo: \n>>> ")
c1 = input ("campeonatos Primer equipo: \n>>> ")
n2 = input ("Segundo equipo: \n>>> ")
c2 = input ("campeonatos Segundo equipo: \n>>> ")
n3 = input ("Tercer equipo: \n>>> ")
c3 = input ("campeonatos Tercer equipo: \n>>> ")
n4 = input ("Cuarto equipo: \n>>> ")
c4 = input ("campeonatos Cuarto equipo: \n>>> ")
n5 = input ("Quinto equipo: \n>>> ")
c5 = input ("campeonatos Quinto equipo: \n>>> ")
n6 = input ("Sexto equipo: \n>>> ")
c6 = input ("campeonatos Sexto equipo: \n>>> ")

c_1 = int(c1)
c_2 = int(c2)
c_3 = int(c3)
c_4 = int(c4)
c_5 = int(c5)
c_6 = int(c6)

print ("| Equipo: \t Campeonatos ganados \t|")
print ("|",n1,"\t\t",       c_1, "\t\t|")
print ("|",n2,"\t\t",       c_2, "\t\t|")
print ("|",n3,"\t\t",       c_3, "\t\t|")
print ("|",n4,"\t\t",       c_4, "\t\t|")
print ("|",n5,"\t\t",       c_5, "\t\t|")
print ("|",n6,"\t\t",       c_6, "\t\t|")

suma = (c_1 + c_2 + c_3 + c_4 + c_5 + c_6)
print ("\nSuma total de todos los campeonatos: \n>>",suma)

#####Calcular porcentajes
porce = (c_1 * 100 / suma)
porce2 = round(porce,2 ) #Round sirve para redondear una cantidad que se imprime y ",2" sirve para solo imprimir dos decimales.
print ("\nPorcentaje del Primer equipo:\t",porce2,"%")

porce = (c_2 * 100 / suma)
porce2 = round(porce,2 )
print ("Porcentaje del Segundo equipo:\t",porce2,"%")

porce = (c_3 * 100 / suma)
porce2 = round(porce,2 )
print ("Porcentaje del Tercer equipo:\t",porce2,"%")

porce = (c_4 * 100 / suma)
porce2 = round(porce,2 )
print ("Porcentaje del Cuarto equipo:\t",porce2,"%")

porce = (c_5 * 100 / suma)
porce2 = round(porce,2 )
print ("Porcentaje del Quinto equipo:\t",porce2,"%")

porce = (c_6 * 100 / suma)
porce2 = round(porce,2 )
print ("Porcentaje del Sexto equipo:\t",porce2,"%")

print ("total:\t\t\t\t 100%")
#####Con los porcentajes obtenidos se pueden realizar las graficas circulares, todo depende de los datos que el usuario ingrese
