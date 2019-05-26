def gc(dna):
    gccontent = 0
    for nts in dna:
        if nts == "G":
            gccontent+=1
        if nts == "C":
            gccontent+=1
    gcpercent = (gccontent/len(dna)) * 100
    return gcpercent

def fastaparse(s):
    a = s.splitlines()
    l = len(a)
    key = []
    val = []
    y = ""
    ans = []
    i, k = 0, 0
    while i<l:
        if a[i][0] == '>':
            key.append(a[i][1:])
            k+=1
            i+=1
        elif a[i][0] != '>':
            y+=(a[i])
            i+=1
            for j in range(i, l):
                if a[j][0] != '>':
                    y+=(a[j])
                    i+=1
                elif a[j][0] == '>':
                    break
            val.append(y)
            y = ""
        else:
            i+=1
    for v in val:
        ans.append(gc(v))
    x = max(ans)
    print(key[ans.index(x)])
    print(x)
    
fi = open("rosalind_gc.txt", "r")
seq = fi.read()
fastaparse(seq)
fi.close()
