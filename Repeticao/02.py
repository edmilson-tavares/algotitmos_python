username = input("Digite seu usuário:")
password = input("Digite sua senha:")

while(username == password): # while(not (username != password))
    print("ERROR! Username e password idênticos.")
    username = input("Digite novamente seu usuário:")
    password = input("Digite novamente sua senha:")

else:
    print("Dados salvos com sucesso!")