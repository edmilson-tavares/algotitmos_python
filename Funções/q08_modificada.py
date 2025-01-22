def qtd_digitos(numero):
    cont = 1
    while numero // 10 != 0:
        numero = numero / 10
        cont += 1
    print(cont)

numero = int(input("Digite um número:"))
qtd_digitos(numero)