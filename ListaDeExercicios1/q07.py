area = float(input("Digite o tamanho em metros quadrados da área a ser pintada:"))
litros = area/6


#adicionando os 10% de folga
litros = litros + litros*0.1

#para latas de 18 litros
latas = litros/18

if(litros <= 18):
    latas = 1
else:
    # latas = latas//1 + 1    --  tanto faz usar essa linha ou a linha abaixo
    latas = int(latas) + 1
preco_latas = latas * 80

print("-"*100)
print("RESULTADO\n\n")
print("1ª situação")
print(f"Será necessário a compra de {latas} lata(s) de 18 litros, resultando num valor de R$ {preco_latas} reais.\n")

#para galões de 3,6 litros
galoes = litros/3.6

if(litros <= 3.6):
    galoes = 1
else:
    # galoes = galoes//1 + 1    --  tanto faz usar essa linha ou a linha abaixo
    galoes = int(galoes) + 1
preco_galoes = galoes * 25

print("2ª situação")
print(f"Será necessário a compra de {galoes} galão(ões) de 3.6 litros, resultando num valor de R$ {preco_galoes} reais.\n")

#para latas e galões
if(litros <= 18):
    galoes = litros/3.6
    if(galoes <= 3):
        latas = 0
        galoes = int(galoes) + 1
    else:
        latas = 1
        galoes = 0
else:
    latas = litros // 18
    sobra = litros % 18
    if(sobra/3.6 <= 3):
        galoes = (sobra // 3.6) + 1
    else:
        latas = latas + 1
        galoes = 0
preco_final = latas*80 + galoes*25
print("3ª situação")
print(f"De forma mais econômica, será necessário a compra de {latas} lata(s) de 18 litros e {galoes} galão(ões) de 3.6 litros, resultando num valor de R$ {preco_final} reais.")
print("-"*100)
