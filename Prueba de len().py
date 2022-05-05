pruebaDeLen = "hola mundo" 
print (len(pruebaDeLen))
#aca le digo que me muestre el largo de la variable pruebaDeLen#

print (pruebaDeLen [1],pruebaDeLen[5])
#aca le digo que me muestre el indice 1 y el indice 5#

print (pruebaDeLen [5:8]) #aca le digo que empieza en indice 5 y termina en el indice 8 a eso se le llama slice, fijarse que el indice que marco como final siempre es uno mas de lo que busco obtener# 

print (pruebaDeLen [5:])  #aca como no pongo nada como valor final, va a imprir desde el indice 5 hasta el final#

print (pruebaDeLen[:3]) #aca es lo inverso al anterior, imprime desde el inicio hasta el numero que le diga de indice#

print (pruebaDeLen[:]) #aca imprimo todos los indices

print (pruebaDeLen[::2]) #aca imprimo con un valor de paso (2) todos los caracteres, el resultado que arroja es hl ud , para el string "hola mundo", esto sucede porque esta saltando dos posiciones de inicio a final#

print (pruebaDeLen[0:10:2]) #lo mismo que el de arriba pero esta vez especificando los indices de inicio y fin#



