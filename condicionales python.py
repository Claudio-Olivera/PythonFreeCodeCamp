#en python despues de la condicion hay que colocar : , y debe estar identado., tener en cuenta el tema de la indentacion , sino no anda.
temperatura = int(input("ingrese la temperatura actual: "))
if temperatura < 25:
    print("Hace frio")
elif temperatura >25 and temperatura<35:
    print("Esta Templado")
else: 
    print ("Hace calor")

#puede haber muchas elif y al final siempre else.