class Locador:
    def __init__(self, cpf: int, nome: str, telefone: int, endereco: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def cpf(self):
      if isinstance(self.__cpf, int): 
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
      if isinstance(self.__cpf, int): 
        self.__cpf = cpf

    @property
    def nome(self):
      if isinstance(self.__nome, str): 
        return self.__nome

    @nome.setter
    def nome(self, nome):
      if isinstance(self.__nome, str): 
        self.__nome = nome

    @property
    def telefone(self):
      if isinstance(self.__telefone, int): 
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone):
      if isinstance(self.__telefone, int): 
        self.__telefone = telefone

    @property
    def endereco(self):
      if isinstance(self.__endereco, str): 
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
      if isinstance(self.__endereco, str): 
        self.__endereco= endereco
