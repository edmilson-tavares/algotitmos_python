print("M para matutino\nV para vespertino\nN para nortuno")
turno = input("Digite o turno que você estuda: ")

turno = turno.lower()

if(turno == 'm'):
    print("Bom dia!")
elif(turno == 'v'):
    print("Boa tarde!")
elif(turno == 'n'):
    print("Boa noite!")
else:
    print("Turno inválido!")