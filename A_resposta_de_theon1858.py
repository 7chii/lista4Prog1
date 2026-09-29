n = int(input())
t = list(map(int, input().split()))

menor = min(t)
print(t.index(menor) + 1)