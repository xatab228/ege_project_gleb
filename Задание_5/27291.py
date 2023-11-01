def function(n):
    bin_n = bin(n)[2:]
    bin_n = bin_n + str(bin_n.count('1') % 2)
    bin_n = bin_n + str(bin_n.count('1') % 2)
    return int(bin_n, 2)
a=[]
for i in range(1000):
    if function(i) < 90:
        a.append(function(i))
print(max(a))

