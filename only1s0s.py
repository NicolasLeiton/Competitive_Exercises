n=9998
d = 1
m = ["1", "0", "0"]


def reset(m):
    return list("1" + "0"*(len(m)))

if n==1:
    print(1)
elif n==2:
    print(5)
elif n == 5:
    print(2)
else:
    while True:

        num=""
        for i in m:
            num+=i
        d = int(num)/n
        if d.is_integer():
            d = int(d)
            print(f"D={d}, m ={num}")
            break

        for i in range(1, len(m)):
            if m[-i]=="0" and m[-i-1]=="0":
                m[-i]="1"
                break
            if i>=len(m)-2:
                m = reset(m)
                break
            if m[-i]=="1" and m[-i-1]=="0" and m[-i-2]=="0":
                m[-i] = "0"
                m[-i-1] = "1"
                break
            
        


        
        
        