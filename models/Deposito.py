
from models import Transacao


class Deposito(Transacao):
    def __init__ (self, valor):
        self.valor = valor