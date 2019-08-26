def parsefasta(filename):
    seq, rawseq = {}, ''
    fi = open(filename, 'r')
    for x in fi:
        rawseq+=x
    rawseq = rawseq.splitlines()
    for stuff in rawseq:
        if stuff.startswith('>'):
            a = stuff[1:].rstrip('\n')
            seq[a] = ''
        else:
            seq[a] += stuff.rstrip('\n')
    final = list(seq.values())
    seqstr = final[0]
    return seqstr

def revcomp(a):
    comp = {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
    seq = ""
    for nt in a:
        seq+=comp[nt]
    rc = ''.join(reversed(seq))
    return rc

def revp(s):
    l = len(s)
    rcofs = revcomp(s)
    for i in range(l):
        for j in range(4, 13):
            if i + j > l:
                continue
            if s[i:i+j] == rcofs[l-i-j:l-i]:
                print("{0} {1}".format(i + 1, j))

print('Restriction site locations and lengths are as follows:')
revp(parsefasta('rosalind_revp.txt'))
