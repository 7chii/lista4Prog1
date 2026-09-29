num = int(input())
quadras = []
out = []
for i in range(num+1):
    linha = list(map(int,input().split()))
    quadras.append(linha)

for x in range(len(quadras) - 1):
    for y in range(len(quadras[x]) -1):
        quadra = []
        outir = ""
        count = 0
        lado_sup_esq = quadras[x][y]
        lado_sup_dir = quadras[x][y+1]
        lado_inf_esq = quadras[x+1][y]
        lado_inf_dir = quadras[x+1][y+1]
        quadra.append(lado_sup_esq)
        quadra.append(lado_sup_dir)
        quadra.append(lado_inf_esq)
        quadra.append(lado_inf_dir)
        for i in range(len(quadra)):
            if quadra[i] == 1:
                 count += 1
        if count >= 2:
            outir = 'S'
        else:
            outir = 'U'
        out.append(outir)
linha = ""

for i in range(len(out)):
    linha += out[i]

    if (i + 1) % num == 0:
        print(linha)
        linha = ""
