aux = 0
while(aux < 5):
    aux = 0
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    salario = float(input("Digite seu salário: "))
    sexo = input("Digite seu sexo(f ou m): ")
    estado_civil = input("Digite seu estado civil(s, c, v ou d): ")

    if(len(nome) <= 3):
        print("Nome inválido! Digite um nome com pelo menos 4 caracteres.")
        aux = 0
    else:
        aux += 1

    if(idade <= 0 or idade >=150):
        print("Idade inválida! Digite uma idade entre 0 e 150")
        aux = 0
    else:
        aux += 1

    if(salario < 0):
        print("Salário inválido! Digite uma salário maior que 0.")
        aux = 0
    else:
        aux += 1

    if (sexo != "m" and sexo != "f"):
        aux = 0
        print("Sexo inválido! Digite m para masculinho ou f para feminino.")
    else:
        aux += 1

    if(estado_civil != 's' and estado_civil != 'c' and estado_civil != 'v' and estado_civil != 'd'): #(estado_civil not in ['s', 'c', 'v', 'd']):
        print("Estado civil inválido!")
        aux = 0
    else:
        aux += 1


    if aux == 5:
        if (estado_civil == "s"):
            estado_civil = "Solteiro(a)"
        elif (estado_civil == "c"):
            estado_civil = "Casado(a)"
        elif (estado_civil == "v"):
            estado_civil = "Viúvo(a)"
        elif (estado_civil == "d"):
            estado_civil = "Divorciado(a)"
        else:
            estado_civil = "ERROR!"

        print(f"Dados salvos com sucesso!\n",
                f"Nome: {nome}\n",
                f"Idade: {idade}\n",
                f"Salário: R$ {salario}\n",
                f"Sexo: {"Masculinho" if (sexo == "m") else "Feminino"}\n",
                f"Estado civil: {estado_civil}")
