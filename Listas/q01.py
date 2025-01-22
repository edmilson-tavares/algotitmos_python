vetor = []

for i in range(5):
    vetor.append(float(input(f"Digite o {i+1} número: ")))

print("Vetor original: ")
print(vetor)
print("="*50)
print("Vetor invertido: ")
vetor.reverse()
print(vetor)
vetor.__reversed__()
print(vetor)