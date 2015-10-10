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
