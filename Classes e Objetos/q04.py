class Pessoa():
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        for i in range(anos):
            if self.idade < 21:
                self.altura += 0.5

            self.idade += 1

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, cm):
        self.altura += cm

    def imprimir_pessoa(self):
        print("-"*70)
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Peso: {self.peso}")
        print(f"Altura: {self.altura}")
        print("-"*70)

pessoa1 = Pessoa("Edmilson", 28, 74.4, 170)
pessoa1.imprimir_pessoa()
pessoa1.emagrecer(4)
pessoa1.imprimir_pessoa()

pessoa2 = Pessoa("Pedro", 18, 79.4, 180)
pessoa2.imprimir_pessoa()
pessoa2.envelhecer(5)
pessoa2.imprimir_pessoa()

pessoa3 = Pessoa("Farney", 15, 65, 172)
pessoa3.imprimir_pessoa()
pessoa3.envelhecer(10)
pessoa3.engordar(20)
pessoa3.imprimir_pessoa()

pessoa4 = Pessoa("José", 10, 52, 150)
pessoa4.imprimir_pessoa()
pessoa4.envelhecer(10)
pessoa4.engordar(15)
pessoa4.crescer(10)
pessoa4.imprimir_pessoa()

