n=1
bin_n=bin(n)[2:]
a=[9999]
while n < 1000:
    for i in range(2):
        count = bin_n.count('1')
        bin_n = bin_n + str((count % 2))
    R=int(bin_n, 2)
    if R > 123:
        a.append(R)
    n+=1
print(min(a))


