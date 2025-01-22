import math
from xml.etree.ElementInclude import include

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca = idade < 12
adolescente = idade > 12


print (True if idade > 18 else False)
print (True if idade < 12 else False)
print (True if idade > 12 else False)
print (math.pi)

# print(maior_idade)
# print(crianca)
# print(adolescente)
