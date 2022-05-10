class Cliente:
    def __init__(self,nome,fone):
      self.__nome = nome
      self.__fone = fone
      print(self, nome, fone)
      
    @property
    def nome(self):
        return self.__nome
      
    @nome.setter
    def nome(self,nome):
      self.__nome = nome
      
    @property
    def fone(self):
        return self.__fone

    @nome.setter
    def nome(self,fone):
      self.__fone = fone