class CategoriaProduto:
    def __init__(self, titulo):
        self.__titulo = titulo

    def setTitulo(self,titulo):
        self.__titulo = titulo

    def getTitulo(self):
      return self.__titulo