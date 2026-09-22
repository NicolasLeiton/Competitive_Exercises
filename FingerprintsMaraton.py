def menol(text):
    tam = min(enumerate(text), key=lambda x: x[1])[0]
    text = text*2
    print(text[tam:(len(text)//2)+tam])


def verificar(unicas, text):
    for i in unicas:
        tam = len(i)//2
        if len(text)==tam:
            for j in range(tam):
                if text == i[j:tam+j]:
                    return
    menol(text)
    unicas.append(text*2)


n = int(input())
while n!=0:
    unicas = []
    for _ in range(n):
        x, text = input().split()
        verificar(unicas, text)
    #print(unicas)
    n = int(input())
    if n==0:
        break
    else:
        print()
