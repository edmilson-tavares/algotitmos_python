tamanho_mb = float(input("Digite o tamanho do arquivo a ser baixado em MB:"))
velocidade_net_mbps = float(input("Digite a velocidade do link de internet em Mbps:"))

print("-"*70)
print("RESULTADO")
print(f"Será necessário um tempo de aproximadamente {round(((tamanho_mb*8)/velocidade_net_mbps)/60, 2)} minutos para baixar o arquivo completo.")
print("-"*70)
