def funcao(numero):
    if numero > 0:
        return "P"
    elif numero < 0:
        return "N"
    else:
        return "Número zero!"

n = int(input("Digite um número: "))
resultado = funcao(n)

print(f"Resultado: {resultado}")