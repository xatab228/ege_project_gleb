a=[9999999]
for i in range(100):
    bin_n = bin(i)[2:]
    for k in range(2):
        count = bin_n.count('1')
        bin_n= bin_n + str(count%2)
    r=int(bin_n, 2)
    if r>123:
        a.append(r)
print(min(a))

