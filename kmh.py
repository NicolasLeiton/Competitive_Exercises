n = int(input())
max = 0

def llegar(num):
    num+=1
    while num%10!=0:
        num+=1
    return num

for _ in range(n):
    l = input()
    if l=="/":
        print(max)
        continue
    l = int(l)
    if l>=max:
        max=llegar(l)
    print(l)