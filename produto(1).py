class Produto:
    def __init__(self,codigo,descricao,categoria: categoria_produto,quantidade,preco,cliente):
      self.__codigo = codigo
      self.__descricao = descricao
      self.__categoria = categoria_produto
      self.__quantidade = quantidade
      self.__preco = preco
      self.__cliente = cliente
      print(self, 'fui criado')

    def codigo(self):
      return self.__codigo

    def codigo(self,codigo):
      self.__codigo = codigo

    def descricao(self):
      return self.__descricao

    def descricao(self,descricao):
      self.__descricao = descricao

    def categoria(self):
      return self.__

    def codigo(self,codigo):
      self.__codigo = codigo
