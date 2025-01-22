area = float(input("Digite o tamanho em metros quadrados da área a ser pintada:"))

#para latas de 18 litros
litros = area/3
latas = litros/18

if(litros <= 18):
    latas = 1
else:
    latas = latas//1 + 1    #--  tanto faz usar essa linha ou a linha abaixo
    latas = int(latas) + 1

preco_latas = latas * 80

print("-"*70)
print("RESULTADO")
print(f"Será nececessário a compra de {latas} lata(s) de 18 litros, resultando num valor de R$ {preco_latas} reais.")
print("-"*70)
