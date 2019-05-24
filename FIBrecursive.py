def recurserabbit(n, k):
    if n==1 or n==2:
        return 1
    else:
        return recurserabbit(n-1, k) + k*recurserabbit(n-2, k)
        
fi = open("rosalind_fib.txt", "r")
a = fi.read()
b = [int(x) for x in a.split()]
n = b[0]
k = b[1]
print(recurserabbit(n, k))
