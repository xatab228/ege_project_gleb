def function(n):
    bin_n = bin(n)[2:]
    count1 = bin_n.count('1')
    if (len(bin_n) - count1) < count1:
        bin_n = bin_n + '1'
    else:
        bin_n = bin_n + '0'
    return int(bin_n, 2)
a=[]
for i in range(1000):
    if function(i) > 80:
        a.append(function(i))
print(min(a))