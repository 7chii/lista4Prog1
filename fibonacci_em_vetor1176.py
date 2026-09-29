num_casos = int(input())

fib = [0, 1, 1]
for i in range(num_casos):
    num = int(input())
    if num <= len(fib) - 1:
        print(f'Fib({num}) = {fib[num]}')
    else:
        for i in range(num - (len(fib)-1)):
           proxFib = fib[-1] + fib[-2]
           fib.append(proxFib)
        print(f'Fib({num}) = {fib[num]}')