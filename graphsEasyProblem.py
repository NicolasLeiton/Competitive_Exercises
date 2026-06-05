from collections import defaultdict
while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break
    lista = list(map(int, input().split()))
    adyacencia = defaultdict(list)
    for i in range(n):
        adyacencia[lista[i]].append(i+1)


    for i in range(m):
        k, v = map(int, input().split())
        try:
            print(adyacencia[v][k-1])
        except:
            print(0)