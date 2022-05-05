#estructura de control en programacion que permite ejecutar una o varias lineas de codigo multiples veces.
# 
# lo usamos cuando sabemos cuantas veces se debe repetir.
# 
# Iteracion: repeticion de bucle o cliclo.

# for <var> in range(<inicio>, <fin>) :

#el <var> seria una variable de control, se actualiza automaticamente antes de cada iteracion, utilizar un nombre descriptivo

#el range retorna una secuencia de valores y se lo asigna a cada  

for i in range(4):
    print(i) #imprime 0 1 2 3 ya que el valor de i se actualiza antes de cada iteracion.

#range retorna una secuencia de valores, y cada uno de esos valores va a ser asignado a la variable de control , range es una secuencia de numeros enteros.

#tambien tener en cuenta que en el valor de range se puede especificar desde donde queremos iniciar la secuencia range(1,4)

for i in range(1,4):
    print(i) #ya no imprime 0

 #range tambien tiene parametros start , stop, step
 #for i in range(start,stop[,step]):   

#------ciclos sobre iterables-----------
#iterables retornan uno a la vez , los iterables en python son:
#cadenas de caracteres
#listas
#tuplas
#diccionarios
#otros

#asi : for <var> in <iterable>:
            #cuerpo del ciclo

for char in "Loops": #con strings
    print(char)

for num in [6,7,8]: #con listas
    print(num)    

for num in (10,11,12): #con tuplas
    print(num)   

letras = {"a":50, "b":60} #con diccionarios
for clave in letras:
    print(clave) #para ver sus claves

for valor in letras.values(): #para mostrar los valores de las claves
    print (valor)  #50 y 60

for clave,valor in letras.items():#para mostrar el par clave-valor entero. 
    print(clave,valor) #a 50 y b 60