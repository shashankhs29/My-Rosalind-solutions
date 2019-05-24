from string import whitespace
def transcribe(seq):
    nt = ['A','T', 'G', 'C']
    seqlist = [x for x in seq if x not in whitespace]
    s1 = [y for y in seqlist if y in nt]
    s2 = ''.join(s1)
    rna = s2.replace('T', 'U')
    return rna

fi = open("rosalind_rna.txt", "r")
strand = fi.read()
print("Transcribed RNA strand:\n")
print(transcribe(strand))
