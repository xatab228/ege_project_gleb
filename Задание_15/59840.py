for a in range(1000, 0, -1):
    if all( (48 != y + 2 * x) or (a < x) or (a<y) for x in range(1000) for y in range(1000) ):
        print(a)