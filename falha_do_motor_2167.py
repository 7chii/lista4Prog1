indice_saida = []
numero_de_casos = int(input())

casos = list(map(int,input().split()))

for i in range(1,numero_de_casos):
    if casos[i] < casos[i-1]:
        indice_saida.append(i)

if(len(indice_saida) == 0):
    print(0)
else:
    print(indice_saida[0] + 1)