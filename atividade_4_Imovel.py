from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia


class Imovel:
    def __init__(self, codigo: int, descricao: str,
                 valor: float, locador: Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = locador
        self.__locatarios = []
        self.__mobilias = []

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

    @property
    def valor(self):
        if isinstance(self.__valor, float):
            return self.__valor

    @valor.setter
    def valor(self, valor):
        if isinstance(self.__valor, float):
            self.__valor = valor

    @property
    def locador(self):
        if isinstance(self.__locador, Locador):
            return self.__locador

    @locador.setter
    def locador(self, locador):
        if isinstance(self.__locador, Locador):
            self.__locador = locador

    @property
    def locatarios(self):
        return self.__locatarios

    def incluir_locatario(self, locatario: Locatario):
        if isinstance(locatario, Locatario) and (locatario not in
                                                 self.__locatarios):
            self.__locatarios.append(locatario)

    def excluir_locatario(self, codigo_locatario: int):
        for locatario in self.__locatarios:
            if locatario.codigo == codigo_locatario:
                self.__locatarios.remove(locatario)

    @property
    def mobilias(self):
        return self.__mobilias

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        situacao = True
        for mobilia in self.__mobilias:
            if mobilia.codigo == codigo_mobilia:
                situacao = False
                break
        if situacao is True:
            self.__mobilias.append(self)

    def excluir_mobilia(self, codigo_mobilia: int):
        for mobilia in self.__mobilias:
            if mobilia.codigo == codigo_mobilia and mobilia in self.__mobilias:
                self.__mobilias.remove(mobilia)

    def find_locatario_by_codigo(self, codigo_locatario: int):
        for locatario in self.__locatarios:
            if locatario.codigo == codigo_locatario:
                return locatario
