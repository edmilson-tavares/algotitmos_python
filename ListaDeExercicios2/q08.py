print("-"*70)
print("Posto de combustível")
print("A - Álcool")
print("G - Gasolina")
print("-"*70)
litros = 0
while(litros <= 0 or combustivel not in ('A', 'a', 'G', 'g')):
    litros = float(input("Digite a quantidade de litros vendidos: "))
    combustivel = input("Digite qual foi o tipo de combustível: ")
    if combustivel == 'A' or combustivel == 'a':
        if litros > 0 and litros <= 20:
            valor_pago = litros * (4.89 - (4.89*3/100))
        elif litros > 20:
            valor_pago = litros * (4.89 - (4.89*5/100))
        else:
            print("Quantidade inválida. Digite novamente!")
    elif combustivel == 'G' or combustivel == 'g':
        if litros > 0 and litros <= 20:
            valor_pago = litros * (6.69 - (6.69*4/100))
        elif litros > 20:
            valor_pago = litros * (6.69 - (6.69*6/100))
        else:
            print("Quantidade inválida. Digite novamente!")

    else:
        print("Combustível inválido. Digite novamente!")

print("-"*70)
print("Posto de combustível")
print(f"Valor a ser pago: R$ {valor_pago}")
print("-"*70)
