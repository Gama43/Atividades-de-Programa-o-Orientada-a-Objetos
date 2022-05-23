from usuario_bu import UsuarioBU

class Funcionario(UsuarioBU):
  def __init__(self, departamento:str, cpf, dias_de_emprestimo):
    super().__init__(cpf, dias_de_emprestimo)
    if isinstance (departamento, str):
      self.__departamento = departamento

  @property
  def departamento(self):
    return self.__departamento
  
  @departamento.setter
  def departamento(self, departamento: str):
    if isinstance(departamento, str):
      self.__departamento = departamento

  def emprestar(self, titulo_livro:str):
    return f' do departamento {self.__departamento} pegou emprestado o livro {titulo_livro} com {dias_de_emprestimo} de prazo'

  def devolver(self, titulo_livro:str):
    return f' do departamento {self.__departamento} devolveu o livro: {titulo_livro}
