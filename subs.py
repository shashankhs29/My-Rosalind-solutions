def motifsearch(a, b):
    la = len(a)
    listindex = [str(x+1) for x in range(la) if a.find(b, x) == x]
    ans = ""
    for y in listindex:
        ans+=(y + ' ')
    return ans[:-1]

fi = open("rosalind_subs.txt", "r")
m = fi.read()
n = m.splitlines()
p = n[0]
q = n[1]
print(motifsearch(p, q))
fi.close()
