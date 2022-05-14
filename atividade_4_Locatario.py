class Locatario:
    def __init__(self, codigo: int, nome: str, telefone: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__telefone = telefone

    @property
    def codigo(self):
        if isinstance(self.__codigo, int): 
          return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
      if isinstance(self.__codigo, int): 
        self.__codigo = codigo

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
