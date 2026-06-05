from collections import OrderedDict

while True:
    try:
        m, n = map(int, input().split())
    except EOFError:
        break
    matrix = [{} for _ in range(n)]

    for i in range(m):
        index  = list(map(int, input().split()[1:]))
        vals  = list(map(int, input().split()))
        for j in range(len(index)):
            matrix[index[j]-1][i+1] = vals[j]

    print(n, m)

    for fila in matrix:
        ordenado = OrderedDict(sorted(fila.items()))
        print(len(ordenado), *ordenado.keys())
        print(*ordenado.values())