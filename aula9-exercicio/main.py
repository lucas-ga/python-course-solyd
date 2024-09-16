# Crie um software de gerenciamento bancário
# Esse software poderá ser capaz de criar clientes e contas
# Cada cliente possui nome, cpf e idade
# Cada conta possui um cliente, saldo, limite, sacar,
# depositar e consultar saldo

from cliente import Cliente
from conta import Conta

cliente_lucas = Cliente("Lucas",12345678901,25)
conta_lucas = Conta(cliente_lucas)

conta_lucas.consultar_saldo()

conta_lucas.sacar(50)

conta_lucas.consultar_saldo()

conta_lucas.depositar(275)

conta_lucas.consultar_saldo()