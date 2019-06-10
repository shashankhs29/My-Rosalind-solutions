def iev(num):
    prob = [1, 1, 1, 0.75, 0.5, 0]
    #p(AAxAA) = 1, p(AAxAa) = 1, p(AAxaa) = 1
    #p(AaxAa) = 0.75, p(Aaxaa) = 0.5, p(aaxaa) = 0
    sum = 0
    for i in range(len(num)):
        sum+=(num[i]*prob[i])
    return sum*2

fi = open("rosalind_iev.txt", "r").read()
a = fi.split()
b = [int(x) for x in a]
print(iev(b))
