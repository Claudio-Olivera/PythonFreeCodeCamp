#Lista:
# Es una estructura de datos utilizada para almacenar multiples valores en una secuencia.
#ejemplo: [1,2,3,4,5] 
# secuencia ordenada:
# ["a","b","c"] 0="a", 1="b", 2="c"
#Puede contener valor de cualquier tipo y de distintos tipo en cada uno.
#SON MUTABLES, es decir modificables.

autos = ["audi","ferrari","bmw"]

print(autos[1], autos[2]) #devuelve en consola el ferrari, que esta en el indice 1

#agregar elementos al final de la lista
autos.append("ford")
print(autos[3])

#agregar en la posicion de indice que quiero insertar el elemento.
autos.insert(1,"lamborgini")
print(autos) #agregue lamborgini a la lista en la posicion que quiero, eso desplaza la posicion de ferrari y de los otros elementos.

#remover un elemento
autos.append("bmw") #muestra 2 bmw
print(autos)
autos.remove("bmw") #remueve el primer bmw de la lista
print (autos)#ahora solo muestra un bmw

#si intento remover algo que no esta en la lista ERROR.

#como encontrar un elemento o ver si esta 
print("ferrari" in autos) #si esta es True
print("pontiac" in autos) #no esta es False

#index , para retornar el indice de la primera aparicion del elemento en la lista.Si no se encuentra elemento da error.
print(autos.index("ford"))

#actualizar el valor de una lista
autos[0] = "pontiac" #cambia audi por pontiac
print(autos)

#--------Metodos de listas-----------
#.count(elem) contar elementos de una lista
#.extend(lista) extender una lista agregandole otra
#.pop() elimina y retorna un elemento de una lista
#.reverse() reversa el orden actual de la lista
#.sort() ordena ascendente o descendente una lista.




