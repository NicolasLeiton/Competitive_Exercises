entrada = input()

def convertir(num, base):
    convertido = ""
    while num>=base:
        convertido= str(num%base) + convertido
        num = num//base
    convertido = str(num) + convertido
    return convertido
        


while entrada!="0":
    base, p, m = entrada.split()
    base = int(base)
    num = int(p, base=base)%int(m, base=base)
    if base == 10:
        print(num)
    else:
        print(convertir(num, base))
    entrada=input()