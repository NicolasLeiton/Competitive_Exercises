n = int(input())

for i in range(n):
    num = int(float(input())*1000)
    if num%15==0 or (num+5)%15==0:
        print("VALID")
    else:
        print("IMPOSSIBLE")
    
