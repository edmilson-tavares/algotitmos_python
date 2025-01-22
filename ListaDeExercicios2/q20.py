print("-" * 70)
print("Cálculo da sequência S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.")
print("-" * 70)

n = int(input("Digite o valor de n: "))
m = 1
s = 0
for i in range(1, n + 1):
    s += i / m
    m += 2

print("Resultado: ", s)