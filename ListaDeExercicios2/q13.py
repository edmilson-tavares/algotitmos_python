cont_par = 0
cont_impar = 0

for i in range(5):
    num = int(input(f"Digite o {i+1} número: "))
    if num % 2 == 0:
        cont_par += 1
    else:
        cont_impar += 1

print(f"Resultado: {cont_par} pares e {cont_impar} ímpares.")