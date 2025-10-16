import sys
n = int(sys.stdin.readline())

def letra_num(letra:str):
    pos="ABCDEFGH".find(letra)
    return pos

def num_letra(num:int):
    return "ABCDEFGH"[num]
def esquinas(dlet, dnum, hlet, hnum):
    for i in range(1, 8):
        if (dlet+i==hlet and dnum+i ==hnum):
            return True
        elif (dlet+i ==hlet and dnum-i==hnum):
            return True
        elif (dlet-i == hlet and dnum+i==hnum):
            return True
        elif dlet-i == hlet and dnum-i == hnum:
            return True
    return False
        
            
for _ in range(n):
    desdeletra, desdenum, hastaletra, hastanum = sys.stdin.readline().split()
    desdenum, hastanum = int(desdenum)-1, int(hastanum)-1
    desdeletra, hastaletra = letra_num(desdeletra), letra_num(hastaletra)
    
    if (desdeletra+desdenum)%2 != (hastaletra+hastanum)%2:
        print("Impossible")
        continue

    salida= f"{num_letra(desdeletra)} {desdenum+1}"

    if desdeletra==hastaletra and desdenum==hastanum:
        print(f"0 {salida}")
        continue
    if esquinas(desdeletra, desdenum, hastaletra, hastanum):
        print(f"1 {salida} {num_letra(hastaletra)} {hastanum+1}")
        continue
    else:
        for i in range(1,7):
            if desdeletra+i<8  and desdenum+i<8:
                if esquinas(desdeletra+i, desdenum+i, hastaletra, hastanum):
                    salida+= f" {num_letra(desdeletra+i)} {desdenum+i+1}"
                    break
            if -1<desdeletra-i<8  and desdenum+i<8:
                if esquinas(desdeletra-i, desdenum+i, hastaletra, hastanum):
                    salida+= f" {num_letra(desdeletra-i)} {desdenum+i+1}"
                    break

            if desdeletra+i<8  and -1<desdenum-i<8:
                if esquinas(desdeletra+i, desdenum-i, hastaletra, hastanum):
                    salida+= f" {num_letra(desdeletra+i)} {desdenum-i+1}"
                    break
            if -1<desdeletra-i<8  and -1<desdenum-i<8:
                if esquinas(desdeletra-i, desdenum-i, hastaletra, hastanum):
                    salida+= f" {num_letra(desdeletra-i)} {desdenum-i+1}"
                    break
        print(f"2 {salida} {num_letra(hastaletra)} {hastanum+1}")
            