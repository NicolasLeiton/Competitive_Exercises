import sys

def cases(virus):
    if virus == "A" or virus == "T":
        return "simple"
    revirus = virus[::-1]
    if virus[-1] == "C":
        results=cases(virus[:-1])
        if results == "simple" or results=="mutation":
            return "mutation"
    if virus[0] == "A":
        results = cases(virus[1:])
        if results == "simple" or results=="mutation":
            return "mutation"
    if revirus[0] == "A":
        results = cases(revirus[1:])
        if results == "simple" or results=="mutation":
            return "mutation"
    if revirus[0]=="G" and revirus[-1] == "C":
        results = cases(revirus[1:-1])
        if results == "simple" or results=="mutation":
            return "mutation"
    
    return "doomed"
    
    

for line in sys.stdin.readlines():
    n, virus = line.split()
    print(cases(virus))
