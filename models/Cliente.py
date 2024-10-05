
from models import Conta


class Cliente:

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, transacao):
        conta_operacao = None
        numero_conta = int(input("Digite o número da conta"))
        for conta in self.contas:
            if conta.numero == numero_conta:
                saque_valido = conta.sacar(transacao.valor)
                if saque_valido == True:
                    conta.historico.adicionar_transacao(transacao) 
                    return
                else:
                    return
        print("Conta inexistente")
        

    
    def adicionar_conta(self, conta):
        # Método para adicionar uma conta à lista de contas do cliente
        self.contas.append(conta)