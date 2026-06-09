n, m = map(int, input().split())
matriz = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    matriz[a-1].append(b-1)
    matriz[b-1].append(a-1)

tuneles = 0
if n<=2:
    tuneles = n-1
    n = 0
for i in range(n):

    if len(matriz[i])<=1:
        compa = 2 - len(matriz[i])
        min=0
        while compa>0:
            
            for j in range(n):
                if i!=j and len(matriz[j])<=min and i not in matriz[j]:
                    matriz[i].append(j)
                    matriz[j].append(i)
                    tuneles+=1
                    compa-=1
                    if compa == 0:
                        break
            min+=1

print(tuneles)