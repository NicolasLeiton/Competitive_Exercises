from heapq import *
from collections import deque, Counter
n = int(input())
todos = set(range(1, n+1))
v = []
u = []
for i in range(1, n+1):
    entrada = int(input())
    v.append(entrada)

puntas = list(todos- set(v))
heapify(puntas)
frecuencias = Counter(v)
v = deque(v)

def sacar():
    u.append(heappop(puntas))
    sacado = v.popleft()
    frecuencias[sacado] -= 1
    if frecuencias[sacado] == 0:
        heappush(puntas, sacado)
    
ok = True
for i in range(n):
    if len(puntas)<1:
        ok = False
        print("Error")
        break
    sacar()

if ok:
    for i in u:
        print(i)