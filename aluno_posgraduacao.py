from aluno import Aluno

class AlunoGraduacao (Aluno):
  def __init__(self, elaborando_tese: bool, matricula:int, cpf: int, dias_de_emprestimo: int):
    super().__init__(cpf, dias_de_emprestimo, matricula)
    if isinstance (elaborando_tese, bool):
      self.__elaborando_tese = elaborando_tese

  @property
  def elaborando_tese(self):
    return self.__elaborando_tese
  
  @elaborando_tese.setter
  def elaborando_tese(self, elaborando_tese: bool):
    if isinstance(elaborando_tese, bool):
      self.__elaborando_tese = elaborando_tese

  def emprestar(self, titulo_livro:str):
    if self.__elaborando_tese is True:
      self.__dias_de_emprestimo * 2
      
    return f'Aluno de matricula {self.__matricula} pegou emprestado o livro: {titulo_livro} com {self.__dias_de_emprestimo} dias de prazo'