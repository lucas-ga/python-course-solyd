from cliente import Cliente

class Conta:

    limite = 0
    saldo = 0

    def __init__(self, cliente):

        Conta.cliente = cliente
        Conta.saldo = 0
        Conta.limite = 500

    def sacar(self, valor):

        if (Conta.saldo + Conta.limite) >= valor:
            Conta.saldo = Conta.saldo - valor
        else:
            print("limite insuficiente")

    def depositar(self, valor):
        Conta.saldo = Conta.saldo + valor

    def consultar_saldo(self):
        print("Seu saldo é de:",Conta.saldo)