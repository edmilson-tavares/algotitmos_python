print("-"*70)
print("DIAS DA SEMANA")
print("1 - Domingo")
print("2 - Segunda feira")
print("3 - Terça feira")
print("4 - Quarta feira")
print("5 - Quinta feira")
print("6 - Sexta feira")
print("7 - Sábado")
print("-"*70)

dia = int(input("Digite o dia correspondente da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda feira")
elif dia == 3:
    print("Terça feira")
elif dia == 4:
    print("Quarta feira")
elif dia == 5:
    print("Quinta feira")
elif dia == 6:
    print("Sexta feira")
elif dia == 7:
    print("Sábado")
else:
    print("Valor inválido!")