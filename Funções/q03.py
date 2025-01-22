def soma(*argumento):
    print(argumento)
    print(type(argumento))
    soma = 0
    for i in argumento:
        soma += i
    return soma


n1 = float(input("Número 1: "))
n2 = float(input("Número 2: "))
n3 = float(input("Número 3: "))
soma_final = soma(n1, n2, n3)
print(f"Resultado = {soma_final}")
