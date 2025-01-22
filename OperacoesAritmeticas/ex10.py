graus_celcius = float(input(("Digite uma temperatura em graus Celsius: ")))

# graus_celcius = 5 * ((graus_farenheit - 32) / 9)

graus_farenheit = ((graus_celcius/5)*9) + 32

print("O valor", graus_celcius, "em graus Celsius, é equivalente a", graus_farenheit, " em graus Farenheit")