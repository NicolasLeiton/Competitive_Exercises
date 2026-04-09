import math

n = input()
digitos = len(n)
suma = 0

for i in range(1, 1000000):
    suma+=math.log10(i)
    if digitos<10:
        if math.log10(int(n))<=suma+0.1:
            break
    elif int(suma)+1 == digitos:
        break
print(i)