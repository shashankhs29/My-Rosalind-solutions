def countnt(seq):
    a, t, g, c = 0, 0, 0, 0
    for nt in seq:
        if nt == 'A':
            a+=1
        elif nt == 'C':
            c+=1
        elif nt == 'G':
            g+=1
        elif nt == 'T':
            t+=1
        else:
            continue
    print(f"{a} {c} {g} {t}")

print("Enter DNA strand:\n")
strand = input()
countnt(strand)
