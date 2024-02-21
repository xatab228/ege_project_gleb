for a in range(1000, 0, -1):
    if all( (x + 3*y > a) or (y<30) or (x<30) for x in range(1000) for y in range(1000)):
        print(a)