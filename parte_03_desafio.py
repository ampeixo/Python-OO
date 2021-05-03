"""Lançamos o seguinte desafio: para ajudar na formatação de datas você deve criar uma nova classe
auxiliar. Essa classe deve representar uma Data (sem hora) que sabe imprimir uma data formatada.

Ela deve funcionar dessa forma:
from datas import Data
d = Data(21,11,2007)
d.formatada()

Imprime:
21/11/2007

Crie e implemente essa classe dentro de uma arquivo datas.py. Mãos à obra!
"""


class Data:
    def __init__(self, dia, mes, ano):
        print("Construindo a classe...{}".format(self))
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formata_data(self):
        print("{}/{}/{}".format(self.dia, self.mes, self.ano))
        # tipo de formatação por f-strings, uma maneira mais nova de formatação
        print(f"{self.dia}/{self.mes}/{self.ano}")


data1 = Data(20, 4, 2021)
data1.formata_data()

