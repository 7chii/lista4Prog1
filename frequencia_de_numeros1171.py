n = int(input())
dicion = {}
for i in range(0,n):
    num = int(input())
    
    if num not in dicion:
        dicion[num] = 1
    else:
        dicion[num] += 1
dicion = dict(sorted(dicion.items()))
for key in dicion:
    print(f'{key} aparece {dicion[key]} vez(es)')