maior = 0
for i in range(5):
    num = float(input(f"Digite o {i+1}º número:"))
    if num > maior:
        maior = num

print(f"Maior número é {maior}")