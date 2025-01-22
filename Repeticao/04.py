a = 80000
b = 200000

ano = 0
while a < b:
    a += (3/100 * a)
    b += (1.5/100 * b)
    ano += 1

print(f"São necessários {ano} anos para a população de A superar a população de B")