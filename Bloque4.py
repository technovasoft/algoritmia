print ("Sesgo o Skewness\n")

print ("Medida estadística que describe la simetría de la distribución alrededor de un promedio, esto es, el sesgo refleja el grado de simetría respecto a la media aritmética.\n")

print ("1.Si el sesgo es igual a cero, la distribucion es simetrica.\n")

print ("2. Si el sesgo es positivo la distribucion tendra una cola asimetrica extendida hacia los valores positivos.\n")

print ("3. Si el sesgo es negativo indica una distribucion con una cola asimetrica extendida hacia los valores negativos.\n")

print ("Su formula es:   N/(N-1)(N-2)*(X1 - X)3 + (X2 - X)3 +...(Xn - X)3/σ, Siempre y cuando N>2\n")

print ("Para sacar σ (desviación estandar) se necesita:\n")
print ("Sacar la varianza")
print ("1.Calcular la media (Promedio)")
print ("2.Por cada numero restar la media y elevar el resultado al cuadrado (La diferencia elevado al cuadrado")
print ("3.Ahora calcular la media de esas diferencias al cuadrado")
print ("4. La desviacion estandar es la raiz cuadrada de la varianza\n")

print ("Ingresa 6 numeros para sacar la varianza")

x1 = input("Ingresa el primer numero\n>")
x2 = input("Ingresa el segundo numero\n>")
x3 = input("Ingresa el tercer nummero\n>")
x4 = input("Ingresa el cuarto numero\n>")
x5 = input("Ingresa el quinto numero\n>")
x6 = input("Ingresa el sexto numero\n>")

x_1 = float(x1)
x_2 = float(x2)
x_3 = float(x3)
x_4 = float(x4)
x_5 = float(x5)
x_6 = float(x6)

suma = (x_1 + x_2 + x_3 + x_4 + x_5 + x_6)
media = (suma/6)

xr1 = (x_1 - media)
xr2 = (x_2 - media)
xr3 = (x_3 - media)
xr4 = (x_4 - media)
xr5 = (x_5 - media)
xr6 = (x_6 - media)

print ("Suma: ",suma)
print ("1.Promedio: ",media)

xd1 = (xr1 ** 2)
xd2 = (xr2 ** 2)
xd3 = (xr3 ** 2)
xd4 = (xr4 ** 2)
xd5 = (xr5 ** 2)
xd6 = (xr6 ** 2)

suma2 = (xd1 + xd2 + xd3 + xd4 + xd5 + xd6)
varianza = (suma2/5)
dev_est = (varianza ** (1/2))

print ("Varianza : ",varianza)
print ("Desviación Estándar: ",dev_est,"\n")

print ("Ya teniendo el valor de la desviación estandar")
n = input("Ingresa el valor de N del 1 al 6\n>")
num = int(n)

if (num == 1):
    print ("Ingresaste 1\nLa operacion no puede ser completada ya que para seguir se necesita que N>=2")

elif (num == 2):
    print ("Ingresaste 2")
    sesgo = (num/((num-1)*(num-2))*((xr1 ** 3)+(xr2 ** 3))/(dev_est ** 3))
    print ("El sesgo es: ",sesgo)

elif (num == 3):
    print ("Ingresaste 3")
    sesgo = (num/((num-1)*(num-2))*((xr1 ** 3)+(xr2 ** 3)+(xr3 ** 3))/(dev_est ** 3))
    print ("El sesgo es: ",sesgo)

elif (num == 4):
    print ("Ingresaste 4")
    sesgo = (num/((num-1)*(num-2))*((xr1 ** 3)+(xr2 ** 3)+(xr3 ** 3)+(xr4 ** 3))/(dev_est ** 3))
    print ("El sesgo es: ",sesgo)

elif (num == 5):
    print ("Ingresaste 5")
    sesgo = (num/((num-1)*(num-2))*((xr1 ** 3)+(xr2 ** 3)+(xr3 ** 3)+(xr4 ** 3)+(xr5 ** 3))/(dev_est ** 3))
    print ("El sesgo es: ",sesgo)

elif (num == 6):
    print ("Ingresaste 6")
    sesgo = (num/((num-1)*(num-2))*((xr1 ** 3)+(xr2 ** 3)+(xr3 ** 3)+(xr4 ** 3)+(xr5 ** 3)+(xr6 ** 3))/(dev_est ** 3))
    print ("El sesgo es: ",sesgo)
             
if (sesgo == 0):
    print ("La distribucion es simetrica")
elif (sesgo > 0):
    print ("El sesgo tiene una cola asimetrica extendida hacia los valores positivos.")
elif (sesgo < 0):
    print ("El sesgo tiene una cola asimetrica extendida hacia los valores negativos.")
    
#-----------------------------------------------------------------------------------------------------------------------------
print ("Apuntamiento o Curtosis\n")

print ("Es una medida estadistica que describe el apuntamiento o achatamiento de una cierta distribucion con respecto a una distribucion normal.\n")

print ("1.La curtosis positiva indica una distribucion relativamente apuntada.\n")

print ("2.La negativa indica una distribucion relativamente achatada\n")

print ("3. En una distribucion normal, la curtosis es igual a 3, a los valores mayores de 3 se los llama curtosis excesiva.\n")

print ("Su formula es:   (N(N+1)/(N-1)(N-2)(N-3)*(X1 - X)4 + (X2 - X)4 +...(Xn - X)4/σ4)-3(N-1)2/(N-2)(N-3), Siempre y cuando N>3\n")

print ("Para sacar σ (desviación estandar) se necesita:\n")
print ("Sacar la varianza")
print ("1.Calcular la media (Promedio)")
print ("2.Por cada numero restar la media y elevar el resultado al cuadrado (La diferencia elevado al cuadrado")
print ("3.Ahora calcular la media de esas diferencias al cuadrado")
print ("4. La desviacion estandar es la raiz cuadrada de la varianza\n")

print ("Ingresa 6 numeros para sacar la varianza")

x1 = input("Ingresa el primer numero\n>")
x2 = input("Ingresa el segundo numero\n>")
x3 = input("Ingresa el tercer nummero\n>")
x4 = input("Ingresa el cuarto numero\n>")
x5 = input("Ingresa el quinto numero\n>")
x6 = input("Ingresa el sexto numero\n>")

x_1 = float(x1)
x_2 = float(x2)
x_3 = float(x3)
x_4 = float(x4)
x_5 = float(x5)
x_6 = float(x6)

suma = (x_1 + x_2 + x_3 + x_4 + x_5 + x_6)
media = (suma/6)

xr1 = (x_1 - media)
xr2 = (x_2 - media)
xr3 = (x_3 - media)
xr4 = (x_4 - media)
xr5 = (x_5 - media)
xr6 = (x_6 - media)

print ("Suma: ",suma)
print ("Promedio: ",media)

xd1 = (xr1 ** 2)
xd2 = (xr2 ** 2)
xd3 = (xr3 ** 2)
xd4 = (xr4 ** 2)
xd5 = (xr5 ** 2)
xd6 = (xr6 ** 2)

suma2 = (xd1 + xd2 + xd3 + xd4 + xd5 + xd6)
varianza = (suma2/5)
dev_est = (varianza ** (1/2))

print ("Varianza : ",varianza)
print ("Desviación Estándar: ",dev_est,"\n")

print ("Ya teniendo el valor de la desviación estandar")
n = input("Ingresa el valor de N del 1 al 6\n>")
num = int(n)

if (num == 1):
    print ("Ingresaste 1\nLa operacion no puede ser completada ya que para seguir se necesita que N>=3")

elif (num == 2):
    print ("Ingresaste 2\nLa operacion no puede ser completada ya que para seguir necesira que N>=3")

elif (num == 3):
    print ("Ingresaste 3")
    curtosis = (num*(num+1)/((num-1)*(num-2)*(num-3)))*((xr1 ** 4)+(xr2 ** 4)+(xr3 ** 4))/(dev_est ** 4)-((3*(num-1) ** 2)/((num-2)*(num-3)))
    print ("La curtosis es: ",curtosis)

elif (num == 4):
    print ("Ingresaste 4")
    curtosis = (num*(num+1)/((num-1)*(num-2)*(num-3)))*((xr1 ** 4)+(xr2 ** 4)+(xr3 ** 4)+(xr4 ** 4))/(dev_est ** 4)-((3*(num-1) ** 2)/((num-2)*(num-3)))
    print ("La curtosis es: ",curtosis)

elif (num == 5):
    print ("Ingresaste 5")
    curtosis = (num*(num+1)/((num-1)*(num-2)*(num-3)))*((xr1 ** 4)+(xr2 ** 4)+(xr3 ** 4)+(xr4 ** 4)+(xr5 ** 4))/(dev_est ** 4)-((3*(num-1) ** 2)/((num-2)*(num-3)))
    print ("La curtosis es: ",curtosis)

elif (num == 6):
    print ("Ingresaste 6")
    curtosis = (num*(num+1)/((num-1)*(num-2)*(num-3)))*((xr1 ** 4)+(xr2 ** 4)+(xr3 ** 4)+(xr4 ** 4)+(xr5 ** 4)+(xr6 ** 4))/(dev_est ** 4)-((3*(num-1) ** 2)/((num-2)*(num-3)))
    print ("La curtosis es: ",curtosis)
    
             
if (curtosis > 0):
    print ("La curtosis positiva es relativamente apuntada.")
elif (curtosis < 0):
    print ("La curtosis negativa es relativamente achatada.")
