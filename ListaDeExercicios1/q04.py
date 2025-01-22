peso = float(input("João, informe quantos kg de peixe você pegou hoje: "))

# excesso = peso % 50 if (peso // 50 > 1) else 0
excesso = peso - 50 if (peso - 50 > 0) else 0
multa = excesso * 4

print("-"*70)
print("RESULTADO")
print(f"João, o excesso de hoje foi de {round(excesso, 2)} kg. Sendo assim, sua multa será de R$ {round(multa, 2)} reais!")
print("-"*70)