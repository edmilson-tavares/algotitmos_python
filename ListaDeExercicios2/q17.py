print("-"*70)
print("Lendo N números")
print("Digite 0 quando quiser encerrar o programa")
print("-"*70)

contador = 0
soma = 0
maximo = -10000000000
minimo = +10000000000
valor = -1
while valor != 0:
    valor = float(input(f"Digite o {contador + 1}º número: "))
    contador += 1
    soma += valor
    maximo = valor if valor > maximo else maximo
    minimo = valor if valor < minimo and valor != 0 else minimo

print(f"Foram lidos {contador-1} números.")
print(f"A soma deles é {soma}.")
print(f"O maior número é o {maximo}.")
print(f"O menor número é o {minimo}.")
