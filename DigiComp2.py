n, m = map(int, input().split())
grafo = [[0]]
bitmask = 0
for i in range(1, m+1):
    entrada = input().split()
    grafo.append([int(entrada[1]), int(entrada[2])])
    if entrada[0]=='R':
        bitmask |= (1 << (i-1))

combinaciones = [bitmask]


def convertir(bitmask):
    salida=""
    for i in range(m):
        if (bitmask >> i) & 1:
            salida += "R"
        else:
            salida += "L"
    print(salida)


for it in range(1, n+1):
    estoy = 1
    while estoy!=0:
        soy = (bitmask >> (estoy-1)) & 1
        bitmask ^= (1 << (estoy-1))
        if soy:
            estoy = grafo[estoy][1]
        else:
            estoy = grafo[estoy][0]
    
    combinaciones.append(bitmask)
    if bitmask==combinaciones[0]:
        convertir(combinaciones[n%it])
        break
    elif it==n:
        convertir(bitmask)

