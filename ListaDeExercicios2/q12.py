print("-"*70)
print("Exponenciação")
print("-"*70)

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = 1
for i in range(expoente):
    resultado *= base

print("Resultado: ", resultado)