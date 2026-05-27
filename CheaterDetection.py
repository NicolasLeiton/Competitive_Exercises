n = int(input())

for i in range(n):
    entrada = float(input())
    num = int(round(entrada * 1000))
    if num%15==0 or (num+5)%15==0:
        print("VALID")
    else:
        print("IMPOSSIBLE")
    
