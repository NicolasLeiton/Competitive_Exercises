n = int(input())

def gana(tablero, p):
    # filas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] == p:
            return True
    
    # columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i] == p:
            return True
    
    # diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == p:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == p:
        return True
    
    return False


for t in range(n):

    f1 = input()
    f2 = input()
    f3 = input()
    
    if t < n-1:
        input()  # línea vacía

    tablero = [f1, f2, f3]

    x = f1.count('X') + f2.count('X') + f3.count('X')
    o = f1.count('O') + f2.count('O') + f3.count('O')

    xwin = gana(tablero, 'X')
    owin = gana(tablero, 'O')

    if o > x or x > o + 1:
        print("no")
    elif xwin and owin:
        print("no")
    elif xwin and x != o + 1:
        print("no")
    elif owin and x != o:
        print("no")
    else:
        print("yes")