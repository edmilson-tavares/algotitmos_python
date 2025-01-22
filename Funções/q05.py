def somaImposto(taxaImposto, custo):
    return taxaImposto/100 * custo + custo

custo = float(input("Digite o valor do custo do produto: "))
taxa = float(input("Digite a taxa de imposto do produto: "))

valor_final = somaImposto(taxa, custo)
print(f"Valor final = R$ {valor_final:.2f}")