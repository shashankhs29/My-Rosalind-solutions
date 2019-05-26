def dh(c, d):
    x = 0
    for i in range(len(c)):
        if c[i] != d[i]:
            x+=1
    return x

fi = open("rosalind_hamm.txt", "r")
a = fi.read()
b = a.splitlines()
c, d = b[0], b[1]
print(dh(c, d))
fi.close()
