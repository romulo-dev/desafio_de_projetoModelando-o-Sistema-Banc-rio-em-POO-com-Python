
class Conta:

    def __init__(self, numero, cliente, historico, saldo = 0, agencia = "0001"):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
        self.saldo = saldo
        self.agencia = agencia

    def novaConta(cliente, numero):
        nova_conta = Conta(numero, cliente)
        cliente.adicionar_conta(nova_conta)
        return nova_conta


    def sacar(self, valor):
        
        if valor <= 0 or valor > self.saldo:
            print("Valor inválido")
            return False
        else:
            self.saldo -= valor
            print("Saque realizado com sucesso")
            return True
        
    def saldo(self):
        return self.saldo
        


    def depositar(self, valor):
        if valor >= 0:
            print("valor válido")
            return True
        else:
            print("Valor inválido")
            return False