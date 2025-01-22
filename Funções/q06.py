def conversao(hora, tipo):
    if hora > 12:
        hora -= 12
    return hora

def impressao(horas, minutos, tipo):
    if tipo == 'A':
        print(f"Hora convertida: {horas}:{minutos} {tipo}/M")
    elif tipo == 'P':
        print(f"Hora convertida: {horas}:{minutos} {tipo}/M")
    else:
        print("Formato inválido!")

aux = 1
while aux == 1:
    horas = int(input("Digite as horas: "))
    minutos = int(input("Digite os minuntos: "))

    print("Digite A para A/M ou P para P/M")
    tipo = input("Digite o formato da hora: ")

    hora_convertida = conversao(horas, tipo)
    impressao(hora_convertida, minutos, tipo)

    print("-" * 70)
    print("Menu de opções")
    print("0 - Encerrar")
    print("1 - Nova conversão")
    print("-" * 70)

    aux = int(input("Digite uma opção: "))
