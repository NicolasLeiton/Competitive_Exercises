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

def search_pattern(pattern: str, text: str) -> list[int]:
    concat = pattern + "ñ" + text  
    z = z_function(concat)
    p_len = len(pattern)
    matches = []
    
    for i in range(p_len + 1, len(concat)):
        if z[i] == p_len:
            matches.append(i - (p_len + 1))
            
    return matches

import sys
entrada = sys.stdin.readlines()
for i in range(0, len(entrada), 2):
    print(*search_pattern(entrada[i].strip(), entrada[i+1].strip()))