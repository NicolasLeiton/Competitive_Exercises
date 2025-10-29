n, m = list(map(int, input().split()))
matriz=[input() for j in range(n)]

cantidad = 1
for i in range(m):
    if matriz[-1][i]=="_":
        cantidad+=1
        for j in range(n):
            if matriz[j][i]!="_":
                cantidad-=1
                break
print(cantidad)