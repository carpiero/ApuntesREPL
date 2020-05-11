print('hello world')
# variables
men = "si quieres No"
print(men)
# numero entero
a = 40
B = 2
z = a + B
print(z)
# calculos
suma = 39 + 3
resta = 15 - 13
multiplicacion = 12 * 2
division = 7 / 3
division_entera = 7 // 3
modulo = 15 % 6
expo = 2**4
print(suma)
print(resta)
print(multiplicacion)
print(division)
print(division_entera)
print(modulo)
print(expo)
# cadena de caracteres
cadena = "esto es una cadena de caracteres"
tipo_cadena = type(cadena)
print(tipo_cadena)
# numero entero
numero_entero = 18
tipo_numero_entero = type(numero_entero)
print(tipo_numero_entero)
# numero con decimales
num_decim = 56.98
tipo_num_decim = type(num_decim)
print(tipo_num_decim)
# lista
lista = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
tipo_lista = type(lista)
print(tipo_lista)
# Longitud
hechizo = "alojomoru"
print(len(hechizo))
print(hechizo[0])
print(hechizo[1])
print(hechizo[-4])
# Ejemplos de listas
numero = [3, 4, 5, 7, 4, 3, 1, 1]
ninjas = ["naruto", 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
mezcla = ['apple', 390, 876, 'orange', 'highway', 0.42, 87]
# Esto es una lista de listas que asignamos a la variable de nombre matriz
matriz = [[3, 4, 5], [1, 2, 3], [7, 3, 2]]
# Para seleccionar un elemento por su índice
print(ninjas[0])
print(ninjas[-1])
print(matriz[0])
# lista[start: stop: step]
print(ninjas[::2])
print(ninjas[1:-2])
print(ninjas[1:4])
print(ninjas[1::2])
# añadir un elemento nuevo al final de un lista
print(ninjas)
ninjas.append("kakashi")
print(ninjas[5])
# sumar listas
estudiantes = ['Harry', 'Hermione', 'Ron']
profesores = ['Dumbledore', 'Severus', 'Hagrid']
print(estudiantes)
print(profesores)
hogwards = estudiantes + profesores
print(hogwards)
# media de un conjunto de números
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
suma = sum(numeros)
longitud = len(numeros)
media = suma / longitud
print(media)
# mínimo y máximo
minimo = min(numeros)
maximo = max(numeros)
print(minimo)
print(maximo)
# Ordenación
numeros_ordenados = sorted(numeros)
print(numeros_ordenados)
# lista con valores repetidos
lista_peliculas_cine = ['alien', 'terminator 2', 'arma letal', 'alien', 'terminator 2']
print(lista_peliculas_cine)
opciones_peliculas = set(lista_peliculas_cine)
print(opciones_peliculas)
# diccionario de película y valoración dada
valoraciones = {'alien': 9.5, 'terminator': 8.9, 'arma letal': 7.3}
print(valoraciones)
# algunos métodos de diccionarios
print('lllllllllllllllllllllllllllllllllllllllllllllllllllll')
print(valoraciones['alien'])
print(valoraciones.keys())
print(valoraciones.values())
print(valoraciones.items())
# tipo booleanos
print(5 + 5 == 9)
print(5 + 5 == 10)
print(7 // 3 == 2)
print('isla' != 'isla')
print(100 < 100)
print(100 <= 100)
print(100 < 100)
# para ver si un elemento se encuentra en un conjunto o lista usaremos in
listezas = [1, 2, 3, 4, 5]
print(3 in [1, 2, 3, 4, 5])
print(7 not in [1, 2, 3, 4, 5])
#false
print('sadasdaddddddddddddddddddddddddddddddddddd')
hola=8
print((hola + 5 == 10) and (5 + 4 ==9 ))
print((100 < 180) and (100 > 90))
print((100 < 70) or (100 < 80))
print((93 < 5) or (7 not in [1, 2, 3, 4, 5]))
# Condicionales (if - elif - else)
entrada= int(input('Introduce el numero:'))
# convertimos la cadena de caracteres en entero. Esta operación se llama cast
numero_entrada= int(entrada)
print(numero_entrada)
print(numero_entrada < 20)
# Ahora veamos que has puesto
if numero_entrada == 42:
    print('has elegido el 42')
if numero_entrada >= 42:
    print('has elegido el', numero_entrada)
elif numero_entrada <= 42:
    print('el numero', numero_entrada, 'es menor que 42')
else:
    print('el nuero', numero_entrada, 'es mayor que 42')
#Bucles con Python
print('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu')
# Primer ejemplo: range
for numer in range(10):
    print(numer)
# Segundo ejemplo: range(start: stop: step)
for numere in range(5, 30, 3):
    print(numere)
# Tercer ejemplo
ninjas = ['Naruto', 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
for ninja in ninjas:
  print(ninja)
# Cuarto ejemplo
print('oooooooooooooooooooooooooooooooooppppppppppppppppppppppp')
valoraciones={'alien':9.5,'terminator':8.9,'arma letal':7.3}
print(valoraciones.keys())
for peli in valoraciones.keys():
  print('Pelicula:',peli)
for valoracion in valoraciones.values():
  # str(x) -> convierte x a tipo cadena de caracteres para 
	# poder encadenarla a "valoraciones:"
  print('valoraciones:' + str(valoracion))
for peli,puntuacion in valoraciones.items():
  print(peli,'tiene una puntuacion de',puntuacion)
print('888888888888888888888888888888888888888888888888888')
# Quinto ejemplo: cálculo de la suma
numeros = [34, 12, 93, 783, 330, 896, 1, 55]
total = 0
for numero in numeros:
  total+=numero
  print(total)
semm=sum(numeros)
print(semm)
# Sexto ejemplo
lista=[]
for x in range(2,6):
  numero=x**2
  lista.append(numero)
print(lista)
# Séptimo ejemplo: Bucle doble
valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
estudiantes = ['Harry', 'Hermione', 'Ron']
for estudiante in estudiantes:
  for peli,valoracion in valoraciones.items():
    print(estudiante, peli, valoracion)
# Indentación y errores
# Este código da error de indentación. print(x) debería estár más a la derecha
for x in range(10):
    print(x)
# Este código tiene doble indentación
valoraciones = {'Alien':9.5, 'Terminator 2':8.9, 'Arma Letal':7.3}
estudiantes = ['Harry', 'Hermione', 'Ron']
for estudiante in estudiantes: 
	# en este nivel estamos dentro del primer for
	print(">>> estamos dentro del primer for hablando de", estudiante)
	for peli, valoracion in valoraciones.items(): 
		# en este nivel estamos dentro del segundo for
		print(">>> estamos dentro del segundo for hablando de", peli, "y de", estudiante)
		print(estudiante, "vió", peli, "y le puso una nota de", valoracion)
# Para los más pro
# version newbie
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
# version pro
lst=[i for i in range(1,11) ]
print(lst)
# pares version newbie
lst2=[]
for e in lst:
  if e%2==0:
    lst2.append(e)
print(lst2)
# pares version pro
lst4=[e for e in lst if e%2==0]
print(lst4)
for o in range (2,11,2):
  print(o)
# impares version newbie
lst5=[]
for e in lst:
  if e%2>=1:
    lst5.append(e)
print(lst5)
#impares version pro
lst6=[x for x in lst if x%2>=1]
print(lst6)
# pares -> 0, impares -> 1​
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst)
# version newbie
lst6=[]
for e in lst:
  if e%2==0:
    lst6.append(0)
  else :
    lst6.append(1)
print(lst6)
# version pro
lst7=[0 if e%2==0 else 1 for e in lst]
print(lst7)
# pares -> 1, impares -> 0​

# version newbie
lst8=[]
for e in lst:
  if e%2==0:
    lst8.append(1)
  else:
    lst8.append(0)
print(lst8)
# version pro
lst9=[1 if e%2==0 else 0 for e in lst]
print(lst9)
#sumar todos los elementos
lst=[1,2,3,4,5,6,7,8,9,10] 
# version 1
suma=sum(lst)
print(suma)
# version 2
suma=0
for e in lst:
  suma+=e
print(suma)

# BUCLE WHILE')
print('whileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
i=1
while i<=3:
  print(i)
  i+=1
print('whileeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')

  
#######
#
#
#
numeros = [1, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7]
for e in numeros:
  if e>5:
    print(e)
numeroo=[e for e in numeros if e>5]
print(numeroo)
numerr=len(numeroo)
print(numerr)
#Muestra por pantalla una nueva lista que traduzca los elementos de la lista original:
# Los menores o iguales que 5 serán 0,
# Los mayores que 5 serán 1.
pruebalst=[0 if e<=5 else 1 for e in numeros]
print(pruebalst)
# otra prueba
lst3=[]
for r in numeros:
  if r<=5:
    lst3.append(0)
  elif r>=7:
    lst3.append(7)
  else :
    lst3.append(1)
print(lst3)
#DEFFFFFF
def resta(a, b):
  return a - b
fr=resta(30, 10)
print(fr)
# quitar de una lista
lst3.remove(0)
print(lst3)
# | uno u otro y & uno y otro
commute = 30
rain = True
traffic = True

if (rain == True) | (traffic == True):
    if (rain == True) & (traffic == True):
        total_commute = commute + 15 + 20
    elif (rain == True) & (traffic == False):
        total_commute = commute + 15
    elif (rain == False) & (traffic == True):
        total_commute = commute + 20
else:
    total_commute = commute

print("Your total commute time is expected to be", total_commute, "minutes.")
# Complete the square sum function so that it squares each number passed into it and then sums the results together. For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.
def square_sum(*a):
    return sum(x ** 2 for x in a)
fr=square_sum(1,2,2)    
print(fr)
def square_sum(*a):
    lst2=[]
    for e in a:
      lst2.append(e**2)
    suma=sum(lst2)
    return suma
fr=square_sum(1,2,2)
print(fr)
#holaasssssssssssssssssssssssssssssssssssssssssssssssssssss
print('DIVISOR DE NUMEROS')
dividendo=int(input('Escriba el dividendo:'))
divisor=int(input('Escriba el divisor:'))
cociente=dividendo//divisor
resto=dividendo%divisor
if resto>0:
  print('la division no es exacta','Cociente:',cociente,'Resto:',resto)
else:
  print('la division es exacta','Cociente:',cociente,'Resto:',resto)
numero = [3, 4, 5, 7, 4, 3, 1, 1]
ninjas = ["naruto", 'Sakura', 'Sasuke', 'Hinata', 'Shikamaru']
num= numero + ninjas
print(num)
print('NUEVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
lst=[u for u in range(0,10)]
print(lst)
lst2=[u for u in range (4,11)]
print(lst2)
lst2=[u for u in range(-6,0)]
print(lst2)
lst=[u for u in range(-56,-49)]
print(lst)
lst=[u for u in range (1,18,2)]
print(lst)
lst=[u for u in range(-6,11,2)]
print(lst)
lst=[u for u in range(100,1001,100)]
print(lst)
for u in  range (10,3,-1):
  print(u)
lst=[u for u in range (-50,-57,-1)]
print(lst)
lst=[u for u in range(17,0,-2)]
print(lst)
lst=[u for u in range(500,-1,-100)]
print(lst)
menor0=int(input('Escriba un número entero mayor que 0:'))
if menor0 <1:
  print('¡Le he pedido un número entero mayor que 0!')
else:
  gu=[l for l in range(menor0)]
  go=[l for l in range(menor0,-1,-1)]
  gur=gu+go
  print(gur)
print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
numeros = [1, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6, 7]
for e in numeros:
  if e>5:
    print(e)
numeroos=[e for e in numeros if e>5]
hola=len(numeroos)
print(hola)
numer=[0 if e>5 else 1 for e in numeros]
print(numer)
print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
num=[]
for e in numeros:
  if e>6:
    num.append(99)
  elif e>5:
    num.append(1)
  else :
    num.append(0)
print(num)
hh=set(num)
print(hh)
print('ooooooooooooooooooooooooooooooooooooooooooooooooooooooooo')
#PRUEBA TECNICA
lst=['buho','leon','camello','conejo','cabra']
lst3=[]
for e in lst:
  hola=len(e)
  if hola<5:
    lst3.append(e)
print(lst3)
# APUNTES IRONHACK dos variables
ages = {'Brian':23, 'Amy':22, 'Darlene':47, 'Ralph':32, 'Jordan':28, 'Stephanie':35}

for name, age in ages.items():
    print(name, "is", age, "years old.")
#LOOPS
new_list = []

for i in range(1, 11):
    square = i**2
    new_list.append(square)

print(new_list)
new=[x**2 for x in range(1,11)]
print(new)
# Manejo de archivos 
import os
os.getcwd()
root = 'C:'
level_1 = 'ironhack'
level_2 = 'module_0'
level_3 = 'python-beginner'
level_4 = 'data'

os.path.join(root, level_1, level_2, level_3, level_4)
folder_name = 'new_folder'

if os.path.exists(folder_name) == False:
    os.makedirs(folder_name)

print('ooo')
#EJERCICIO 1
well_height=125
daily_distance=30
nightly_distance=20
snail_position=0
advance_cm = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]
advancemaxmin =[]
days=0
for x in advance_cm:
  if snail_position<125:
    snail_position+=x-nightly_distance
    advancemaxmin.append(x-nightly_distance)
maximo=max(advancemaxmin)
minimo=min(advancemaxmin)
print(advancemaxmin)
minday=[]
for pos,item in enumerate(advancemaxmin):
  if item==minimo:
    minday.append(pos+1)
minday2=0
for x in minday:
  minday2=x
maxday=[]
for pos,item in enumerate(advancemaxmin):
  if item==maximo:
    maxday.append(pos+1)
maxday2=0
for x in maxday:
  maxday2=x
print(f'Maximum displacement fue el día {maxday2} con {maximo}cm')
print(f'Minimum displacement fue el día {minday2} con {minimo}cm')
average=sum(advancemaxmin)/len(advancemaxmin)
print(average)
import math
cuadrado=0
for r in advancemaxmin:
  cuadrado+=(r-average)**2
div=cuadrado/len(advancemaxmin)
standard_deviation=math.sqrt(div)
print(standard_deviation)
#EJERCICIO 2
gandalf = [10, 11, 13, 30, 22, 11, 10, 33, 22, 22]
saruman = [23, 66, 12, 43, 12, 10, 44, 23, 12, 17]
spells= [x-y for (x,y) in zip(gandalf,saruman)]
gandalf_wins=0
saruman_wins=0
tie=0
for g in spells:
  if g>0:
    gandalf_wins+=1
  elif g<0:
      saruman_wins+=1
  else:
    tie+=1
if gandalf_wins>saruman_wins:
  print('Gandalf wins')
elif gandalf_wins<saruman_wins:
  print('Saruman wins')
else:
  print('Tie')
# EJERCICIO 2 BONUS
POWER = {'Fireball': 50,'Lightning bolt': 40, 'Magic arrow': 10,'Black Tentacles': 25,'Contagion': 45}
gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 'Magic arrow', 'Lightning bolt', 'Fireball', 'Fireball', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles','Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']
gandalf_power=[]
saruman_power=[]
spells=[]
gandalf_wins=0
saruman_wins=0
tie=0
for x in gandalf:
  for j in POWER:
    if x==j:
      gandalf_power.append(POWER[x])
for x2 in saruman:
  for j2 in POWER:
    if x2==j2:
      saruman_power.append(POWER[x2])
spells=[u-v for (u,v)in zip(gandalf_power,saruman_power)]
print(spells)

for g in spells:
    if g>0 and saruman_wins<3:
        gandalf_wins+=1
        saruman_wins=0
    elif g<0 and gandalf_wins<3:
        gandalf_wins=0
        saruman_wins+=1
    else:
        gandalf_wins+=0
        saruman_wins+=0
print(gandalf_wins)
print(saruman_wins)

if gandalf_wins>=3:
    print('Gandalf wins')
elif saruman_wins>=3:
    print('Saruman wins')
else:
    print('Tie')

print(gandalf_power)
average_gandalf=sum(gandalf_power)/len(gandalf_power)
print(average_gandalf)
average_saruman=sum(saruman_power)/len(saruman_power)
print(average_saruman)
import math
numgan=0
for p in gandalf_power:
  numgan+=(p-average_gandalf)**2
vgan=numgan/len(gandalf_power)
stdvgan=math.sqrt(vgan)
print(stdvgan)
numsar=0
for p in saruman_power:
  numsar+=(p-average_saruman)**2
vsar=numsar/len(saruman_power)
stdvsar=math.sqrt(vsar)
print(stdvsar)
# EJERCICIO 3
# Variables
stops = [(10, 0), (4, 1), (3, 5), (3, 4), (5, 1), (1, 5), (5, 8), (4, 6), (2, 3)]
# Calculate the number of stops.
number_stops=len(stops)
print(number_stops)
# 2. Assign to a variable a list whose elements are the number of passengers at each stop (in-out).
# Each item depends on the previous item in the list + in - out.
n_passenger=[]
for j in stops:
  n_passenger.append(j[0]-j[1])
Total_passenger=[]
Total_passenger.append(n_passenger[0])
while len(Total_passenger)<=number_stops-1:
  Total_passenger.append(Total_passenger[len(Total_passenger)-1]+n_passenger[len(Total_passenger)])
print(Total_passenger)
# 3. Find the maximum occupation of the bus.
maximum_oc=max(Total_passenger)
print(maximum_oc)
# 4. Calculate the average occupation. And the standard deviation.
average_oc=sum(Total_passenger)/len(Total_passenger)
print(average_oc)
import math 
for n in Total_passenger:
  num=(n-average_oc)**2
div=len(Total_passenger)
stdev_oc=math.sqrt(num/div)
print(stdev_oc)
# EJERCICIO 4
# Robin Hood has hit the following points:
points = [(4, 5), (-0, 2), (4, 7), (1, -3), (3, -2), (4, 5), (3, 2), (5, 7), (-5, 7), (2, 2), (-4, 5), (0, -2),(-4, 7), (-1, 3), (-3, 2), (-4, -5), (-3, 2), (5, 7), (5, 7), (2, 2), (9, 9), (-8, -9)]
##### 1. Robin Hood is famous for hitting an arrow with another arrow. Find the coordinates of the points where an arrow hits another arrow.
unico_arrow=[]
arrow_in_arrow=[]
for j in points:
  if j not in unico_arrow:
    unico_arrow.append(j)
  else:
    if j not in arrow_in_arrow:
      arrow_in_arrow.append(j)
print(arrow_in_arrow)
#2. Calculate how many arrows have fallen in each quadrant.
#Note: the arrows that fall in the axis (x=0 or y=0) don't belong to any quadrant.
q1=[]
q2=[]
q3=[]
q4=[]
q5=[]
for k in points:
    if k[0]>0 and k[1]>0:
        q1.append(k)
    elif k[0]<0 and k[1]>0:
        q2.append(k)
    elif k[0]<0 and k[1]<0:
        q3.append(k)
    elif k[0]>0 and k[1]<0:
        q4.append(k)
    else:
        q5.append(k)
lq1=len(q1)
lq2=len(q2)
lq3=len(q3)
lq4=len(q4)
print(f'Q1 tiene {lq1} flechas')
print(f'Q2 tiene {lq2} flechas')
print(f'Q3 tiene {lq3} flechas')
print(f'Q4 tiene {lq4} flechas')
#3. Find the point closest to the center. Calculate its distance to the center.
#Take into account that there might be more than one point at the minimum distance to the center.
#Hint: Use the Euclidean distance. You can find more information about it here.
#Hint: Defining a function that calculates the distance to the center can help.
distance=[]
import math
for u in points:
  eclu=math.sqrt(u[0]**2+u[1]**2)
  distance.append(eclu)
minimo=min(distance)
minpoints=[]
for pos,item in enumerate(distance):
  if item==minimo:
    minpoints.append(points[pos])
print(f'Las flechas mas cercanas son {minpoints}, con una distancia euclidiana de {minimo}')
#4. If the archery target has a radius of 9, calculate the number of arrows that won't hit the target.
#Hint: Use the function created in step 3.
out=[]
intarget=[]
for k in points:
  if k[0]>=9 or k[1]>=9 or k[0]<=-9 or k[1]<=-9:
    out.append(k)
  else:
    intarget.append(k)
lenout=len(out)
#import inflect
#p = inflect.engine()
#number=p.number_to_words(lenout)
#print(f'Número de flechas fuera de la diana: {number}, flechas {out}')
#EJERCICIO 5
temperatures_C = [33, 66, 65, 0, 59, 60, 62, 64, 70, 76, 80, 81, 80, 83, 90, 79, 61, 53, 50, 49, 53, 48, 45, 39]
mimtemp=min(temperatures_C)
print(mimtemp)
maxtemp=max(temperatures_C)
print(maxtemp)
up70=[x for x in temperatures_C if x>=70]
print(up70)
average=sum(temperatures_C)/len(temperatures_C)
print(average)
#5. Imagine that there was a sensor failure at 3am and the data for that specific hour was not recorded. How would you estimate the missing value? Replace the current value of the list at 3am for an estimation.
hours=[x for x in range(0,len(temperatures_C))]
print(hours)
# Estimare que es la media de los regitros de las 1am, 2am, 4am, 5am, dandole un cuarto de peso a los datos de los extremos 1am y 5am.
estimation=[]
for pos,item in enumerate(hours):
  if item==1 or item==2 or item==4 or item==5:
    estimation.append(temperatures_C[pos])
est=int((estimation[0]*0.25+estimation[1]+estimation[2]+estimation[3]*0.25)/2.5)
print(est)
temperatures_C2=[est if x==0 else x for x in temperatures_C]
print(temperatures_C2)
#6. Bonus: the maintenance staff is from the United States and does not understand the international metric system. Help them by converting the temperatures from Celsius to Fahrenheit.
tempfahre=[x*9/5+32 if x==x else x for x in temperatures_C2]
print(tempfahre)
#7. Make a decision!
#Now it's time to make a decision taking into account what you have seen until now.
#Remember that if one of the following events occurs, then the cooling system needs to be replaced for a new one to avoid damaging the processor.
#More than 4 temperatures are greater than or equal to 70ºC.
#Any temperature is above 80ºC.
#The average temperature exceeds 65ºC.
#To make your decision, check if any of the three conditions above is met. You might need to use some of the variables you created in steps 1 to 6. Print a message to show if the cooling system needs to be changed or not.
if len(up70)>4 or maxtemp>80 or average>65:
  print('El sistema de refrigeración tiene que ser reemplazado')
else:
  print('El sistema de refrigeración no tiene que ser reemplazado')
#Bonus
#The company has decided that the decision you made is not valid. They want you to analyze the data again but this time, the conditions that need to be met in order to change the cooling system are different.
#This time, if one of the following events occurs, then the cooling system needs to be replaced:
#The temperature is greater than 70ºC during more than 4 consecutive hours.
#Any temperature is above 80ºC.
#The average temperature exceeds 65ºC.
#Follow the steps so that you can make the decision.

#1. Create a list with the hours where the temperature is greater than 70ºC. Store it in a variable.
up71=[x for x in temperatures_C if x>70]
print(up71)
#2. Check if the list you created in step 1 has more than 4 consecutive hours.
posit=[]
for posi,ite in enumerate(temperatures_C):
  for u in up71:
    if ite==u:
      posit.append(posi)
position=list(set(posit))
print(position)
po2=[]
po3=[]
for t in position:
  po2.append(t)
  if t-po2[len(po2)-2]==1:
    po3.append(1)
  elif len(po3)>3:
    po3.append(1)
  else:
    del po3[0:len(po3)]
if position[len(position)-1]-position[len(position)-2]==1:
  po3.append(1)
if len(po3)>4:
  print('Existen más de 4 horas consecutivas por encima de 70ªC')
else:
  print('No existen más de 4 horas consecutivas por encima de 70ªC') 
print(po3)
#version dos 
po2=[]
po3=1
for t in position:
  po2.append(t)
  if t-po2[len(po2)-2]==1:
    po3+=1
  elif po3>4:
    po3+=0
  else:
    po3==0
if po3>4:
  print('Existen más de 4 horas consecutivas por encima de 70ªC')
else:
  print('No existen más de 4 horas consecutivas por encima de 70ªC') 
print(po3)
#3. Make the decision!
#To make your decision, check if any of the three conditions is met. Print a message to show if the cooling system needs to be changed or not.  
if po3>4 or maxtemp>80 or average>65:
  print('El sistema de refrigeración tiene que ser reemplazado')
else:
  print('El sistema de refrigeración no tiene que ser reemplazado')
#4. Find the average value of the temperature lists (ºC and ºF). What is the relation between both average values?
print(temperatures_C2)
print(tempfahre)
def average(l):
  return sum(l)/len(l)
print(average(temperatures_C2)) 
print(average(tempfahre))
print('La relación es la formula 𝐹=1.8∗𝐶+32')
print(average(temperatures_C2)*9/5+32==average(tempfahre))
#5. Find the standard deviation of the temperature lists (ºC and ºF). What is the relation between both standard deviations?
def stdev(j):
  import math 
  num=0
  for n in j:
    num+=(n-average(j))**2
  div=len(j)
  return math.sqrt(num/div)
print(stdev(temperatures_C2))
print(stdev(tempfahre))
print('La relación es la formula stedev𝐹=1.8∗stedev𝐶')
print(stdev(tempfahre)/stdev(temperatures_C2))
#EJERCICIO 6 Rock, Paper & Scissors
#Let's play the famous game against our computer
#1. Import the choice function of the random module.
import random
#2. Create a list that includes the 3 possible gesture options of the game: 'rock', 'paper' or 'scissors'. Store the list in a variable called gestures.
gestures=['rock','paper','scissors']
#3. Create a variable called n_rounds to store the maximum number of rounds to play in a game.
#Remember that the number of rounds must be odd: 1, 3, 5, ...
n_rounds=(int(input(f'Cuantos números de rounds quieres jugar:')))
num_rounds=[]
#(int(input(f'Cuantos números de rounds quieres jugar:')))
#4. Create a variable called rounds_to_win to store the number of rounds that a player must win to win the game.
#Hint: the value stored in rounds_to_win depends on the value of n_rounds.
rounds_to_win=n_rounds//2+1
#5. Create two variables to store the number of rounds that the computer and the player have won. Call these variables cpu_score and player_score.¶
cpu_score=[]
player_score=[]
#6. Define a function that randomly returns one of the 3 gesture options.
#You will use this function to simulate the gesture choice of the computer.
def cpu_choi():
  import random
  cpu_choice=random.choice(gestures)
  return cpu_choice
#7. Define a function that asks the player which is the gesture he or she wants to show: 'rock', 'paper' or 'scissors'.
#The player should only be allowed to choose one of the 3 gesture options. If the player's choice is not rock, paper or scissors, keep asking until it is.
#player_choice=(input(f'Escoge entre {gestures[0]}, {gestures[1]} o {gestures[2]}:'))
#while player_choice!=gestures[0] and player_choice!=gestures[1] and player_choice!=gestures[2]:
 # player_choice=(input(f'Por favor escoge entre {gestures[0]}, {gestures[1]} o {gestures[2]}:'))

#8. Define a function that checks who won a round.
#The function should return 0 if there is a tie, 1 if the computer wins and 2 if the player wins.
def roundwin():
  cpu_choic=cpu_choi()
  num_rounds.append(1)
  print(f'Computer eligió {cpu_choic}')
  round2=0
  if cpu_choic==player_choice:
    round2=0
  elif cpu_choic==gestures[0] and player_choice==gestures[2]:
    round2=1
  elif cpu_choic==gestures[1] and player_choice==gestures[0]:
    round2=1
  elif cpu_choic==gestures[2] and player_choice==gestures[1]:
    round2=1 
  else:
    round2=2
  return round2
#9. Define a function that prints the choice of the computer, the choice of the player and a message that announces who won the current round.
#You should also use this function to update the variables that count the number of rounds that the computer and the player have won. The score of the winner increases by one point. If there is a tie, the score does not increase.
def win():
  roundw=roundwin()
  print(f'Player eligió {player_choice}')
  if roundw==2:
    print('Player win')
    player_score.append(1)
  elif roundw==1:
    print('CPU win')
    cpu_score.append(1)
  else :
    print('Tie')
  return
#10. Now it's time to code the execution of the game using the functions and variables you defined above.
#First, create a loop structure that repeats while no player reaches the minimum score necessary to win and the number of rounds is less than the maximum number of rounds to play in a game.
#Inside the loop, use the functions and variables above to create the execution of a round: ask for the player's choice, generate the random choice of the computer, show the round results, update the scores, etc.
while not any([len(cpu_score)>=rounds_to_win, len(player_score)>=rounds_to_win,len(num_rounds)>=n_rounds ]):
  player_choice=(input(f'Escoge entre {gestures[0]}, {gestures[1]} o {gestures[2]}:'))
  while player_choice!=gestures[0] and player_choice!=gestures[1] and player_choice!=gestures[2]:
    player_choice=(input(f'Por favor escoge entre {gestures[0]}, {gestures[1]} o {gestures[2]}:'))
  win()
  print(f'Player score:{len(player_score)}')
  print(f'CPU score:{len(cpu_score)}')
#1. Print the winner of the game based on who won more rounds.
#Remember that the game might be tied.
if player_score>cpu_score:
  print('El ganador es Player')
elif player_score<cpu_score:
  print('El ganador es CPU')
else:
  print('Empate entre CPU y Player')
#BONUS
#In this challenge, you need to improve the previous game by adding two new options. To know more about the rules of the improved version of rock, paper, scissors, check this link.
#In addition, you will also need to improve how the game interacts with the player: the number of rounds to play, which must be an odd number, will be requested to the user until a valid number is entered. Define a new function to make that request.
#Hint: Try to reuse the code that you already coded in the previous challenge. If your code is efficient, this bonus will only consist of simple modifications to the original game.
gestures2=['rock','paper','scissors','spock','lizard']
valid=False
while not valid:
  try:
    n_rounds2=(int(input(f'Cuantas rondas quieres jugar:')))
    valid=True
  except ValueError:
    print('Por favor, escoge un numero impar:')
while n_rounds2%2==0:
    n_rounds2=(int(input(f'Por favor, escoge un numero impar:')))
rounds_to_win2=n_rounds2//2+1
num_rounds2=[]
cpu_score2=[]
player_score2=[]
def cpu_choi2():
  import random
  cpu_choice2=random.choice(gestures2)
  return cpu_choice2

def roundwin2():
  cpu_choic2=cpu_choi2()
  num_rounds2.append(1)
  print(f'Computer eligió {cpu_choic2}')
  round3=0
  if cpu_choic2==player_choice2:
    round3=0
  elif cpu_choic2==gestures2[0] and player_choice2==gestures2[2] or player_choice2==gestures2[4]:
    round3=1
  elif cpu_choic2==gestures2[1] and player_choice2==gestures2[0] or player_choice2==gestures2[3]:
    round3=1
  elif cpu_choic2==gestures2[2] and player_choice2==gestures2[1] or player_choice2==gestures2[4]:
    round3=1 
  elif cpu_choic2==gestures2[3] and player_choice2==gestures2[0] or player_choice2==gestures2[2]:
    round3=1 
  elif cpu_choic2==gestures2[4] and player_choice2==gestures2[1] or player_choice2==gestures2[3]:
    round3=1 
  else:
    round3=2
  return round3

def win2():
  roundw2=roundwin2()
  print(f'Player eligió {player_choice2}')
  if roundw2==2:
    print('Player win')
    player_score2.append(1)
  elif roundw2==1:
    print('CPU win')
    cpu_score2.append(1)
  else :
    print('Tie')
  return

while not any([len(cpu_score2)>=rounds_to_win2, len(player_score2)>=rounds_to_win2,len(num_rounds2)>=n_rounds2 ]):
  player_choice2=(input(f'Escoge entre {gestures2[0]}, {gestures2[1]}, {gestures2[2]}, {gestures2[3]} o {gestures2[4]}:'))
  while player_choice2!=gestures2[0] and player_choice2!=gestures2[1] and player_choice2!=gestures2[2]and player_choice2!=gestures2[3]and player_choice2!=gestures2[4]:
    player_choice2=(input(f'Por favor escoge entre {gestures2[0]}, {gestures2[1]} , {gestures2[2]}, {gestures2[3]}, {gestures2[4]}:'))
  win2()
  print(f'Player score:{len(player_score2)}')
  print(f'CPU score:{len(cpu_score2)}')
if player_score2>cpu_score2:
  print('El ganador es Player')
elif player_score2<cpu_score2:
  print('El ganador es CPU')
else:
  print('Empate entre CPU y Player')
# EJERCICIO lytics
babyshark = '''Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt, doo doo doo doo doo doo
Let's go hunt!
Run away,…'''
# 1: First Paragraph
#Create a code to print the first paragraph and asign it to a variable.
firstp='''Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!'''
print(firstp)
#Step 2: Full song
#Create a code that prints the complete lyrics.
print(babyshark)
#Step 3: Check output
#Now i want you must create a string variable called result to store all the characters and check if it is equal to the lyrics. Remenber de hint section
result2=""
for x in babyshark:
  result2+=x
print(result2==babyshark)
#Step 4: Function
#Create a functions called babyshark() that generates the wanted output.
def baby_shark_lyrics():
  d=' doo'
  B='Baby shark'
  M='Mommy shark'
  D='Daddy shark'
  G='Grandma shark'
  F='Grandpa shark'
  L="Let's go hunt"
  O=d*6
  def a(c):
    u=f'''{c},{O}
{c},{O}
{c},{O}
{c}!'''
    return u
  b=f'''{a(B)}
{a(M)}
{a(D)}
{a(G)}
{a(F)}
{a(L)}
Run away,…'''
  return b
print(baby_shark_lyrics() == babyshark)

def baby_shark_lyrics2():
  a = {'Baby': ' shark','Mommy': ' shark','Daddy': ' shark','Grandma': ' shark','Grandpa': ' shark','Let\'s go hunt': ''}
  c = ''
  for k,v in a.items():
    c += '{}{},{}\n'.format(k, v, ' doo'*6)*3
    c += '{}{}!\n'.format(k,v)
  c += 'Run away,…'
  return c
print(baby_shark_lyrics2() == babyshark)

#print(baby_shark_lyrics())
#Step 5: Files
#Baby shark lyrics can be read in the songs folder. Try to store the content of that file in a variable called text and check if it is equal to the babyshark variable and the output of your baby_shark_lyrics function.
#https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
#text = open(r"C:\Users\carlospinero\data-prework\1.-Python\lyrics\songs\baby-shark.txt","r")
#Step 6: Refactor
#Now I want you to refactor your baby_shark_lyrics function in order to be less than 400 characters. If your code is larger than 400 characters, you should change baby_shark_lyrics function in order to shorten it.
import inspect
code = inspect.getsource(baby_shark_lyrics)
print('Your baby_shark_lyrics functions has {} characters'.format(len(code)))
print(len(code) < 400)
print(f'Your baby_shark_lyrics functions has {len(code)} characters')
#BONUUUUUUUUUUUUUUUS
def bottles_lyrics():
  def u():
    j='' ''
    for x in range(99,1,-1):
      j+=f'''{x} bottles of beer on the wall, {x} bottles of beer.
Take one down and pass it around, {x-1} bottles of beer on the wall.

'''
    return j
  bo=f'''{u()}1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.

No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.'''
  return bo
#version 2
def bottles_lyrics():
  j=''
  for x in range(99,2,-1):
    j+='{} bottles of beer on the wall, {} bottles of beer.\nTake one down and pass it around, {} bottles of beer on the wall.\n\n'.format(x,x,x-1)
  j+='2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.'
  return j
import inspect
code = inspect.getsource(bottles_lyrics)
print('Your bottles_lyrics functions has {} characters'.format(len(code)))
print(len(code) < 1000)
#print(bottles_lyrics()==bottle)
#EJERCICIO MISION IMPOSIBLE
#You are the computer scientist who has to protect valuable national intelligence data. This data is in a computer without internet connection in a room with a tactile floor that detects the pressure. But you've discovered that more than one spy has infiltrated and stolen data, so you have to implement and test the new security system.

#An ultrasensitive microphone has been installed that records all sound in the room. The list of sounds is stored in a list called dbs. As soon as the door closes it will alert if noise is detected above a threshold of 10 decibels: the alarm will sound and alert the entire building.

#Each item in the dbs list corresponds to a 5 second interval
dbs = [0, 1, 0, 0, 0, 0, 1, 0, 1, 23, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 20, 1, 1, 15, 1, 0, 0, 0, 40, 15, 0, 0]
# Show volumes that exceed 10 dBs
dbs10=[]
for x in dbs:
  if x>10:
    dbs10.append(x)
print(dbs10)
# Show the moments (indexs of the list) in which a volume exceeds 10 dBs
index=[]
for pos,it in enumerate(dbs):
  if it>10:
    index.append(pos)
print(index)
# Combine the last two exercises to show the moments when a volume exceeds 10 dBs. HINT: Use the enumerate function
comb=[]
for pos, it in enumerate(dbs):
  if it>10:
    comb.append((pos,it))
print(comb)
# Ethan is discovered if two consecutive volumes are greater than 10 dB. Is he safe? 
# HINT: Beware of the extremes, do not have an error of the type
# IndexError: list index out of range
print(index)
ind2=[]
ind3=1
for t in index:
  ind2.append(t)
  if t-ind2[len(ind2)-2]==1:
    ind3+=1
  elif ind3>=2:
    ind3+=0
  else:
    ind3==0
if ind3>=2:
  print('Existen dos escuchas consecutivas de más de 10dbs')
  print('Alarm!')
else:
  print('No existen dos escuchas consecutivas de más de 10dbs') 
#Bonus
#Now you have the role of Ethan's hacker. To cheat the security system you are going to execute a computer code on the list dbs and you are going to reduce all values higher than 20 in 12 dBs but the ones higher than 30 in 18 dBs. Then confirm the result of your operation by printing the new modified dbs list on the screen.
print('Pre hacking:\n',dbs)
dbshack=[]
for i in dbs:
  if i>30:
    dbshack.append(i-18)
  elif i>20 and i<=30:
    dbshack.append(i-12)
  else:
    dbshack.append(i)
print('Post hacking:\n',dbshack)
# KATA NIVEL 7
# ISOGRAMS
def is_isogram(string):
  p=0
  string=string.upper()
  for x in string:
    for j in string:
      if j==x:
        p+=1 
      else:
        p+=0
  if p==len(string):
    k=string
  else:
    k=8
  return k==string
#version 2
def is_isogram(string):
  return len(string) == len(set(string.lower()))
#version 3
def is_isogram(string):
  string = string.lower()
  for letter in string:
    if string.count(letter) > 1: return False
  return True
#del[a : b] :- This method deletes all the elements in range starting from index ‘a’ till ‘b’ mentioned in arguments.
order=[1,1,3,3,7,2,2,2,2]
del order[0:2]
print(order)
#pop() :- This method deletes the element at the position mentioned in its arguments.
order=[1,1,3,3,7,2,2,2,2]
order.pop(2)
print(order)
#insert(a, x) :- This function inserts an element at the position mentioned in its arguments. It takes 2 arguments, position and element to be added at respective position.
order=[1,1,3,3,7,2,2,2,2]
order.insert(3,99)
print(order)
#remove() :- This function is used to delete the first occurrence of number mentioned in its arguments.
order=[1,1,3,3,7,2,2,2,2]
order.remove(3)
print(order)
#sort() :- This function sorts the list in increasing order.
order=[1,1,3,3,7,2,2,2,2]
order.sort()
print(order)
#reverse() :- This function reverses the elements of list.
#al reves sin ordenar
order=[1,1,3,3,7,2,2,2,2]
order.reverse()
print(order)
#extend(b) :- This function is used to extend the list with the elements present in another list. This function takes another list as its argument.
order=[1,1,3,3,7,2,2,2,2]
order2=[99,86]
order.extend(order2)
print(order)
#clear() :- This function is used to erase all the elements of list. After this operation, list becomes empty.
order=[1,1,3,3,7,2,2,2,2]
order.clear()
print(order)
#count() is an inbuilt function in Python that returns count of how many times a given object occurs in list.
list1 = [1, 1, 1, 2, 3, 2, 1]  
print(list1.count(1)) 
#Given a list lst and a number N, create a new list that contains each number of lst at most N times without reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].
def delete_nth(order,max_e):
  order2=list(set(order))
  for j in order2:
    while order.count(j)>max_e:
      order.reverse()
      for x in order2:
        if order.count(x)>max_e:
          order.remove(x)
      order.reverse() 
  return order
print(delete_nth([1,1,3,3,7,2,2,2,2],1))
#version 1
def delete_nth(order,max_e):
    order2 = []
    for x in order:
        if order2.count(x) < max_e: 
          order2.append(x)
    return order2
print(delete_nth([1,1,3,3,7,2,2,2,2],1))
#Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.
#For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.
#[10, 343445353, 3453445, 3453545353453] should return 3453455.
#version 1
def sum_two_smallest_numbers(numbers):
  h=[]
  min1=min(numbers)
  for x in numbers:
    if x!=min1:
      h.append(x)
  min2=min(h)
  return min1 +min2
#version 2
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])
#version 3
def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]
#Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b.
#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:
#array_diff([1,2,2,2,3],[2]) == [1,3]
def array_diff(a, b):
  h=[]
  for x in a:
    h.append(x)
    for y in b:
      if x==y and x in h:
        h.remove(x)
  return h
#version 2
def array_diff(a, b):
  return [x for x in a if x not in b]
#version 3
def array_diff(a, b):
  h=[]
  for x in a:
    if x not in b:
      h.append(x)
  return h
#Given a positive number n > 1 find the prime factor decomposition of n. The result will be a string with the following form :
#"(p1**n1)(p2**n2)...(pk**nk)"
#with the p(i) in increasing order and n(i) empty if n(i) is 1.
#Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
def primeFactors(n):
  i = 2
  factors = []
  while i * i <= n:
    if n % i:
      i += 1
    else:
      n //= i
      factors.append(i)
  if n > 1:
    factors.append(n)
  string=''
  set_factors=sorted(set(factors))
  for x in set_factors: 
    if factors.count(x)>1:
      string+=f'({x}**{factors.count(x)})' 
    else:
      string+=f'({x})'
  return string
#version 2
def primeFactors(n):
  ret = ''
  for i in range(2, n + 1):
    num = 0
    while(n % i == 0):
      num += 1
      n /= i
    if num > 0:
      ret += '({}{})'.format(i, '**%d' % num if num > 1 else '')
    if n == 1:
      return ret
#clase
def hola(a):
  s=' '
  j=s.join(a)
  return j
Pedro=['Pedro','Garcia']
print(hola(a=Pedro))

def list2string(str_lst):
  str_lst_fixed = [str(e) for e in str_lst]
  string = ' '.join(str_lst_fixed)
  return string
list2string(['my', 'name', 'is', 1])

def keyword_arguments(**kwargs):
  print(kwargs)
  return 1

a = keyword_arguments(a=5, b=2, c=3, david=45, asdf='b')
#PANDAS
def get_means(df):
    df.columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numeric = df.select_dtypes('number')
    #numeric = df._get_numeric_data()
    means_df = pd.DataFrame(numeric.mean()).reset_index()#crea un nuevo data frame
    means_df.columns = ['colname', 'mean'] #no hace falta
    return means_df
print(get_means(data))
print(data.mean())
data.info()
data.dtype()
data['age'].mean() #solo de pandas data['age'] para seleccionar columnas
data.info(memory_usage='deep')
data.index
data.columns
data.shape
pd.to_datetime(data)
data.year
def analyze_df(df,colnames):
  for col in colnames:
    print(f'mean {df[col].mean()})
    print(f'max {df[col].max()}')
    print(f'minimo {df[col].min()}')
def increment_year(df):
  df['year']=df['year']+1    

#errores
#atributos 
from collections import nametuple
person= nametuple('person','name age year')
david= person(name='carlos',age=30,year=1987)
david.name
david.age
david.year
#key error
d.get('x','default')
d.['d']=8 #añadir al diccionario
d['d'] #llamar
#type error
#value error
#import error no tienes importador instalado
#io error archivo que no existe ruta mal
#manually raisen exceptions
def even_number_check(n):
  if n % 2 != 0:
    raise ValueError("number is not even, try again ¯\_(⊙︿⊙)_/¯")
  else:
    print('this number is even ʕᵔᴥᵔʔ')
#el que tu quieres
class ASASAS(Exception):
  pass
def integer_number_check(n):
  if type(n) is not int:
    raise ASASAS("number is not an integer, try again ¯\_(⊙︿⊙)_/¯")
  else:
    print('this number is an integer ʕᵔᴥᵔʔ')
integer_number_check('a')

#exception handling
try: #lo que querermos ejecutar
  even_number_check(2)
except ValueError: #salvo si hay error 
  print('the number is not even...')
  raise
else: #ejecutar cuando no hay error
  print('the number is even, no error was raised...')
finally: #ejecutar siempre
  print('this is going to execute whatever happens...')
print('this cell is going to execute till the end...')

def even_number_check(n):
  if n % 2 != 0:
    raise ValueError("number is not even, try again ¯\_(⊙︿⊙)_/¯")
  else:
    print('this number is even ʕᵔᴥᵔʔ')
        
def integer_number_check(n):
  if type(n) is not int:
    raise ValueError("number is not an integer, try again ¯\_(⊙︿⊙)_/¯")
  else:
    print('this number is an integer ʕᵔᴥᵔʔ')

number_list = [1, 2, 3, 4, 5, 5.5, 6, 7, 8, 9, 10, 'a']
evens = []

for number in number_list:
    
  try:
    integer_number_check(number)
  except ValueError:  # broad error clauses are not recommended
    print(f'error checking the number {number} is integer...')
  else:
    print(f'checking the number: {number} is integer finished OK...')
        
    try:
      even_number_check(number)
    except ValueError:
      print(f'error checking the number {number} is even...')
    else:
      evens.append(number)


#se ejecuta siempre
try:
  print('br')
except:
  pass

#KATA Total amount of points
#version 1
def points(games):
  total=0
  for x in games:
    if len(x)==3:
      if int(x[0])>int(x[2]):
        total+=3
      elif int(x[0])==int(x[2]):
        total+=1
    elif len(x)>3:
      if x[1]==':':
        if int(x[0])>int(x[2]+x[3]):
          total+=3
        elif int(x[0])==int(x[2]+x[3]):
          total+=1
      elif x[2]==':':
        if int(x[0]+x[1])>int(x[3]):
          total+=3
        elif int(x[0]+x[1])==int(x[3]):
          total+=1
  return total 
#version 2
def points(games):
  count = 0
  for score in games:
    res = score.split(':')
    if res[0]>res[1]:
      count += 3
    elif res[0] == res[1]:
      count += 1
  return count
#Strings