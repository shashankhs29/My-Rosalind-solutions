def printlist(l):
    x = ""
    for i in range(len(l)):
        x += (str(l[i]) + ' ')
    print(x[:-1])

def maxof4(a, c, g, t):
    m = max(a, c, g, t)
    if m == a:
        return 'A'
    elif m == c:
        return 'C'
    elif m == g:
        return 'G'
    elif m == t:
        return 'T'

def fastaparse(s):
    a = s.splitlines()
    l = len(a)
    val = []
    y = ""
    i = 0
    while i<l:
        if a[i][0] == '>':
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
    return val

def cp(val):
    con = ""
    a, c, g, t = 0, 0, 0, 0
    al, cl, gl, tl = ['A: '], ['C: '], ['G: '], ['T: '] 
    for i in range(len(val[0])):
        for seq in val:
            if seq[i] == 'A':
                a+=1
            elif seq[i] == 'C':
                c+=1
            elif seq[i] == 'G':
                g+=1
            elif seq[i] == 'T':
                t+=1
        al.append(a), cl.append(c), gl.append(g), tl.append(t)
        con += maxof4(a, c, g, t)
        a, c, g, t = 0, 0, 0, 0 
    print(con)
    printlist(al)
    printlist(cl)
    printlist(gl)
    printlist(tl)

fi = open("rosalind_cons.txt", "r")
seq = fi.read()
seqfil = fastaparse(seq)
cp(seqfil)
fi.close()
