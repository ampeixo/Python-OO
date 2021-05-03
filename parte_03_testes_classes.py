# Código para testes com a classe (ContaCorrente) da (conta.py)

from conta import ContaCorrente

# criando dois obejtos de conta corrente
conta1 = ContaCorrente(203, "Erick Clapton", 100.00)
print(conta1)
conta2 = ContaCorrente(204, "BB King", 50.00)
print(conta2)

valor_deposito = 100.00
valor_saque = 50.00

# testando o método deposita
conta1.deposita(valor_deposito)
print("após o depósito, de {} ".format(valor_deposito))
# testando o método extrato
conta1.extrato()

conta2.deposita(valor_deposito)
print("após o depósito, de {} ".format(valor_deposito))
conta2.extrato()

# testando o método trasnfere
conta1.transfere(25.50, conta2)
conta1.extrato()
conta2.extrato()
# testando o método com trasnferência maior que o limite da conta
conta1.transfere(675.00, conta2)

# <---------------------------------------->
"""código para testes com as classes estáticas:
Quando definimos um método estático, ou seja, de classe,
podemos chamá-lo sem a necessidade de criação de um objeto antes.
Portanto a sintaxe para isso é bastante simples, bastando chamar
um método depois do nome da classe."""
codigos = ContaCorrente.codigos_bancos()
print(codigos)
print(codigos['BB'])
print(codigos['Caixa'])
