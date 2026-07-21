from collections import defaultdict

def dfs(graph:dict, node:list, destino:int, visited=set(), suma=0):
    visited.add(node)
    if node[0] == destino:
        return suma+node[1]
    
    p = graph[1]
    max(p, key=lambda p:p[1] not in visited)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, suma)


graph = defaultdict(list)


n, m = map(int, input().split())
for _ in range(m):
    a, b, speed = map(int, input().split())
    graph[a].append((b, speed))
print(graph)
p = graph[1]
    
print()
'''
graph = {1: [(2, 3), (3, 4)],
        2: [(4, 2)],
        3: [(4, 5)],
        4: [(1, 3)]'''