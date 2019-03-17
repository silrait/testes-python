import sys

from src.leilao.excecoes import LanceInvalido


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    @property
    def carteira(self):
        return self.__carteira

    @property
    def nome(self):
        return self.__nome

    def propoe_lance(self, leilao, valor):
        if not self.__valor_e_valido(valor):
            raise LanceInvalido('Não pode propor lance maior que o valor da carteira')

        lance = Lance(self, valor)
        leilao.propoe(lance)
        self.__carteira -= valor

    def __str__(self):
        return f'Usuario [nome = {self.__nome}]'

    def __valor_e_valido(self, valor):
        return valor <= self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

    def __str__(self):
        return f'Lance [usuario = {self.usuario}, valor = {self.valor}]'

    def __repr__(self):
        return self.__str__()


class Leilao:

    def __init__(self, descricao):
        self.__maior_lance = sys.float_info.min
        self.__menor_lance = sys.float_info.max
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances[:] # Retorna uma cópia da lista

    @property
    def maior_lance(self):
        return self.__maior_lance

    @property
    def menor_lance(self):
        return self.__menor_lance

    def __str__(self):
        return f'Leilao [descricao = {self.descricao}, Lances = {self.lances}]'

    def __len__(self):
        return len(self.__lances)

    def propoe(self, lance: Lance):
        if self.__lance_e_valido(lance):
            if not self.__tem_lances():
                self.__menor_lance = lance.valor

            self.__maior_lance = lance.valor

            self.__lances.append(lance)

    def __lance_e_valido(self, lance):
        return not self.__tem_lances() or (self.__usuarios_diferentes(lance) and
                                           self.__valor_e_maior_que_lance_anterior(lance))

    def __usuarios_diferentes(self, lance):
        if self.__lances[-1].usuario != lance.usuario:
            return True

        raise LanceInvalido('O mesmo usuário não pode dar dois lances seguidos')

    def __tem_lances(self):
        return self.__lances

    def __valor_e_maior_que_lance_anterior(self, lance):
        if lance.valor > self.__lances[-1].valor:
            return True

        raise LanceInvalido('O valor do lance deve ser maior que o anterior')


