print ("Media aritmetica:")

#Se entiende por media aritmetica al promedio en una serie de datos, esto es, la suma de todos los datos entre el numero totaal de datos.

#Ejemplo del libro

print ("Un estudiante obtuvo las siguientes calificaciones durante el semestre pasado:")

#Perdon por no usar for xD

materia1 = input("Ingresa la primera materia\n>")
materia2 = input("Ingresa la segunda materia\n>")
materia3 = input("Ingresa la tercer materia\n>")
materia4 = input("Ingresa la cuarta materia\n>")
materia5 = input("Ingresa la quinta materia\n>")
materia6 = input("Ingresa la sexta materia\n>")

print ("Ingresa la calificacion de cada materia")

calif1 = input("ingresa la primera calificacion\n>")
calif2 = input("ingresa la segunda calificacion\n>")
calif3 = input("ingresa la tercer calificacion\n>")
calif4 = input("ingresa la cuarta calificacion\n>")
calif5 = input("ingresa la quinta calificacion\n>")
calif6 = input("ingresa la sexta calificacion\n>")

califi1 = int(calif1)
califi2 = int(calif2)
califi3 = int(calif3)
califi4 = int(calif4)
califi5 = int(calif5)
califi6 = int(calif6)

suma = (califi1 + califi2 + califi3 + califi4 + califi5 + califi6)
prom = (suma/6)

print ("Materia \t\t Calficacion")
print (materia1, "\t\t\t", califi1)
print (materia2, "\t\t\t", califi2)
print (materia3, "\t\t\t", califi3)
print (materia4, "\t\t\t", califi4)
print (materia5, "\t\t\t", califi5)
print (materia6, "\t\t\t", califi6)
print ("Suma\t\t\t", suma)
print ("Promedio\t\t", prom)



#--------------------------------------------------------------------------------------------

#Mediana 
print ("Mediana")
print ("Corresponde al número intermedio después de ordenar los datos en forma ascendente o descendente.\n")
print ("Ingresa 5 numeros los cuales deseas ordenar")
n1 = input("Ingresa el primer numero\n>")
n2 = input("Ingresa el segundo numero\n>")
n3 = input("Ingresa el tercer numero\n>")
n4 = input("Ingresa el cuarto numero\n>")
n5 = input("Ingresa el quinto numero\n>")

n1_1 = int(n1)
n2_2 = int(n2)
n3_3 = int(n3)
n4_4 = int(n4)
n5_5 = int(n5)
lista = [n1_1,n2_2,n3_3,n4_4,n5_5]
for recorrido in range(1,len(lista)):
  for posicion in range(len(lista) - recorrido):
      if lista[posicion] > lista[posicion + 1]:
          temp = lista[posicion]
          lista[posicion] = lista[posicion + 1]
          lista[posicion + 1] = temp
print ("La lista ordenada es:", lista)
print ("La mediana es:",lista[2])
