
from models import Cliente

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)  # Chama o construtor da classe Cliente
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


     
        
