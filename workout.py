'''entrada = list(map(int, input().split()))
m = []
jim = []
for i in range(10):
    r = list(map(int, input().split()))
    m.append(r)
    jim.append(entrada[i*2]+entrada[i*2+1])

t = 0


for _ in range(3):
    for i in range(10):
        a, b, c = m[i]
        temp = (t)%(a+b)
        #
        if c<=temp<a+c:
            print(f"maquina {i+1}, t {t}, temp {temp}, suma {a+c-temp}, c {c}")
            t+=(a+c)-temp
        
        t+=jim[i]
        m[i][2]=(t-entrada[i*2])%(a+b)

t-=entrada[-1]
print(t)
'''
import sys

input = sys.stdin.readline

jim_data = list(map(int, input().split()))

jim_use = []
jim_rec = []

for i in range(10):
    jim_use.append(jim_data[2 * i])
    jim_rec.append(jim_data[2 * i + 1])

machines = []

for _ in range(10):
    u, r, t = map(int, input().split())
    machines.append([u, r, t])

time = 0

for round_ in range(3):
    for m in range(10):

        ju = jim_use[m]
        jr = jim_rec[m]

        u, r, s = machines[m]

        cycle = u + r

        # Avanzar los ciclos del otro usuario hasta que
        # el próximo uso pueda interferir con Jim.
        if s + u <= time:
            k = (time - (s + u)) // cycle + 1
            s += k * cycle

        # ¿Jim puede empezar o debe esperar?
        if s <= time < s + u:
            start = s + u
        elif time == s:
            start = s + u
        else:
            start = time

        finish = start + ju

        # Si el otro usuario quería comenzar mientras Jim
        # estaba usando la máquina, queda retrasado.
        if s < finish:
            s = finish + r

        machines[m][2] = s

        time = finish

        # No contar la última recuperación
        if not (round_ == 2 and m == 9):
            time += jr

print(time)