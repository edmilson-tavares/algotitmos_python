print("-"*70)
print("Lanchonete")
print("=====================================")
print("Especificação        Código     Preço")
print("=====================================")
print("Cachorro Quente       100     R$ 1,20")
print("Bauru Simples         101     R$ 1,30")
print("Bauru com ovo         102     R$ 1,50")
print("Hambúrguer            103     R$ 1,20")
print("Cheeseburguer         104     R$ 1,30")
print("Refrigerante          105     R$ 1,00")
print("=====================================")
print("Para encerrar, digite um código inexistente!")
item_100 = 0
item_101 = 0
item_102 = 0
item_103 = 0
item_104 = 0
item_105 = 0
codigo = int(input("Digite o código do produto: "))
while codigo > 99 and codigo < 106:
    quantidade = int(input("Digite a quantidade desejada: "))
    if codigo == 100:
        item_100 += quantidade
    elif codigo == 101:
        item_101 += quantidade
    elif codigo == 102:
        item_102 += quantidade
    elif codigo == 103:
        item_103 += quantidade
    elif codigo == 104:
        item_104 += quantidade
    elif codigo == 105:
        item_105 += quantidade

    codigo = int(input("Digite o código do produto: "))

if (item_100+item_101+item_102+item_103+item_104+item_105) != 0:
    # Dados básicos do cupom
    print("=======================================")
    print("               LANCHONETE             ")
    print("=======================================")
    print("Item        Quantidade    Preço (R$)")
    print("---------------------------------------")

    if item_100 > 0:
        print(f"Cachorro Quente       {item_100}       R$ 1,20")
    if item_101 > 0:
        print(f"Bauru Simples         {item_101}       R$ 1,30")
    if item_102 > 0:
        print(f"Bauru com ovo         {item_102}       R$ 1,50")
    if item_103 > 0:
        print(f"Hambúrguer            {item_103}       R$ 1,20")
    if item_104 > 0:
        print(f"Cheeseburguer         {item_104}       R$ 1,30")
    if item_105 > 0:
        print(f"Refrigerante          {item_105}       R$ 1,00")
    # Subtotal e outros valores
    print("---------------------------------------")
    total = (item_100 * 1.2) + (item_101 * 1.3) + (item_102 * 1.5) + (item_103 * 1.2) + (item_104 * 1.3) + (item_105 * 1)
    print(f"TOTAL A PAGAR:            R$ {total:.2f}")
    print("---------------------------------------")
    print("       Obrigado pela preferência!       ")
    print("=======================================")