# -------- exemplos de funções

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor  # o mesmo que conta["saldo"] = conta ["saldo"] + valor
    return conta["saldo"]


def saca(conta, valor):
    conta["saldo"] -= valor
    return conta["saldo"]


def extrato(conta):
    print("seu saldo é de {}".format(conta["saldo"]))


# -------- código para teste das funções
conta1 = cria_conta(203, "Alberto Magno", 100.00, 550.00)
print(conta1)

valor_deposito = 100.00
valor_saque = 50.00

deposita(conta1, valor_deposito)
print("após o depósito, de {} ".format(valor_deposito))
extrato(conta1)

saca(conta1, valor_saque)
print("após o saque, de {} ".format(valor_saque))
extrato(conta1)


