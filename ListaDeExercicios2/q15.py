print("-"*70)
print("Cálculo da série de Fibonacci até um valor > 500")
print("-"*70)
n = int(input("Você deseja ver quantos números da série: "))

n_1 = 1
n_2 = 1
print(n_1)
print(n_2)
n_aux = 0
while n_aux <= 500:
    n_aux = n_1 + n_2
    print(n_aux)
    n_1 = n_2
    n_2 = n_aux
