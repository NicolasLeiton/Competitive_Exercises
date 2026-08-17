def z_function(s: str) -> list[int]:
    n = len(s)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
            
    return z

def search_pattern(pattern: str, text: str, ini) -> list[int]:
    concat = pattern + "$" + text  # '$' es un caracter que no está en las cadenas
    z = z_function(concat)
    
    p_len = len(pattern)
    matches = True
    if p_len==ini:
        ini = 1
    tam = len(concat)
    for i in range(p_len+ini, len(concat), p_len):
        if z[i] != p_len:
            if i>len(concat)-p_len and z[i]==len(concat)-i:
                continue

            if ini<p_len and z[i-ini+1]==ini:
                continue
            matches=False
            break
        
    return matches
#text = "abcdfefghijgaf"
#text = "abcdabcdkabcdabcdk"
text = "cabcabca"
#text = "aaaaxaaaaaa"
z =z_function(text)
print(z)
print("Soy este", len(z)-z[-1])
#print(search_pattern("xaaa","aaaaxaaaaaa", 5))
min_pat = set(text)
pat= set()
pattern = ""
total = 0
desde = 0
for i in range(len(text)):
    pat.add(text[i])
    if len(pat)==len(min_pat) and text[i]==text[0]:
        if i*2<=len(text):
            pattern=text[i:i+i]
            desde = i
        else:
            pattern=text[:i]
            desde = i
        total = i
        
        print(pattern, i)
        break


if total==0:
    print(len(text))
else:
    while total<=len(text):
        if search_pattern(pattern, text, desde):
            break
        pattern+=text[total]
        total+=1
    print(total, pattern)
    '''
    ok = False
    while total<len(text):
        ok = True
        for i in range(desde, len(text), total):
            
            print(text[i:i+total],  pattern, total, i)
            if len(text)-i<total and text[i:i+total] == pattern[:len(text)-i]:
                print("QAID")
                break
            elif text[i:i+total] != pattern:
                print("NONO")
                ok = False
                break
        if ok:
            print(total)
            break
        pattern+=text[total]
        total+=1
    if not ok:
        print(total)
    '''
