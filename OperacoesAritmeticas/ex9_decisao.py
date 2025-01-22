x = input(' Me diga um número: ')
x = int(x)
y = input(' Me diga outro número: ')
y = int(y)
z = input(' Me diga mais um número: ')
z = int(z)

if x > y and x > z:
    maior = x
    aux = 1
elif y > x and y > z:
    maior = y
    aux = 2
else:
    maior = z
    aux = 3

if x < y and x < z:
    menor = x
    aux1 = 1
elif y < x and y < z:
    menor = y
    aux1 = 2
else:
    menor = z
    aux1 = 3

if aux == 1:
    if aux1 == 2:
        print("A sequência é: ", x, z, y)
    elif aux1 == 3:
        print("A sequência é: ", x, y, z)
elif aux == 2:
    if aux1 == 1:
        print("A sequência é: ", y, z, x)
    elif aux1 == 3:
        print("A sequência é: ", y, x, z)
else:
    if aux1 == 1:
        print("A sequência é: ", z, y, x)
    elif aux1 == 2:
        print("A sequência é: ", z, x, y)