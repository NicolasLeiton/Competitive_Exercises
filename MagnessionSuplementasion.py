from collections import deque
import math
n,k, p = map(int, input().split())

ini = max(1, n//max(k, p))
fin = min(k, n)
#print("ini: ", ini, " fin: ", fin)
primeros = []
segundos = deque()

control = fin + 1

for i in range(ini, fin+1):
    if i>=control:
        break
    if n%i!=0:
        control=math.ceil(n/i)
        continue
    control = n//i
    if control<=p:
        primeros.append(i)
    if i<=p and control<=k and control!=i:
        segundos.appendleft(control)
    

print(len(primeros)+len(segundos))
for i in primeros:
    print(i)
for i in segundos:
    print(i)