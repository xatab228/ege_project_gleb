
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f1 = (x or not(y)) == (not(z) or w)
                f2 = (not(x) == y) == (not(z) or w)
                print(x, y, z, w, f1, f2)