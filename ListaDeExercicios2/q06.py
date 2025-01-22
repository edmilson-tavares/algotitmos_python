numero = int(input("Digite um número inteiro menor que 1000: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero - (centena * 100) - (dezena * 10)

if(centena == 0):
    msg = ""
elif(centena == 1):
    msg = str(centena) + " centena"
else:
    msg = str(centena) + " centenas"

if(dezena == 0):
    msg += ""
elif(dezena == 1):
    if centena > 0 and unidade > 0:
        msg += ", " + str(dezena) + " dezena e "
    elif centena == 0 and unidade > 0:
        msg += str(dezena) + " dezena e "
    elif centena > 0 and unidade == 0:
        msg += " e " + str(dezena) + " dezena"
    else:
        msg += str(dezena) + " dezena"
else:
    if centena > 0 and unidade > 0:
        msg += ", " + str(dezena) + " dezenas e "
    elif centena == 0 and unidade > 0:
        msg += str(dezena) + " dezenas e "
    elif centena > 0 and unidade == 0:
        msg += " e " + str(dezena) + " dezenas"
    else:
        msg += str(dezena) + " dezenas"

if(unidade == 0):
    msg += ""
elif(unidade == 1):

    if centena > 0 and dezena > 0:
        msg += str(unidade) + " unidade"
    elif centena == 0 and dezena > 0:
        msg += str(unidade) + " unidade"
    elif centena > 0 and dezena == 0:
        msg += " e " + str(unidade) + " unidade"
    else:
        msg += str(unidade) + " unidade"
else:
    if centena > 0 and dezena > 0:
        msg += str(unidade) + " unidades"
    elif centena == 0 and dezena > 0:
        msg += str(unidade) + " unidades"
    elif centena > 0 and dezena == 0:
        msg += " e " + str(unidade) + " unidades"
    else:
        msg += str(unidade) + " unidades"


print(f"{numero} = {msg}")