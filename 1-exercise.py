""" 
Cree una clase de Python llamada BankAccount que represente una cuenta bancaria, 
que tenga como atributos: número de cuenta, nombre (nombre del propietario de la cuenta) y saldo.
Cree un método Deposit() que gestione las acciones de depósito.
Cree un método de retiro () que administre las acciones de retiro.
Cree un método bankFees() para aplicar las tarifas bancarias con un porcentaje del 5% del saldo de la cuenta.
Cree un método display() para mostrar los detalles de la cuenta.
"""

class BankAccount:
    def __init__(self, cuenta, propietario, saldo):
        self.cuenta = cuenta
        self.propietario = propietario
        self.saldo = saldo
        print(f'Bienvenid@: {self.propietario}, su # de cuenta es: {self.cuenta} y su saldo disponible es {self.saldo} soles')

    def deposito(self,monto_deposito):
        self.monto_deposito = monto_deposito
        self.__saldoTotal = self.saldo + self.monto_deposito
        print(f'El monto depositado fue {monto_deposito} soles y su saldo Actual es {self.__saldoTotal} soles')

    def retiro(self,monto_retiro):
        self.monto_retiro = monto_retiro
        self.__saldoTotal = self.__saldoTotal - self.monto_retiro
        print(f'El monto retirado fue {monto_retiro} soles y su saldo Actual es {self.__saldoTotal} soles')

    def bankFees(self):
        self.__tarifa = (5/100)*(self.__saldoTotal)
        self.__saldoTotal = self.__saldoTotal- self.__tarifa
        print(f'Este movimiento tiene un costo de {self.__tarifa} soles, su saldo actual es {self.__saldoTotal} soles despues de las transacciones realizadas')

    def display(self):
        print(f'Hasta luego: {self.propietario}, su saldo disponible es: {self.__saldoTotal} soles')

cuenta = BankAccount(123456, "Marvelys", 100 )
cuenta.deposito(70)
cuenta.retiro(10)
cuenta.bankFees()
cuenta.display()
