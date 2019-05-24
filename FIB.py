def fib(n, k):
    #The answer is x(n) = f(n-1) + k*f(n-2)
    #This can be done using dynamic programming
    
    arr = [0, 1]
    for i in range(2, n+1):
        next = arr[1] + k*arr[0]
        arr[0] = arr[1]
        arr[1] = next
    return arr[1]
    
fi = open("rosalind_fib.txt", "r")
a = fi.read()
b = [int(x) for x in a.split()]
n = b[0]
k = b[1]
print(fib(n, k))
