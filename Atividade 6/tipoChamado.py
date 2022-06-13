from abstractTipoChamado import AbstractTipoChamado


class TipoChamado(AbstractTipoChamado):
    def __init__(self, codigo: int, descricao: str, nome: str):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__nome = nome

    @property
    def codigo(self) -> int:
        if isinstance(self.__codigo, int):
            return self.__codigo

    @property
    def descricao(self) -> str:
        if isinstance(self.__descricao, str):
            return self.__descricao

    @property
    def nome(self) -> str:
        if isinstance(self.__nome, str):
            return self.__nome
