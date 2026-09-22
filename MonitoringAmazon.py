from math import sqrt 
from collections import deque
n = int(input())

def distancia(x1,y1,x2,y2):
    return sqrt((x2-x1)**2+(y2-y1)**2)

def definir(i, dist, anterior):
    if dist<anterior[1]:
        return (i, dist)
    elif dist==anterior[1]:
        if puntos[i]<puntos[anterior[0]]:
            return (i, dist)
        elif puntos[i]==puntos[anterior[0]] and puntos[i+1]<puntos[anterior[0]+1]:
            return (i, dist)
    return anterior


while n!=0:
    puntos = list(map(int, input().split()))
    cola = deque([0])
    visitados = set()
    visitados.add(0)
    while cola:
        a = cola.popleft()
        soy = (puntos[a], puntos[a+1])
        vecinos =[]
        for i in range(2, n*2-1, 2):
            #print("i", i)
            if i==a:
                continue
            dist = distancia(*soy, puntos[i], puntos[i+1])
            if len(vecinos)<2:
                vecinos.append((i, dist))
                continue
            vecinos.sort(key=lambda p: p[1], reverse=True)
            entonces = definir(i, dist, vecinos[0])
            if entonces!=vecinos[0]:
                vecinos[0]=entonces
            else:
                vecinos[1]=definir(i, dist, vecinos[1])

        for i in vecinos:
            if i[0] not in visitados:
                cola.append(i[0])
                visitados.add(i[0])
        #print(soy, vecinos)
        if len(visitados)>=n:
            print("All stations are reachable.")
            break
    if len(visitados)<n:
        print("There are stations that are unreachable.")
            
    n = int(input())