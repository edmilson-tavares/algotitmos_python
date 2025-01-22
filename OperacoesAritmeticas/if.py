
# Solicita ao usuário que digite uma letra
letra = input("Digite uma letra: ").lower()

# Verifica se é uma letra do alfabeto
if letra.isalpha() and len(letra) == 1:
    # Verifica se é uma vogal
    if letra in 'aeiou':
        print(f"A letra '{letra}' é uma vogal.")
    else:
        print(f"A letra '{letra}' é uma consoante.")
else:
    print("O caractere digitado não é uma letra válida.")