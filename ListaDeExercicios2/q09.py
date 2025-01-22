morango = float(input("Digite a quantidade(em kg) de morango: "))
maca = float(input("Digite a quantidade(em kg) de maça: "))

if morango <= 5:
    valor_morango = morango * 2.5
else:
    valor_morango = morango * 2.2

if maca <= 5:
    valor_maca = maca * 1.8
else:
    valor_maca= maca * 1.5

total_kg = morango + maca
total_rs = valor_morango + valor_maca

if total_kg > 8 or total_rs > 25:
    total_rs -= total_rs*0.1

print("-"*70)
print("FRUTEIRA")
print(f"Valor a ser pago: R$ {total_rs}")
print("-"*70)
