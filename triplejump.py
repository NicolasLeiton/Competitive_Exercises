n = int(input()) - 1

saltos = list(map(int, input().split()))

a = saltos[0]//3
c = saltos[n]//3

b  = saltos[1] - 2*a

print(a,b,c)