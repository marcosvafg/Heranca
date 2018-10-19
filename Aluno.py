# Classe aluno
# Importando classe Pessoa
from Pessoa import Pessoa

class Aluno(Pessoa):
    # Método construtor
    def __init__(self, nome, cpf, idade):
        super().__init__(nome, cpf, idade)