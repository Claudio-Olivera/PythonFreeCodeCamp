#error de Sintaxis , ocurre cuando no se siguen las reglas formales para escribir el codigo.
#ejemplo x =% 3
#otro ejemplo x= 5 if x > 15 ---> notar que en el if no coloco los : al final
# otro "hola' dos tipos de comillas distintos.
#otro error: no identar el codigo 


#excepciones son errores detectados durante la ejecucion del programa, como resultado el programa se detiene abruptamente.

# ejemplo : "Hola, Mundo"[45]  -- Error: fuera de rango 

# cuando trabajamos con diccionarios, error de clave o key error, se da cuando tratamos de acceder a una clave que no existe en el diccionario.
# puntos= {"Gino":25, "Marta":80}
# puntos["jack"] #podemos ver que jack no existe en el diccionario.

#otro error es cuando quiero usar una variable que no fue definida previamente ejemplo:
# print(lista_colores) 

#otro error es cuando queremos dividir por 0 
# print(5/0)

#otro error es el RecursionError Maximun recursion depth exceeded in comparison.
# def factorial(n):
# if n == 0 or n == 1
    #return 1
# else:
    #return n * factorial(n)  #como podemos ver el ultimo n de la lina 27 no tiene manera de disminuir y por lo tanto nunca va a alcanzar el caso base. 

#podemos usar try y except para hacer un manejo de posibles errores, con try , se ejecuta el codigo o intenta ejecutarlo y con except (en caso de haber error ) se ejecuta el cambio u otro codigo que queremos . 
#ejemplo:
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

try:
    resultado=num1/num2
    print(f"{num1 / num2}=", resultado)
except:
    print("Alerta, Excepcion")

    #tambien puedo decirle al except explicitamente que tipo de error quiero que maneje except ,es mucho mas recomendado  ejemplo:
try:
    resultado=num1/num2
    print(f"{num1 / num2}=", resultado)
except ZeroDivisionError:   #tambien se puede tener multiples except , se escriben una abajo de otra.
    print("No puede dividir por 0.")   

    #tambien podemos hacer que el except maneje esto como variable
try:
    resultado=num1/num2
    print(f"{num1 / num2}=", resultado)
except ZeroDivisionError as e:
    print(e)

    #tambien se puede usar la clausula else sirve como respaldo al igual que en los condicionales.
try:
    resultado=num1/num2
    print(f"{num1 / num2}=", resultado)
except ZeroDivisionError as e:
    print(e)
else:
    print("No ocurre una excepcion") #hay que ingresar valores validos ejemplo 4 / 2

    #tambien tenemos la clausula finally ejecuta codigo independientemente si hay o no excepciones, es usado por ejemplo, para cuando queremos cerrar un archivo, es algo que tiene que ocurrir siempre en nuestro programa.Independientemente de las excepciones  y try's

try:
    resultado=num1/num2
    print(f"{num1 / num2}=", resultado)
except ZeroDivisionError as e:
    print(e)
finally:
    print("Programa Terminado")

    
