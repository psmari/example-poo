from conta_bancaria import ContaBancaria

# criando o objeto
conta_1 = ContaBancaria('Samuel', 10000)
conta_1.__saldo = 1
print(conta_1.__saldo)
conta_1.consultar_saldo()