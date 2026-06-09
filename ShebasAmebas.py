m, n = map(int, input().split())
matriz = []
for _ in range(m):
    fila = list(input())
    matriz.append(fila)



def buscar(matriz, fil, col):

    if m>fil+1:
        if matriz[fil+1][col]== "#":
            matriz[fil+1][col] = "."
            buscar(matriz, fil+1, col)
    if n>col+1:
        if matriz[fil][col+1]== "#":
            matriz[fil][col+1] = "."
            buscar(matriz, fil, col+1)
    
    if n>col+1 and m>fil+1:
        if matriz[fil+1][col+1]== "#":
            matriz[fil+1][col+1] = "."
            buscar(matriz, fil+1, col+1)
    if 0<col and m>fil+1:
        if matriz[fil+1][col-1]== "#":
            matriz[fil+1][col-1] = "."
            buscar(matriz, fil+1, col-1)
    if 0<col:
        if matriz[fil][col-1]== "#":
            matriz[fil][col-1] = "."
            buscar(matriz, fil, col-1)
    if n>col+1 and 0<fil:
        if matriz[fil-1][col+1]== "#":
            matriz[fil-1][col+1] = "."
            buscar(matriz, fil-1, col+1)

    if 0<fil:
        if matriz[fil-1][col]== "#":
            matriz[fil-1][col] = "."
            buscar(matriz, fil-1, col)
    if 0<col and 0<fil:
        if matriz[fil-1][col-1]== "#":
            matriz[fil-1][col-1] = "."
            buscar(matriz, fil-1, col-1)
    
    

figuras = 0

for i in range(m):
    for j in range(n):
        if matriz[i][j]=="#":

            matriz[i][j]="."
            figuras+=1
            buscar(matriz, i, j)
print(figuras)