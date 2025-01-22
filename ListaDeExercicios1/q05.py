valor_hora = float(input("Digite o valor da hora de trabalho: "))
qtd_hora_trabalhada = float(input("Digite quantas horas você trabalha no mês: "))
salario_bruto = valor_hora * qtd_hora_trabalhada

ir = 11/100 * salario_bruto
inss = 8/100 * salario_bruto
sindicato = 5/100 * salario_bruto
salario_liquido = salario_bruto - ir - inss - sindicato

print("-"*70)
print("RESULTADO")
print(f"+Salário bruto: R$ {round(salario_bruto, 2)}")
print(f"-IR: R$ {round(ir, 2)}")
print(f"-INSS: R$ {round(inss, 2)}")
print(f"-Sindicato: R$ {round(sindicato, 2)}")
print(f"=Salário líquido: R$ {round(salario_liquido, 2)}")
print("-"*70)