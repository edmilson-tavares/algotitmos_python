valor_hora = float(input("Digite o valor em R$ da sua hora de trabalho: "))
qtd_hora = float(input("Digite quantas horas você trabalha no mês: "))

salario_bruto = valor_hora*qtd_hora

if salario_bruto <= 0:
    print("Valor inválido!")
    exit()
elif salario_bruto <= 900:
    percentual_ir = 0
    ir = 0
    inss = 10/100 * salario_bruto
    fgts = 11/100 * salario_bruto
    sindicato = 3/100 * salario_bruto
elif salario_bruto <= 1500:
    percentual_ir = 5
    ir = percentual_ir / 100 * salario_bruto
    inss = 10 / 100 * salario_bruto
    fgts = 11 / 100 * salario_bruto
    sindicato = 3 / 100 * salario_bruto
elif salario_bruto <= 2500:
    percentual_ir = 10
    ir = percentual_ir / 100 * salario_bruto
    inss = 10 / 100 * salario_bruto
    fgts = 11 / 100 * salario_bruto
    sindicato = 3 / 100 * salario_bruto
else:
    percentual_ir = 20
    ir = percentual_ir / 100 * salario_bruto
    inss = 10 / 100 * salario_bruto
    fgts = 11 / 100 * salario_bruto
    sindicato = 3 / 100 * salario_bruto


print("-"*70)
print("FOLHA DE PAGAMENTO")
print(f"Salário Bruto: ({qtd_hora} * {valor_hora}): R$ {salario_bruto}")
print(f"(-) IR ({percentual_ir}%): R$ {ir}")
print(f"(-) INSS (10%): R$ {inss}")
print(f"(-) Sindicato (3%): R$ {sindicato}")
print(f"FGTS (11%): R$ {fgts}")
print(f"Total de descontos: R$ {ir+inss+sindicato}")
print(f"Salário Liquido: R$ {salario_bruto - (ir+inss+sindicato)}")
print("-"*70)