class ContaCorrente():
    def __init__(self, numero, nome, saldo = 0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def deposito(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado com sucesso!")

    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado com sucesso!")
        else:
            print(f"Saldo insuficiente para o valor R$ {valor}!")

    def imprimir_saldo(self):
        print("-"*70)
        print(f"Correntista: Sr(a). {self.nome}")
        print(f"Saldo: R$ {self.saldo}")
        print("-"*70)

conta = ContaCorrente("51478", "Edmilson")
conta.imprimir_saldo()
conta.deposito(1000)
conta.saque(550)
conta.saque(500)
conta.imprimir_saldo()



