numero = int(input("Digite um número para ser gerado a tabuada: "))
print(f"Tabuada de {numero}:")

for i in range(1,11):
    print(f"{numero}x{i} = {numero * i}")

print("================================")



for i in range(10):
    print(f"{numero}x{i+1} = {numero * (i+1)}")