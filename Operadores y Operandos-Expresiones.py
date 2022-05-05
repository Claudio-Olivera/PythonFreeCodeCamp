#Expresion es una combinacion de valores, variables y operadores que al ser evaluados resultan en un valor#
#Las expresiones se evaluan de izquierda a derecha a no ser que haya algun operador de mayor importancia#

#1#Operadores:

#Aritmeticos:suma , resta, multiplicacion, division, division Entera, exponente y Modulo, a tener en cuenta la division por mas que sea exacta siempre retorna un numero de coma flotante es decir: 15/5 = 3.0, no se puede hacer division por 0 15/0 = ERROR.                                   pero si quiero una division que devuelva entero para eso esta division entera y se representa asi : 15 // 3 = 3 , de esta manera evitamos que el resultado sea de coma flotante. trunca los decimales, no los redondea.

#la exponencia se coloca asi : 5**3 = 125  // 5**0 = 1 

#operador modulo retorna el resto de una division asi: 5%2=1 , 4%3=1 esto es muy util si queremos saber pares o impares, si el resto es 1 el numero es impar, si es 0 es par, pero lo tenemos que hacer con 2 obviamente , asi: 4%2 = 0 es par , 5%2=1 es impar.

#el orden de prioridad de las operaciones es :
#parentesis, #exponentes, #multiplicacion, #division, #suma , #resta.De izquierda a derecha.


#Logicos: valores booleanos, True, False, and, or, not.

#para saber mas de and revisar truth table, comprueba si el valor de las expresiones de un lado y del otro de and son verdaderos o falsos.          asi: (5<6) and (6>8)  devuelve False.

#or unicamente cuando ambos operandos son falsos , el resultado sera falso (5<6) or (6>8) devuelve True. ya que uno de sus operandos es verdadero.

#not si la expresion es verdadera el resultado sera falso, y si es falso sera true.Simplemente niega .

#not tiene la mayor prioridad, despues and, y por ultimo or , si hay igual prioridad se evalua de izquierda a derecha.



#Operadores Relacionales :Utilizados para comprar valores y retornan booleanos >, >=, <, <= , ==, !=

#Operadores de Asignacion: =, +=, -=, *=, /=, **=, //=, %= .

