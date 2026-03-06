def subarray(trac):
    neg, pos = 0, 0
    for i in trac:
        if i<0:
            neg+=1
        elif i>0:
            pos+=1

    i = 0
    j = len(trac) - 1 
    while (neg-pos)!=0:
        if i>j:
            break
        if neg<pos:
            if trac[i]>0:
                i+=1
                pos-=1
                continue
            elif trac[j]>0:
                j-=1
                pos-=1
                continue
        else:
            if trac[i]<0:
                i+=1
                neg-=1
                continue
            if trac[j]<0:
                j-=1
                neg-=1
                continue
        i+=1

    return j-i+1


n = int(input())
while n>0:
    trac = list(map(int, input().split()))
    d = max(trac)
    w = min(trac)
    if d<0:
        d = 0
    if w>0:
        w = 0
    r = subarray(trac)
    print(d, w, r)
    n = int(input())




