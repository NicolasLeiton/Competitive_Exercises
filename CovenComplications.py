from collections import defaultdict
import bisect

n, m = map(int, input().split())

grafo = defaultdict(list)
ferrets = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

def drain(pos):
    drained = 0
    for i in grafo[pos+1]:
        drained+=ferrets[i-1]
    return drained

ataques = []
total = 0
salida = 0
for i in range(len(ferrets)):
    if ferrets[i]==0:
        drained = drain(i)
        total+=drained
        if drained>0:
            bisect.insort(ataques, -drained)

for i in ataques:
    total+=i
    salida+=total

print(salida)
