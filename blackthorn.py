s = input()
si = False
for i in range(len(s)-2):
    if s[i:i+3]=="kth":
        print("yes")
        si = True
        break
if si == False:
    print("no")