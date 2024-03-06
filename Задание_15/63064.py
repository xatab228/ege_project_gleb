for a in range(0, 1000):
    if all(((x & 45 > 0) or (x & 89 > 0)) <= (x & a > 0) for x in range(1000)):
        print(a)