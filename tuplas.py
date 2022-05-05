#estructura de datos inmutable que contiene una secuencia ordenada de elementos.

#ejemplo de tupla en python: (1,2,3,4) 

#puede contener cualquier tipo de datos
#valores de distintos tipos de datos
#cada posicion se identifica con un entero denominado indice.
#a diferencia de las listas son immutables, es decir no se pueden cambiar

#si intento editar la tupla = ERROR ejemplo: 
# a=(1,2,3,4) 
# a[0] = 5
# como resultado tengo un Error.
# 
# Acceder a un elemento de tupla
#tener cuidado con la identacion en python.
letras = ("a", "b", "c")
print(letras[0]) 

#Saber si existe elemento en una tupla
print("b" in letras)

#Buscar el indice de elemento en una tupla
print(letras.index("c"))

#contar el numero de ocurrencias del elemento en la tupla
numeros=(3,4,5,5,5,6,7,8,9,40,5,6,45,5,5,6,4,5,6,8,75,6,5,453,54,5,4,7,8,3,2,69,5)
print(numeros.count(5)) #cuenta el numero de veces que esta 5 en al lista.


