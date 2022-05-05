#funcion: Es un bloque de codigo reutilizable que realiza una sala tarea especifica.

# def <funcion> (parametro):
    #codigo #no olvidar la identacion

def mostrar_mensaje ():
    print("¡Hola, Mundo!")

mostrar_mensaje() #para llamar la funcion va pegado tambien al borde 

pizzas=0
sanguchitos=0
empanadas=2
def ahora_con_parametro(pizzas, sanguchitos):
    print (pizzas + sanguchitos + empanadas)
ahora_con_parametro(int(input("aca el numero de pizzas: ")), int(input("aca el numero de sanguchitos: ")) )

#pizzas y sanguchitos son los parametros y los argumentos son los valores que les asignemos, es decir, el argumentos de empanadas es 2

#las funciones pueden retornar valores.

def mostrar_cantidad_empanadas(empanadas):
    return empanadas + 5 #una vez que llega al return se detiene la funcion inmediatamente. Si no hay return devuelve None

print(mostrar_cantidad_empanadas(empanadas)) #la funcion tiene un retorno si la pongo dentro de un print me devuelve el return de la funcion en consola.

#SCOPE: es el alcance de una variable en el programa, y determina donde se podra usar.
# hay dos tipos de scope en python , el global, y el local, las globales son definidas en el programa principal y pueden ser utilizadas en todo el programa, pero las variables locales que son definidas dentro de la funcion solo pueden ser utilizadas dentro de la funcion.

#ejemplo:

x = 6 # x es la variable global
def f(y):
    print (x+y) # Y es la variable local es 
f(2)
#y si llamo a y no me la va a reconocer. ya que no esta definida globalmente. 