print("Cálculo do salário por horas trabalhadas")
print("\n")

ganho_hora = input('Quando você ganha por hora de trabalho: ')
ganho_hora = float(ganho_hora)

qtd_hora = input('Quantas horas você trabalha no mês: ')
qtd_hora = float(qtd_hora)

salario = qtd_hora * ganho_hora

print("Salário: R$ ", salario)

