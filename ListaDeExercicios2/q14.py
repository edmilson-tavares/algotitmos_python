print("-"*70)
print("Cálculo da série de Fibonacci")
print("-"*70)
n = int(input("Você deseja ver quantos números da série: "))

n_1 = 1
n_2 = 1
print(n_1)
print(n_2)
for i in range(n-2):
    n_aux = n_1 + n_2
    n_1 = n_2
    n_2 = n_aux
    print(n_aux)