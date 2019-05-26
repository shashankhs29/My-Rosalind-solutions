from string import whitespace
def revcomp(seq):
    nt = ['A', 'T', 'G', 'C']
    compdict = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    seqlist = [x for x in seq if x not in whitespace and x in nt]
    seqrev = ''.join(reversed(seqlist))
    seqrc = ""
    for i in seqrev:
        seqrc+=compdict[i]
    return seqrc

fi = open("rosalind_revc.txt", "r")
strand = fi.read()
print("Reverse compliment of given DNA strand:\n")
print(revcomp(strand))
fi.close()
