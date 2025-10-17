import sys
def ordenar(pre, ino):
    global arbol
    #print(pre, ino, arbol)
    if len(ino)==1:
        arbol+=ino
        return
    
    for i, letra in enumerate(ino, 0):
        if letra == pre[0]:
            der = len(ino[:i]) +1
            ordenar(pre[1:], ino[:i])
            ordenar(pre[der:], ino[i+1:])
            arbol+= letra

global arbol
for line in sys.stdin.readlines():
    preord, inord = line.split()
    arbol =  "" #Nodo(preord[0])
    ordenar(preord, inord)
    print(arbol)
    
