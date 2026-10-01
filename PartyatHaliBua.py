from collections import deque, defaultdict

def bfs(graph, start):
    dist = {start: 0}
    queue = deque([start])
    contador=[1]
    contador2= [1, 0]
    while queue:
        node = queue.popleft()

        for neighbor in graph[node]:
            if neighbor not in dist:
                dist[neighbor] = dist[node] + 1
                if len(contador)<=dist[neighbor]:
                    contador.append(1)
                else:
                    contador[dist[neighbor]]+=1

                if dist[neighbor]%2!=0:
                    contador2[1]+=1
                else:
                    contador2[0]+=1
                queue.append(neighbor)

    return contador, dist



n = int(input())
while n!=0:
    grafo = defaultdict(list)
    jefe = input()
    grafo[jefe]=[]
    for i in range(n-1):
        persona, jefecito = input().split()
        grafo[jefecito].append(persona)

    
    salida = bfs(grafo, jefe)
    print(salida)
    print(max(salida), end=" ")
    if salida[0]==salida[1]:
        print("No")
    else:
        print("Yes")
    n = int(input())

