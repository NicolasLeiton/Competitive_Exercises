A = (['/', '/'], ['/', '+'])
B= (['-', '-'], ['-', '-'])
def mostrar(fig):
    for i in fig:
        for j in i:
            print(j, end="")
        print()

def replace(d):
    if d=='/':
        re = '\\'
    elif d == '\\':
        re = '/'
    elif d=='-':
        re = '|'
    elif d == '|':
        re = '-'
    else:
        re = d
    return re

def turn(fig1:list):
    turned = []
    fig= list(fig1)
    fig.reverse()
    for i in range(len(fig[0])):
        temp = []
        for j in range(len(fig)):
            temp.append(replace(fig[j][i]))
        turned.append(temp)
    return turned

def sew(fig1:list, fig2:list):
    sewed = []
    if len(fig1)!=len(fig2):
        raise Exception("error")
    
    for i in range(len(fig1)):
        sewed.append(fig1[i]+fig2[i])
    return sewed


import sys
text = ""
n = 1

for line in sys.stdin.readlines():
    line = line.strip()
    line = line.replace(" ","")
    text += line
    if len(text)>0 and ";" in text:
        temp = 0
        for i in range(len(text)):
            if text[i]==";":
                print(f"Quilt {n}:")
                n+=1
                try:
                    mostrar(eval(text[temp:i]))
                except:
                    print("error")
                temp=i+1
        text = text[temp:]
