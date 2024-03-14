for a in range(0, 1000):
    if all(((x & 57 > 0) or (x & 99 > 0)) <= (x & a > 0) for x in range(0, 100000)):
        print(a)