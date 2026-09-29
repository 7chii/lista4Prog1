listinha = []
ind = 0
for i in range(20):
    num = int(input())
    listinha.append(num)

for i in range(1,21):
    print(f'N[{ind}] = {listinha[-i]}')
    ind += 1