#un diccionario es una coleccion de pares clave-valor

#ejemplo:
numeros={"A": 45,"B": 30} 
#"A:45" es un par clave-valor, y en cada par hay una clave("A") y un valor(45),van : y un espacio entre los : y el valor. Y a su vez cada clave-valor debe estar separada por una , y un espacio despues de la misma.

#las claves son unicas e innmutables., no admite listas, pero si tuplas. Deben ser unicas y no deberian existir dos iguales.ya que se reemplazarian

#los valores asociados pueden ser de cualquier tipo

#la clave se usa para accerder a su valor asociado

#los pares clave-valor pueden ser añadidos, modificados, eliminados, por lo tanto son mutables.

#Como acceder al valor en un diccionario.
print(numeros.get("A"))#devuelve 45

#Como añadir  pares clave-valor
numeros["C"]=56 #CLAVE Y VALOR A AGREGAR
print(numeros) 

#Como modificar pares clave-valor
numeros["C"]=17 #actualizo el valor
print(numeros)

#Como remover pares clave-valor
del numeros["B"]
print(numeros)

#revisar la existencia de un elemento
print("B" in numeros)





