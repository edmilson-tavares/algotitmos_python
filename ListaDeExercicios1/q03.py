altura = float(input("Digite sua altura: "))

peso_ideal_homem = (72.7*altura) - 58
peso_ideal_mulher = (62.1*altura) - 44.7

print("-"*70)
print("RESULTADO")
print(f"Homem, seu peso ideal é {round(peso_ideal_homem, 2)} kg!")
print(f"Mulher, seu peso ideal é {round(peso_ideal_mulher, 2)} kg!")
print("-"*70)