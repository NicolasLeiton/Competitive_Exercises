import math
r, n = list(map(int, input().split()))
caso = 1
while r!= 0 and n != 0:
    minima = math.ceil(r/n)-1
    if minima>26:
        print(f"Case {caso}: impossible")
    else:
        print(f"Case {caso}: {minima}")
    caso+=1
    r, n = list(map(int, input().split()))
