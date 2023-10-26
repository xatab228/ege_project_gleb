def r(n):
    bin_n=bin(n)[2:]
    if n%5==0:
        bin_n1 = bin_n + '101'
    else:
        bin_n1 = bin_n + '1'
    if n%7==0:
        bin_n2 = bin_n1 + '111'
    else:
        bin_n2 = bin_n1 + '1'
    return(int(bin_n2, 2))
a=[-1]
for i in range(1000000):
    if r(i)<1855663:
        a.append(i)
print(max(a))
