from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        super().__init__()
        self.__chamados = []
        self.__tiposchamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado) -> int:
        numero = 0
        if isinstance(tipo, TipoChamado) and tipo is not None:
            for chamado in self.__chamados:
                if chamado.tipo == tipo:
                    numero += 1
        return numero

    def inclui_chamado(self, data: Date, cliente: Cliente,
                       tecnico: Tecnico, titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado) -> Chamado:
        if isinstance(data, Date) and data is not None and \
           isinstance(cliente, Cliente) and cliente is not None and \
           isinstance(tecnico, Tecnico) and tecnico is not None and \
           isinstance(titulo, str) and titulo is not None and \
           isinstance(descricao, str) and descricao is not None and \
           isinstance(prioridade, int) and prioridade is not None and \
           isinstance(tipo, TipoChamado) and tipo is not None:
            situacao = True
            for chamado in self.__chamados:
                if chamado.data == data and chamado.cliente == cliente and \
                 chamado.tecnico == tecnico and chamado.tipo == tipo:
                    situacao = False
            if situacao is True:
                self.__chamados.append(Chamado(data, cliente, tecnico,
                                               titulo, descricao,
                                               prioridade, tipo))
            return self.__chamados[-1]

    def inclui_tipochamado(self, codigo: int,
                           nome: str, descricao: str) -> TipoChamado:
        if isinstance(codigo, int) and codigo is not None and \
           isinstance(nome, str) and nome is not None and \
           isinstance(descricao, str) and descricao is not None:
            for tipoChamado in self.__tiposchamados:
                if tipoChamado.codigo == codigo:
                    break
            else:
                self.__tiposchamados.append(TipoChamado
                                            (codigo, nome, descricao))
            return self.__tiposchamados[-1]

    @property
    def tipos_chamados(self):
        return self.tipos_chamados
