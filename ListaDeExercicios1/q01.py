inteiro_1 = int(input("Digite o 1º número inteiro: "))
inteiro_2 = int(input("Digite o 2º número inteiro: "))
real = float(input("Digite um número real: "))

item1 = (2 * inteiro_1) * (inteiro_2 / 2)
item2 = (3 * inteiro_1) + (real)
item3 = real**3

print("-"*70)
print("RESULTADO")
print(f"Produto do dobro do primeiro com metade do segundo: {item1}")
print(f"Soma do triplo do primeiro com o terceiro: {item2}")
print(f"O terceiro elevado ao cubo: {item3}")
print("-"*70)

