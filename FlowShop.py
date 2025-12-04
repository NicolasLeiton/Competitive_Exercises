n, m = list(map(int, input().split()))

tiempos = [list(map(int, input().split())) for i in range(n)]

salida = []

for i in range(1, m):
    tiempos[0][i] = tiempos[0][i]+tiempos[0][i-1]

for i in range(1, n):
    tiempos[i][0] = tiempos[i][0]+tiempos[i-1][0]
salida.append(tiempos[0][-1])
for fila in range(1, n):
    for col in range(1, m):
        tiempos[fila][col] = max(tiempos[fila-1][col], tiempos[fila][col-1])+tiempos[fila][col]
    salida.append(tiempos[fila][-1])
print(*salida)