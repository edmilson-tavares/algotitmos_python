class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def muda_lado(self, lado):
        self.lado = lado

    def retorna_lado(self):
        return self.lado

    def calcula_area(self):
        return self.lado**2

print("-"*70)
print("Cálculo de área de um quadrado")
lado = float(input("Digite o valor(em cm) do lado do quadrado: "))
quadrado = Quadrado(lado)
print(f"Área: {quadrado.calcula_area()} cm²")
print("Agora vamos dobrar o lado do quadrado, assim temos: ")
quadrado.muda_lado(lado*2)
print(f"Área: {quadrado.calcula_area()} cm²")
print("-"*70)
