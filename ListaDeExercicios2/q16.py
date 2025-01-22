print("-"*70)
print("Cálculo do fatorial de um número")
print("-"*70)
numero = int(input("Digite um número natural: "))
iterador = numero
fatorial = 1

while iterador != 1:
    fatorial *= iterador
    iterador -= 1

print("-"*70)
print("Resultado")
print(f"{numero}! = {fatorial}")
print("-"*70)

