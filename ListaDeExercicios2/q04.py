lado1 = float(input("Digite o 1º lado do triângulo: "))
lado2 = float(input("Digite o 2º lado do triângulo: "))
lado3 = float(input("Digite o 3º lado do triângulo: "))

if (lado1 + lado2) > lado3:
    if (lado1 == lado2 and lado2 == lado3):
        print("Triângulo Equilátero: três lados iguais")
    elif (lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
        print("Triângulo Escaleno: três lados diferentes")
    else:
        print("Triângulo Isósceles: quaisquer dois lados iguais")
else:
    print("Os 3 lados não formam um triângulo!")

