from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []
        super().__init__()

    @property
    def clientes(self) -> list:
        return self.__clientes

    @property
    def tecnicos(self) -> list:
        return self.__tecnicos

# Permite a inclusao de um novo cliente na lista de clientes
# @param codigo codigo do Cliente
# @param nome nome do Cliente
# @return retorna o cliente inserido

    def inclui_cliente(self, codigo: int, nome: str) -> Cliente:
        if isinstance(codigo, int) and \
         isinstance(nome, str) and \
         self.__clientes is not None:
            for cliente in self.__clientes:
                if cliente.codigo == codigo:
                    break
            else:
                self.__clientes.append(Cliente(nome, codigo))
            return self.__clientes[-1]


# Permite a inclusao de um novo tecnico na lista de tecnicos
# @param codigo codigo do tecnico
# @param nome nome do tecnico
# @return retorna o tecnico inserido

    def inclui_tecnico(self, codigo: int, nome: str) -> Tecnico:
        if isinstance(codigo, int) and codigo is not None and \
           isinstance(nome, str) and nome is not None:
            situacao = True
            for tecnico in self.__tecnicos:
                if tecnico.codigo == codigo:
                    situacao = False
                    break
            if situacao is True:
                self.__tecnicos.append(Tecnico(nome, codigo))
            return self.__tecnicos[-1]
