# not(x & 105 == 0) or (not(x & 58 != 0) or (x & A != 0))


for A in range(0, 1000):
    if all(not (x & 105 == 0) or (not (x & 58 != 0) or (x & A != 0)) for x in range(1000)):
        print(A)
        break