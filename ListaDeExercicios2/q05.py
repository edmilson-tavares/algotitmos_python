import math

print("-"*70)
print("RAÍZES DE UMA EQUAÇÃO DO SEGUNDO GRAU (aX² + bX + c = 0)")
print("-"*70)

a = float(input("Digite o valor de a: "))

if a == 0:
    print("Com a = 0, temos uma equação do 1º grau e não do 2º grau.")
else:
    b = float(input("Digite o valor de b: "))
    c = float(input("Digite o valor de c: "))
    delta = b**2 - 4 * a * c
    if delta < 0:
        print("Com delta < 0, temos uma equação com raízes reais.")
    elif delta == 0:
        raiz = (-1 * b)/(2 * a)
        print(f"Com delta = 0, temos apenas uma raíz {raiz}.")
    else:
        # raiz1 = ((-1 * b) + (delta**(1/2)))/ (2 * a)
        raiz1 = ((-1 * b) + math.sqrt(delta))/ (2 * a)
        raiz2 = ((-1 * b) - (delta**(1/2)))/ (2 * a)
        print(f"Com delta > 0, temos duas raízes: {raiz1} e {raiz2}.")
