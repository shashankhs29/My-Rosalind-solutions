def fastaparse(s):
    a = s.splitlines()
    strands = []
    y = ""
    i = 0
    while i<len(a):
        if a[i][0] != '>':
            y+=(a[i])
            i+=1
            for j in range(i, len(a)):
                if a[j][0] != '>':
                    y+=(a[j])
                    i+=1
                elif a[j][0] == '>':
                    break
            strands.append(y)
            y = ""
        else:
            i+=1
    return strands

def translation(strand):
    nt = ["T", "C", "A", "G"]
    ctable = [x + y + z for x in nt for y in nt for z in nt]
    aa = "FFLLSSSSYYxxCCxWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
    cdict = dict(zip(ctable, aa))
    codon = [strand[i:i+3] for i in range(0, len(strand)-3, 3)]
    prot = ''
    for nts in codon:
        if cdict[nts]=='x':
            break
        prot += cdict[nts]
    return prot

def splc(l):
    exon = l[0]
    for i in range(1, len(l)):
        exon = exon.replace(l[i], '')
    return translation(exon)

fi = open("rosalind_splc.txt", "r").read()
print(splc(fastaparse(fi)))
