# Arquivo principal
from Pessoa import Pessoa
from Funcionario import Funcionario

# Objeto da classe Pessoa
p1 = Pessoa('João', '123', 20)
# Imprimir dados do objeto
print(p1.get_nome())
print(p1.get_cpf())
print(p1.get_idade())
# Objeto em versão texto
print(p1)

# Objeto funcionario
f1 = Funcionario('José', '456', 40,
                 '0099', 2526.45,
                 'Biblioteca')

print(f1.get_nome())
print(f1)