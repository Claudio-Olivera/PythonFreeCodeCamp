class CuentaBancaria: #con mayuscula nombre de clase al inicio y despues camel case
    def __init__(self, num_cuenta, nombre_titular, balance): #incializacion, self esta relacionado con la instancia actual
    #la instancia a su vez es cada una de las cuentas bancarias que crearé a partir de la clase(son los objetos.)
        self.num_cuenta = num_cuenta
        self.nombre_titular = nombre_titular
        self.balance = balance
#hasta este punto definimos los atributos de la clase, ahora empieza la definicion de metodos.(lso metodos son las funciones.)

    def generar_balance(self):
        print(self.balance)
    
    def nombre_del_usuario(self):
        print(self.nombre_titular)

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto

#asi se crea una instancia de la clase CuentaBancaria, el self se omite.
mi_cuenta = CuentaBancaria("105-356-643","Nora Smith", 5600)
#aca ejecuto los metodos para el objeto creado a partir de la clase es decir, el objeto seria mi_cuenta y usa los metodos que tiene la clase.
mi_cuenta.generar_balance()
mi_cuenta.depositar(400)
mi_cuenta.generar_balance()
mi_cuenta.nombre_del_usuario()

mi_cuenta2 = CuentaBancaria("305-256-983","Roberto Carlos", 10)

mi_cuenta2.generar_balance()
mi_cuenta2.depositar(15000)
mi_cuenta2.generar_balance()
mi_cuenta2.nombre_del_usuario()




    

        