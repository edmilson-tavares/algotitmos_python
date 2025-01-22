
print("-"*70)
print("Cálculo da sequência H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N")
print("-"*70)

n = int(input("Digite o valor de N: "))
h = 0
for i in range(1, n+1):
    h += 1/i

print("Resultado: ", h)
