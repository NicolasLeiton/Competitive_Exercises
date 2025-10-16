import sys

casos = int(sys.stdin.readline())

for _ in range(1, casos+1):
    cantidad = int(sys.stdin.readline())
    numeros = list(map(int, sys.stdin.readline().split()))
    numeros.insert(0, 0)
    maxima = 0
    k_temp = 0
    for i in range(cantidad):
        dif = numeros[i+1]-numeros[i]
        if dif>maxima:
            maxima = dif
            k_temp = dif-1
        elif dif == k_temp:
             k_temp -=1
        elif k_temp < dif:
             maxima+=1
             k_temp=maxima
                
    print(f"Case {_}: {maxima}")
        