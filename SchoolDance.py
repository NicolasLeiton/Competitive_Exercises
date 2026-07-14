from collections import defaultdict
n, m, k = map(int, input().split())
parejas = defaultdict(set)
ocupados = set()
for i in range(k):
    boy, girl =map(int, input().split())
    if boy not in ocupados and -girl not in ocupados:
        parejas[-girl].add(boy)
        ocupados.add(-girl)
        ocupados.add(boy)
    else:
        parejas[boy].add(-girl)

def dfs(parejas, nodo, visitados, ocupados):
    visitados.add(nodo)
    for vecino in parejas[nodo]:
        if vecino<0 and vecino not in ocupados:
            parejas[nodo].remove(vecino)
            parejas[vecino].add(nodo)
            ocupados.add(nodo)
            ocupados.add(vecino)
            return True
        if vecino not in visitados and dfs(parejas, vecino, visitados, ocupados):
            parejas[nodo].remove(vecino)
            parejas[vecino].add(nodo)
            ocupados.add(nodo)
            ocupados.add(vecino)
            return True

    return False
        
for i in range(1, n+1):
    if i not in ocupados:
        dfs(parejas, i, visitados=set(), ocupados=ocupados)
    
print(len(ocupados)//2)
for i in range(-1, -m-1, -1):
    if len(parejas[i])==1:
        print(*parejas[i], -i)
