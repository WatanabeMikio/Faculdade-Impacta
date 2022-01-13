
class Pessoa:
    
    def __init__(self, nome, idade, rg):
        # Os atributos abaixo são privados:
        self.__nome = nome
        self.__idade = idade
        self.__rg = rg
        self.__rg_conjuge = -1
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    
    @property
    def rg(self):
        return self.__rg
    
    @property
    def rg_conjuge(self):
        return self.__rg_conjuge
    
    @property
    def esta_casado(self):
        if self.__rg_conjuge <= 0:
            return False
        else:
            return True
    
    @idade.setter
    def idade(self, nova_idade):
        if isinstance(nova_idade, int) and nova_idade >= 0:
            self.__idade = nova_idade
    
    @rg_conjuge.setter
    def rg_conjuge(self, valor):
        self.__rg_conjuge = valor

    def casar(self, outra_pessoa):
        if (not self.esta_casado) and (not outra_pessoa.esta_casado):
            self.__rg_conjuge = outra_pessoa.rg
            outra_pessoa.rg_conjuge = self.__rg
        

# Programa principal
pes1 = Pessoa("João Silva", 25, 12345)
pes2 = Pessoa("Maria Santos", 22, 9876)

print("Nome:", pes1.nome, "Casado?", pes1.esta_casado)
print("Nome:", pes2.nome, "Casado?", pes2.esta_casado)
pes1.casar(pes2)
print("Nome:", pes1.nome, "Casado?", pes1.esta_casado)
print("Nome:", pes2.nome, "Casado?", pes2.esta_casado)

