def function(n):
    bin_n = bin(n)[2:-1]
    if n % 2 ==0:
        bin_n += '01'
    else:
        bin_n += '10'
    return int(bin_n, 2)
counter = 1
while True:
    counter += 1
    if function(counter) == 2017:
        print(counter)
        break