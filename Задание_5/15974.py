def N(n):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n += '10'
    else:
        bin_n += '01'
    return int(bin_n, 2)
for i in range(1000):
    if N(i) <= 102:
        print(i, N(i))