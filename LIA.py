def fact(n):
    if n<2: return 1
    return n*fact(n-1)

def C(a,b):
    return fact(a)/(fact(b)*fact(a-b))

def lia(p,k,n):
    #p(AaBb) = 4/16, k = generation, n = atleast this many
    c = 2**k
    prob = 0
    if n<c/2:
        for j in range(n):
            prob += C(c, j)*(p**j)*((1-p)**(c-j))
        return 1-prob
    elif n>c/2:
        for j in range(n,c+1):
            prob += C(c, j)*(p**j)*((1-p)**(c-j))
        return prob

fi = open('rosalind_lia.txt', 'r').read()
a = fi.split()
k, n = int(a[0]), int(a[1])
print(k, n)
print(lia(0.25, k, n))
