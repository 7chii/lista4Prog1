numero_de_linhas = int(input())
pares = []
impares = []
for i in range(numero_de_linhas):
    num = int(input())
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

pares.sort()
impares.sort(reverse=True)
for i in range(len(pares)):
    print(f'{pares[i]}')
for i in range(len(impares)):
    print(f'{impares[i]}')