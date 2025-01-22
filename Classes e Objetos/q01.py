class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        print(self.cor)

bola = Bola("azul", "10", "plástico")
bola.mostra_cor()
bola.troca_cor("vermelho")
bola.mostra_cor()

print("-"*70)
print("Objeto completo")
print("Cor: ", bola.cor)
print(f"Circunferência: {bola.circunferencia} cm")
print("Material:", bola.material)
print("-"*70)
