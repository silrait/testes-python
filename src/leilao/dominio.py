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
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances

    def __str__(self):
        return f'Leilao [descricao = {self.descricao}, Lances = {self.lances}]'

    def __getitem__(self, item):
        return self.__lances[item]

    def __len__(self):
        return len(self.__lances)


class Avaliador:
    def __init__(self):
        self.__maior_lance = sys.float_info.min
        self.__menor_lance = sys.float_info.max

    @property
    def maior_lance(self):
        return self.__maior_lance

    @property
    def menor_lance(self):
        return self.__menor_lance

    def avalia(self, leilao: Leilao):
        for lance in leilao.lances:
            if(lance.valor > self.maior_lance):
                self.__maior_lance = lance.valor
            elif(lance.valor < self.menor_lance):
                self.__menor_lance = lance.valor


    def __str__(self):
        return f'Avaliador [maior lance = {self.maior_lance}, menor lance = {self.menor_lance}]'

