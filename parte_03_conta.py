# Código para exemplos de classes

class ContaCorrente:
    def __init__(self, numero, titular, saldo, limite=500.00):
        print("Construindo a classe...{}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

# Métodos
    def extrato(self):
        print("Saldo de R${}, do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saca(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print("Você tão tem limite disponível para esse valor de saque!")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

# Getters e Setters
    @property
    def saldo(self):
        return self.__saldo

    @property
    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

# Métodos estáticos
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}
