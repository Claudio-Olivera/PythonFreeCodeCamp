#sentencia with nos permite leer archivos asi:
# with open("<nombre_archivo>.txt","r") as archivo:
    #trabajar con el archivo

with open("frases_famosas.txt","r") as archivo: #tambien se puede usar f o file en ingles para ese ultimo archivo de la linea. IMPORTANTE: EL "r" es read , el "w" es write, el "a" es (append-añadir), el signo + incluye leer ejemplo: w+ es leer y escribir.
    for linea in archivo:
        print ("=== Frase ===") #como podemos ver muestra en consola este agregado a cada linea que tengo en el archivo frases_famosas.
        print (linea) 

#otro ejemplo con write 
notas = {
    "Nora": 87,
    "Gino": 100,
    "Loretto": 67,
    "Talina": 45
}
with open ("data_estudiantes.txt","w") as archivo:
    for nombre, nota in notas.items():
        archivo.write(nombre + "-" + str(nota) + "\n") #el \n es para que se cambie de linea despues de cada iteracion

#otro ejemplo con append 
nuevas_notas = {
    "Emily": 54,
    "Daniel":98,
    "Julienne":78
}

with open ("data_estudiantes.txt","a") as archivo: #notar que ahora estoy usando "a", pero el mismo archivo que use antes, "data_estudiantes.txt, como estoy usando "a", agrego los nuevos datos a el mismo archivo. 
    for nombre, nota in nuevas_notas.items():
        archivo.write(nombre + "-" + str(nota) + "\n") 
        


