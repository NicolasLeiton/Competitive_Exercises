import sys

for line in sys.stdin.readlines():
    num = int(line)
    binario = str(bin(num))
    if num<=0:
        mascara = (1<<32)-1
        binario = str(bin(num & mascara))
        cadena=binario[3:].zfill(32)
    else: 
        cadena=binario[2:].zfill(32)

    convertido = cadena[-8:] + cadena[-16:-8] + cadena[-24:-16] + cadena [:-24]
    final =int(convertido, 2)
    if num<0:
        final -= 1 << 32
    
    print(f"{num} converts to {final}")