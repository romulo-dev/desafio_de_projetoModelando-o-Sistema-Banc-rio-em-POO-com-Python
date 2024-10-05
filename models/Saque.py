
from models.Transacao import Transacao


class Saque(Transacao):
    def __init__ (self, valor):
        self.valor = valor