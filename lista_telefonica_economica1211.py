while True:
    try:
        n = int(input())
        telefones = []
        for i in range(n):
            telefone = input()
            telefones.append(telefone)
        ultimaLinha = ""
        numPoupado = 0
        telefones.sort()
        for i in range(len(telefones)):
            if ultimaLinha != "":
                for j in range(len(telefones[i])):
                    if ultimaLinha[j] == telefones[i][j]:
                        numPoupado += 1
                    else:
                        break
            ultimaLinha = telefones[i]

        print(numPoupado)

    except EOFError:
        break

