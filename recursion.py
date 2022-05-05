# La recursion es definir algo en terminos de si mismo.

#Sucesion de Fibonacci.Es un ejemplo muy famoso de una sucesion recursiva.

#sucesion: es una secuencia de numeros que siguen un patron.

# 0,1,1,2,3,5,8,13,21, ...
# fib(n) = fib(n-1)+fib(n-2)

#las funciones recursivas son las que se llaman a si mismas.
#tienen dos elementos principales:
#caso base , permite que el proceso se detenga.
#el caso recursivo, permite que se descomponga el problema para hacerlo mas pequeño hasta que logramos que llegue a caso base.

#EJEMPLO DE ESTO:

#from html.entities import name2codepoint esto se creo cuando lo importe en el modulo de importaciones? wtf??


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) #estas dos son funciones recursivas, ya que estan reusando la funcion dentro de la funcion., siempre tienen que reducir la funcion restando, no se si dividiendo sirve, pero disminuir es necesario para en algun momento poder llegar al stop,osea caso base, que seria n==0 or n==1.

print(fibonacci(8)) #estoy pasando en realidad la posicion (supongamos que es el indice de una lista) de fibonacci que quiero saber y me devuelve el numero correspondiente en la sucesion de fibonacci , eso es lo que hace esta funcion. es decir: la sucesion de fibonacci seria esta : 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, etc... , podemos notar que si contamos posiciones empezando en 0 , la posicion 8 la ocupa el numero 21, si le pasaramos como parametro 10, nos devolveria 55.


#otro ejemplo de recursividad para saber factoriales:

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4)) #es decir 4*3*2*1 = 21 , el factorial de 5 seria 5*4*3*2*1 = 120 eso es un numero factorial.

