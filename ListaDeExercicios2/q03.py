
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))

media = (nota1 + nota2)/2
if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
    print("Notas inválidas!")
    exit()
elif media >= 9 and media <= 10:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media >= 0 and media < 4:
    conceito = "E"

if(conceito == "A" or conceito == "B" or conceito == "C"):
    print(f"APROVADO, conceito {conceito}!")
else:
    print(f"REPROVADO, conceito {conceito}!")
