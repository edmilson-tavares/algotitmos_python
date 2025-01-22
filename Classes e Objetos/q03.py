class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def muda_lados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def retorna_lados(self):
        print(f"Comprimento: {self.ladoA} e Largura: {self.ladoB}")

    def calcula_area(self):
        return self.ladoA * self.ladoB

    def calcula_perimetro(self):
        return 2 * (self.ladoA + self.ladoB)

print("-"*70)
print("Cálculo de piso e rodapé de uma área")
comprimento = float(input("Digite o comprimento(em m) da área desejada: "))
largura = float(input("Digite a largura(em m) da área desejada: "))
area_desejada = Retangulo(comprimento, largura)
print(f"Piso: {area_desejada.calcula_area()} m²")
print(f"Rodapé: {area_desejada.calcula_perimetro()} m")
area_desejada.retorna_lados()
print("-"*70)
