print("-"*70)
print("Calculadora básica + outras funções")
print("+ adição")
print("- subtração")
print("* nultiplicação")
print("/ divisão")
print("-"*70)

numero_1 = float(input("Digite o 1º número:"))
numero_2 = float(input("Digite o 2º número:"))
operador = input("Digite a operação a ser realizada: ")

if operador == "+":
    resultado = numero_1 + numero_2
elif operador == "-":
    resultado = numero_1 - numero_2
elif operador == "*":
    resultado = numero_1 * numero_2
elif operador == "/":
    resultado = numero_1 / numero_2
else:
    print("Operação inválida!")
    exit()

print(f"Resultado: {numero_1}{operador}{numero_2} = {resultado}")

if resultado % 2 == 0:
    print("O resultado da operação é um número par.")
elif resultado % 2 == 1:
    print("O resultado da operação é um número ímpar.")
else:
    print("")

if resultado >= 0:
    print("O resultado da operação é um número positivo.")
else:
    print("O resultado da operação é um número negativo.")

if resultado % 1 == 0:
    print("O resultado da operação é um número inteiro.")
else:
    print("O resultado da operação é um número decimal.")
