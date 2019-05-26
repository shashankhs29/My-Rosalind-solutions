nt = ["U", "C", "A", "G"]
ctable = [x + y + z for x in nt for y in nt for z in nt]
aa = "FFLLSSSSYYxxCCxWLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
cdict = dict(zip(ctable, aa))

def translation(strand):
	lstrand = list(strand)
	lstrand_ = [x for x in lstrand if x in nt]
	strand = ''.join(lstrand_)
	codon = [strand[i:i+3] for i in range(0, len(strand)-3, 3)]
	prot = ''
	for nts in codon:
		prot += cdict[nts]
	return prot

fi = open("rosalind_prot.txt", "r")
s = fi.read()
print(translation(s))
fi.close()
