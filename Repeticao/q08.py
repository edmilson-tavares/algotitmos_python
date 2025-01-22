soma = 0
for i in range(5):
    num = float(input(f"Digite o {i+1}º número:"))
    soma += num

print(f"Soma = {soma}")
media = soma / 5
print(f"Média = {media}")
