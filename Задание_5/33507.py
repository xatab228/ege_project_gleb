def main():
    N = 2
    while True:
        binNum = bin(N)[2:]
        newNum = binNum[:-1] + binNum[1] + binNum[1]
        R = int(newNum, 2)
        if R > 92:
            return N
        else:
            N += 1

print(main())
