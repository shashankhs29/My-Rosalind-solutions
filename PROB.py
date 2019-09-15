from math import log10
def fileparse(fname):
    with open(fname) as stuff:
        flist = list(stuff)
    seqstr = flist[0]
    numseq = [float(x) for x in flist[1].split()]
    return seqstr, numseq

def prob(fname):
    seq, nums = fileparse(fname)
    logprob = []
    for gcvalues in nums:
        dnaprob = 1.0
        gc = gcvalues * 0.5
        at = (1-gcvalues) * 0.5
        for nt in seq:
            if nt == 'A':
                dnaprob*=at
            elif nt == 'T':                
                dnaprob*=at
            elif nt == 'G':
                dnaprob*=gc
            elif nt == 'C':
                dnaprob*=gc
        logprob.append(log10(dnaprob))

    return ' '.join(map(str, logprob))

print(prob('rosalind_prob.txt'))
