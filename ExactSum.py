import sys, bisect

lines = sys.stdin.readlines()

def salida(vals:tuple):
    print(f"Peter should buy books whose prices are {vals[0]} and {vals[1]}.\n")

def buscar(l, r, prices, money):
    while True:
        if prices[l]+prices[r]==money:
            return (prices[l], prices[r])
        elif prices[l] + prices[r]>money:
            l -=1
        else:
            r +=1

for i in range(0, len(lines)-1, 4):
    #N = lines[i]
    prices = list(map(int, lines[i+1].split()))
    money = int(lines[i+2])
    mitad = money/2
    if prices.count(mitad)>1:
        mitad = int(mitad)
        salida((mitad, mitad))
        continue

    prices.sort()
    centro = bisect.bisect_left(prices, mitad)
    salida(buscar(centro-1, centro, prices, money))
