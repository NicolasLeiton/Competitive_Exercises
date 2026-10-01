from collections import defaultdict
T = int(input())

for _ in range(T):
    n = int(input())
    estudiantes = []
    parejas = defaultdict(set)

    for i in range(n):
        est = input().split()
        est[0]=int(est[0])

        for j in range(len(estudiantes)):
            est2=estudiantes[j]
            if abs(est[0]-est2[0])<=40 and est[1]!=est2[1] and est[2]==est2[2] and est[3]!=est2[3]:
                parejas[j].add(i)
                parejas[i].add(j)
            

        estudiantes.append(est)
    print(parejas)
    #personillas = n-len(parejas)
    #print(personillas)
    for _ in range(len(parejas)):
        key, objetos = max(parejas.items(), key=lambda x: len(x[1]))
        print(key, objetos)

        if len(parejas[key])==0:
            break
        for nov in objetos:
            parejas[nov].remove(key)
        parejas[key]=set()
        n-=1
        print(parejas)
    print(n)

    

    
    
