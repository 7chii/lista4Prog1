numero_de_medidas = int(input())

alturas = list(map(int,input().split()))
eh_ou_nao_eh = True
subiuNaUltima = False

for i in range(numero_de_medidas - 1):
    if alturas[i] > alturas[i+1]:
        print(f'{i}:desceu')
        subiuAgora = False
        if subiuAgora == subiuNaUltima and i>0:
            eh_ou_nao_eh = False
            print(f'{i}:falseou')
        subiuNaUltima = subiuAgora
    elif alturas[i] < alturas[i+1]:
            print(f'{i}:subiu')
            subiuAgora = True
            if subiuAgora == subiuNaUltima and i > 0:
                eh_ou_nao_eh = False
                print(f'{i}:falseou')
            subiuNaUltima = subiuAgora
    else:
         print(f'{i}:manteve')
         eh_ou_nao_eh = False
         print(f'{i}:falseou')

print(int(eh_ou_nao_eh))