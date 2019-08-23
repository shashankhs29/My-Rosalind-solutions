def filedict(filename):
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
    return list(seq.values())

def lcsm(seq):
    lsub = ''
    for i in range(len(seq[0])):
        for j in range(len(seq[0])-i):
            if j>len(lsub) and all(seq[0][i:i+j] in x for x in seq):
                lsub = seq[0][i:i+j]
    return lsub

print('The longest common substring is:')
print(lcsm(filedict('rosalind_lcsm.txt')))
