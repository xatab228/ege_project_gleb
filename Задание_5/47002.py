def main(n):
    bin_n = bin(n)[2:] + ' '
    chet = 0
    nechet = 0
    for i in range(len(bin_n)):
        if i % 2 == 0:
            if bin_n[i:i+1] == '1':
                chet += 1
        else:
            if bin_n[i:i+1] == '0':
                nechet += 1
    return abs(chet - nechet)

for i in range(1000):
    if main(i) == 4:
        print(i)