import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def __str__(self):
        return f'Usuario [nome = {self.__nome}]'


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
        if not self.__lances or self.__lances[-1].usuario != lance.usuario and lance.valor > self.__lances[-1].valor:
            if (lance.valor > self.maior_lance):
                self.__maior_lance = lance.valor
            if (lance.valor < self.menor_lance):
                self.__menor_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('Erro ao propor lance')


