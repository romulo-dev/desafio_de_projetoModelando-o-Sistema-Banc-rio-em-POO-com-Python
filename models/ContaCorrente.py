

from models import Conta


class ContaCorrente(Conta):
    def __init__(self, limite, limite_saques, saldo, numero, agencia, cliente, historico):
        super.__init__(saldo, numero, agencia, cliente, historico)
        self.limite = limite
        self.limite_saques = limite_saques