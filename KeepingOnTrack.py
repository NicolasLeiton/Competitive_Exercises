n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

k = 0
for i in adj:
    k+=1


def buscar(adj, pos):
    en_cola = 1
    for k in adj[pos]:
        if k not in visitados:    
            visitados.append(k)
            en_cola+=buscar(adj, k)
    return en_cola

desconectados = []
for i in range(n+1):
    global visitados
    visitados = []
    visitados.append(i)
    desconectados.append(0)
    for j in range(n):
        if j not in visitados:
            visitados.append(j)
            desconectados[i] += buscar(adj, j)*(n-len(visitados)+1)

print(desconectados)