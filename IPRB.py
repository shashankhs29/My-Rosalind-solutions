def prob(k, m, n):
    t = k+m+n
    t_ = t-1
    kp = k/t
    mp = (m/t)*((k/t_)+(0.75*(m-1)/t_)+(0.5*n/t_))
    np = (n/t)*((k/t_)+(0.5*m/t_))
    return kp+mp+np

fi = open("rosalind_iprb.txt", "r")
a = fi.read()
b = a.split()
k = int(b[0])
m = int(b[1])
n = int(b[2])
print(prob(k, m, n))
fi.close()
