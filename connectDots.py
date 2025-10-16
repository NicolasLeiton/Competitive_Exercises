import sys
orden = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
images = list(map(list, sys.stdin.readlines()))
global encontrado
encontrado = ".-|+"
def replace(pos1, pos2, forma):
    actual =images[pos1][pos2]
    if (actual=="-" and forma=="|") or (forma=="-" and actual=="|"):
        images[pos1][pos2]="+"
    elif actual==".":
        images[pos1][pos2]=forma

def buscar(pos1, pos2):
    global encontrado
    pos0=orden.find(images[pos1][pos2])
    ady = [orden[pos0-1], orden[pos0+1]]
    if (orden[pos0-2] in encontrado and pos0>=2) or "0" == ady[0]:
        encontrado += ady[0]
    elif pos0<len(orden):
        if orden[pos0+2] in encontrado:
            encontrado+=ady[1]

    for i in range(len(images)-pos1):
        if images[pos1+i][0]=='\n':
            break
        if images[pos1+i][pos2] in ady:
            ady.remove(images[pos1+i][pos2])
            for j in range(1,i):
                replace(pos1+j, pos2, "|")
        if len(ady)==0:
            return
            
    for i in range(len(images[pos1])-pos2):
        if images[pos1][pos2+i] in ady:
            ady.remove(images[pos1][pos2+i])
            for j in range(1,i):
                replace(pos1, pos2+j, "-")
        if len(ady)==0:
            return

for i in range(len(images)):
    if images[i][0]=="\n":
            encontrado = ".-|+"
            continue
    for j in range(len(images[i])-1):
        if images[i][j] not in encontrado:
            buscar(i,j)

for i in images:
    for j in i:
        print(j, end="")