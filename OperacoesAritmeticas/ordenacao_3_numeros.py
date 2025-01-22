
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 >= num2 and num1 >= num3:
    if num2 >= num3:
        print(f"Ordem decrescente: {num1}, {num2}, {num3}")
    else:
        print(f"Ordem decrescente: {num1}, {num3}, {num2}")
elif num2 >= num1 and num2 >= num3:
    if num1 >= num3:
        print(f"Ordem decrescente: {num2}, {num1}, {num3}")
    else:
        print(f"Ordem decrescente: {num2}, {num3}, {num1}")
else:
    if num1 >= num2:
        print(f"Ordem decrescente: {num3}, {num1}, {num2}")
    else:
        print(f"Ordem decrescente: {num3}, {num2}, {num1}")