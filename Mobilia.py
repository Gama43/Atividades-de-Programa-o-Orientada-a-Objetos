class Mobilia:
    def __init__(self, codigo: int, descricao: str):
        self.__codigo = codigo
        self.__descricao = descricao

    @property
    def codigo(self):
      if isinstance(self.__codigo, int): 
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
      if isinstance(self.__codigo, int): 
        self.__codigo = codigo

    @property
    def descricao(self):
      if isinstance(self.__descricao, str): 
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
      if isinstance(self.__descricao, str): 
        self.__descricao = descricao  
       