print("-"*70)
print("Hipermercado Tabajara")
print("1 - Filé duplo")
print("2 - Alcatra")
print("3 - Picanha")
print("-"*70)

carne = int(input("Digite a carne desejada: "))
qtd_kg = float(input("Digite a quantidade desejada: "))
tipo_pagamento = int(input("O pagamento será no cartão tabajara? \nx' 1 - SIM \n 2 - NÃO\n"))

if qtd_kg > 0 and qtd_kg <= 5:
    if carne == 1:
        preco = 4.9
        valor = qtd_kg * preco
    elif carne == 2:
        preco = 5.9
        valor = qtd_kg * preco
    elif carne == 3:
        preco = 6.9
        valor = qtd_kg * preco
    else:
        print("Opção inválida!")
        exit()
elif qtd_kg > 5:
    if carne == 1:
        preco = 5.8
        valor = qtd_kg * preco
    elif carne == 2:
        preco = 6.8
        valor = qtd_kg * preco
    elif carne == 3:
        preco = 7.8
        valor = qtd_kg * preco
    else:
        print("Opção inválida!")
        exit()
else:
    print("Quantidade de kg menor ou igual a zero.")
    exit()

print("=======================================")
print("          SUPERMERCADO TABAJARA        ")
print("           CUPOM FISCAL SIMPLES        ")
print("=======================================")
print("Item        Quantidade    Preço (R$)")
print("---------------------------------------")

if carne == 1:
    print(f"Filé duplo       {qtd_kg}Kg          {preco}")
elif carne == 2:
    print(f"Alcatra      {qtd_kg}Kg           {preco}")
else:
    print(f"Picanha       {qtd_kg}Kg           {preco}")

print("---------------------------------------")
subtotal = qtd_kg * preco
print(f"Subtotal:                 R$ {subtotal:.2f}")
if tipo_pagamento == 1:
    desconto = subtotal * 0.1
else: desconto = 0
print(f"Desconto:                 R$ {desconto:.2f}")
total = subtotal - desconto
print(f"TOTAL A PAGAR:            R$ {total:.2f}")
print("---------------------------------------")
print("       Obrigado pela preferência!       ")
print("=======================================")
