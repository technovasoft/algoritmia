print ("BLOQUE 1")
print ("CONCEPTOS GENERALES\n")


###########ALGORITMO
print ("DISTRIBUCION DE FRECUENCIA")
print ("Problema 1.1 Los datos de la siguiente tabla muestran a los equipos con mas campeonatos de liga ganados en la Federacion Mexicana de Futbol hasta el año 2011\n")
print ("|   EQUIPO    |   CAMPEONATOS GANADOS\t|   PORCENTAJE   |")
print ("|  America    |            10 \t\t|       ------\t |")
print ("| Cruz Azul   |             8\t\t|       ------\t |")
print ("| Guadalajara |            11 \t\t|       ------\t |")
print ("|  Toluca     |            10 \t\t|       ------\t |") ##Tenemos un total de 46 campeonatos 
print ("|   UNAM      |             7\t\t|       ------\t |")
print ("|  TOTAL      |            46 \t\t|        100%\t |\n")

print ("*Calcula los porcentajes que corresponden a cada equipo conforme a la cantidad de campeonatos ganados\nPara calcular los porcentajes esta es la formula:\n")
print ("EJEMPLO:")
print ("| Cantidad de campeonatos          porcentaje \t|")
print ("|         46 --------------------->   100% \t|")
print ("|         10 --------------------->     x \t|\nSe multiplicara la cantidad de campeonatos ganados del equipo por 100 entre la cantidad TOTAL, osea la suma de todos los campeonatos ganados")
print ("10*100/46 = 21.74\n")

for rep in range (0,5):
    
    n1 = input("Ingresa la cantidad de campeonatos ganados:\n>>> ")
    n2 = input("Ingresa la cantidad total de campeonatos ganados:\n>>> ")
    n3 = float(n1)
    n4 = float(n2)
    operacion = (n3 * 100 / n4)
    operacion2 = round(operacion,2 ) #Round sirve para redondear una cantidad que se imprime y ",2" sirve para solo imprimir dos decimales.
    print (operacion2)
    
############TABLA CON LOS DATOS YA DEFINIDOS
print("\n")
print ("A continuacion se muestra como quedo la tabla luego de calcular los porcentajes\n")
print("La tabla queda de la siguiente manera")
print ("|   EQUIPO    |   CAMPEONATOS GANADOS\t|   PORCENTAJE   |")
print ("|  America    |            10 \t\t|       21.74%\t |")
print ("| Cruz Azul   |             8\t\t|       17.39%\t |")
print ("| Guadalajra  |            11 \t\t|       23.91%\t |")
print ("|  Toluca     |            10 \t\t|       21.74%\t |")
print ("|   UNAM      |             7\t\t|       15.22%\t |")
print ("|  TOTAL      |            46 \t\t|        100%\t |")

