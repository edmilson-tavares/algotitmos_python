def imprime_n(n = 0):
    cont = 0
    if n == 0:
        exit()
    else:
        for i in range(n):
            cont += 1
            for j in range(cont):
                print(j+1, end=' ')
            print()

n = int(input("Digite um valor para n: "))
imprime_n(n)

