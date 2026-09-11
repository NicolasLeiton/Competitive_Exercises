a="a"
b="d"
c="b"

def verificar(a,b,c):
    if c<a and c<b:
        print(-1)
    else:
        if c<a:
            a, b, c = a+a, b+c, c+a
        elif c<b:
            a, b, c = a+c, b+b, c+b
        else:
            a = a+c
            b = b+c
            c = c+c

        print(a)
        print(b)
        print(c)
    return a,b,c

a,b,c = verificar(a,b,c)
    

