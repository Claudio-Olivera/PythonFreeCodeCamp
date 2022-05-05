#las importaciones sirven para poder modularizar mi programa y que distintos archivos python trabajen juntos.

#Modulo: En python es un archivo que contiene definiciones y sentencias, constantes,etc, se busca que esten relacionados los archivos , despues tendremos un programa principal donde importaremos el codigo de otros modulos.

#Importacion: Es una sentencia que da acceso a las funciones y constantes definidas en el modulo importado.

# ejemplo : import nombre_modulo 

#por lo general los imports deberian ser lo primero que este definido en nuestro programa.
# si luego de importarlo quiero llamar a una funcion que esta dentro de uno de los modulos a los cuales le hice import, se llamaria de la siguiente manera :  nombre_modulo.funcion(args)

#IMPORTANTE: Python tiene muchos modulos incorporados, por ejemplo uno de ellos es math, que tiene funciones matematicas. Por ejemplo la funcion pow, que eleva a la potencia, seria 9 al cuadrado , es decir 9*9 = 81.:
import math
print(math.pow(9,2)) #asi accedo a una funcion incorporada en math
print(math.pi) #asi accedo a una constante del modulo importado(math) al ser una constante no cambia nunca. devuelve el numero pi.

#OTRA FORMA DE IMPORTAR UN MODULO ES DARLE UN NOMBRE ALTERNATIVO
# import nombre_modulo as nombre_alternativo

import math as matematicas
print(matematicas.pow(9,2))
print(matematicas.pi)

#otra forma es importar solo un elemento de un modulo y no todo el modulo
# from nombre_modulo import elemento 
from math import pow
print(pow(3,2)) # 3*3 = 9 

#otra forma posible pero no recomendada es importar todo del modulo y podras usar las funciones sin tener que decir de que modulo vienen de esta manera, pero no es recomendado ya que podemos pisar funciones que se llamen igual o generar confusion generalizada extrema, mas cuando son archivos grandes.: 

# from modulo import *
from math import *
print (pow(4,2))

#aca simplemente hago la prueba de traer un dato de otro modulo
from recursion import factorial
print (factorial(6)) #se puede ver en consola que tambien corre la funcion fibonacci, averiguar porque ocurre esto.
