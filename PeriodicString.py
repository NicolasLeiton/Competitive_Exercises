text = input()

def rotar(text):
    return text[-1]+text[:-1]

for i in range(1, len(text)+1):
    if i>len(text)//2:
        print(len(text))
        break
    if len(text)%i!=0:
            continue
    
    compar = rotar(text[:i])
    es = True
        
    for j in range(i, len(text)-i+1, i):
        #print(compar, text[j:j+i])
        if compar != text[j:j+i]:
            es = False
            break
        compar=rotar(compar)

    if es:
        print(i)
        break
